#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sonarReport
   Description :
   Author :       admin
   date：          2020/1/5
-------------------------------------------------
   Change Activity:
                   2020/1/5:
-------------------------------------------------
"""
__author__ = 'admin'
import json
import requests
import requests.auth
import requests.exceptions
import requests.packages.urllib3
import os
import sys
import configparser
import xlsxwriter
from utils.BaseReport import OperateReport
import traceback
import argparse
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

currpath = os.path.dirname(os.path.realpath(__file__))

config = configparser.ConfigParser()
config.read('{0}/../config/sscconfig.ini'.format(currpath), encoding='utf-8-sig')
SONAR_HOST = config.get('SONAR','SONAR_HOST')

class SonarStatisticsReport(object):

    def __init__(self, host=SONAR_HOST, username=None, password=None, token=None, verify_ssl=True, timeout=60, user_agent=None):
        self.host = host
        self.username = username
        self.password = password
        self.token = token
        self.verify_ssl = verify_ssl
        self.timeout = timeout
        self.user_agent = user_agent
        if username is not None:
            self.auth_type = 'basic'
        else:
            self.auth_type = 'unauthenticated'

    def _request(self, method, url, params=None, files=None, data=None, headers=None, stream=False):
        """Common handler for all HTTP requests."""
        if not params:
            params = {}

        if not headers:
            headers = {
                'Accept': 'application/json'
            }
            if method == 'GET' or method == 'POST' or method == 'PUT':
                headers.update({'Content-Type': 'application/json'})
        headers.update({'User-Agent': self.user_agent})

        try:

            if self.auth_type == 'basic':
                response = requests.request(method=method, url=self.host + url, params=params, files=files,
                                            headers=headers, data=data,
                                            timeout=self.timeout, verify=self.verify_ssl,
                                            auth=(self.username, self.password), stream=stream)
            else:
                response = requests.request(method=method, url=self.host + url, params=params, files=files,
                                            headers=headers, data=data,
                                            timeout=self.timeout, verify=self.verify_ssl, stream=stream)

            try:
                response.raise_for_status()

                # two flavors of response are successful, GETs return 200, PUTs return 204 with empty response text
                response_code = response.status_code
                success = True if response_code // 100 == 2 else False
                if response.text:
                    try:
                        data = response.json()
                    except ValueError:  # Sometimes the returned data isn't JSON, so return raw
                        data = response.content

                return SonarResponse(success=success, response_code=response_code, data=data,
                                       headers=response.headers)
            except ValueError as e:
                return SonarResponse(success=False, message="JSON response could not be decoded {0}.".format(e))

        except requests.exceptions.SSLError as e:

            return SonarResponse(message='An SSL error occurred. {0}'.format(e), success=False)

        except requests.exceptions.ConnectionError as e:

            return SonarResponse(message='A connection error occurred. {0}'.format(e), success=False)

        except requests.exceptions.Timeout:

            return SonarResponse(message='The request timed out after ' + str(self.timeout) + ' seconds.',success=False)

        except requests.exceptions.RequestException as e:

            return SonarResponse(message='There was an error while handling the request. {0}'.format(e), success=False)

    def get_projects_list(self,filter='ALL'):
        if filter =='ALL':
            url = "/api/components/search_projects?ps=500"

        # if fiter=='sz':
        #     url = "/api/components/search_projects?ps=100&filter=query = \"sz-\""
        # elif fiter=='sh':
        #     url = "/api/components/search_projects?ps=100&filter=query = \"sh-\""
        # elif fiter=='all':
        #     url = "/api/components/search_projects?ps=500"
        else:
            #url = "/api/components/search_projects?ps=500"
            url = "/api/components/search_projects?ps=100&filter=query = \""+fiter+"-\""

        try:
            response = self._request('GET', url)
            project_list = []
            for application in response.data['components']:
                project_list.append(application['key'])

            project_list_str = ','.join(project_list)
        except TypeError:
            project_list_str =''


        return  project_list_str

    def get_all_metrics_by_projectlsitstr(self,filter,metricKeys):
        url = "/api/measures/search?projectKeys="+filter+"&metricKeys="+metricKeys
        reportdict = dict()
        try:
            response = self._request('GET', url)
            for measure in response.data['measures']:
                component = measure['component']
                if component in reportdict.keys():
                    key = measure['metric']
                    value = measure['value']
                    reportdict[component][key] = value
                else:
                    reportdict[component] = dict()

                    key = measure['metric']
                    value = measure['value']
                    reportdict[component][key] = value
            return reportdict

        except TypeError:
            return reportdict
        except KeyError:
            return reportdict




class SonarResponse(object):
    """Container for all Fortify SSC API responses, even errors."""

    def __init__(self, success, message='OK', response_code=-1, data=None, headers=None):
        self.message = message
        self.success = success
        self.response_code = response_code
        self.data = data
        self.headers = headers

    def __str__(self):
        if self.data:
            return str(self.data)
        else:
            return self.message

    def data_json(self, pretty=False):
        """Returns the data as a valid JSON string."""
        if pretty:
            return json.dumps(self.data, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            return json.dumps(self.data)


def GenSonarReport(sonarip=SONAR_HOST,Metrickeys='bugs,vulnerabilities,code_smells,duplicated_lines_density,line_coverage,branch_coverage,complexity',distribute='all', workspacepath=None):
    sp = SonarStatisticsReport(host=sonarip)
    projectkeys = sp.get_projects_list(distribute)

    sonarinfo = sp.get_all_metrics_by_projectlsitstr(projectkeys,Metrickeys)
    if workspacepath == None:
        reportdir = os.path.dirname(os.path.realpath(__file__)) + '/Sonar'
    else:
        reportdir = workspacepath + '/Sonar'

    if not os.path.exists(reportdir):
        os.makedirs(reportdir)

    try:
        for file in os.listdir(reportdir):
            path_file = os.path.join(reportdir, file)  # 取文件路径
            if os.path.isfile(path_file):
                os.remove(path_file)
        workbook = xlsxwriter.Workbook(reportdir + '/Sonar_Sumarry' + '.xlsx')

        bo = OperateReport(workbook)
        bo.SonarReport(sonarinfo)
        bo.close()

    except Exception:

        logger.error('生成报告失败：{}'.format(traceback.print_exc()))

        return -1

def arg_parser():
    parser = argparse.ArgumentParser(description='Sonar报告生成工具，支持全量报告生成')
    parser.add_argument('-d', '--sonar-distribute', default='sz', help="输入按哪个区域生成报告", dest='distribute',required=True)

    parser.add_argument('-u', '--Sonar-host', help="输入sonar地址", dest="host",required=True)

    parser.add_argument('-m', '--Sonar-Metrics', help="输入度量维度列表", dest="MetricKeys",required=True)

    parser.add_argument('-r', '--Sonar-reportpath', help="输入生成报告目录", dest="reportpath",required=True)


    args = parser.parse_args()

    logger.info(args)

    return args

def main(args):
    distribute = args.distribute
    reportpath = args.reportpath
    host = args.host
    MetricKeys=args.MetricKeys
    GenSonarReport(host,MetricKeys,distribute,reportpath)



if __name__ == '__main__':
    #
    #python3 sonarReport.py -d sz -r '/Users/heyingqin528/develop/imi-test-doc/fortifyReportTools' -u 'http://10.161.46.134:9000' -m bugs,vulnerabilities,code_smells,duplicated_lines_density,coverage,line_coverage,branch_coverage,complexity
    main(arg_parser())
    #GenSonarReport(sonarip=SONAR_HOST,Metrickeys='bugs,vulnerabilities,code_smells,duplicated_lines_density,line_coverage,branch_coverage,complexity',distribute='ALL',workspacepath=None)
