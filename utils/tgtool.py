# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fortify
   Description :
   Author :       admin
   date：          2020/1/16
-------------------------------------------------
   Change Activity:
                   2020/1/16:
-------------------------------------------------
"""
__author__ = 'admin'

import telegram
import logging
import os
import configparser
import jenkins
import argparse
import time
from pprint import pprint
import subprocess
from datetime import datetime

import traceback
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

currpath = os.path.dirname(os.path.realpath(__file__))

"""
TG 消息推送
"""



def execcmd(command):
    """
    执行命令
    :param command:
    :return:
    """
    # print("command=%s" % command)

    output = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        universal_newlines=True)

    stderrinfo, stdoutinfo = output.communicate()
    return (output.returncode, stderrinfo, stdoutinfo)

def string2timestamp(strValue):
    try:
        strValue = strValue.replace('/', '-').replace(',', '.')
        d = datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S.%f")
        t = d.timetuple()
        timeStamp = int(time.mktime(t))
        timeStamp = float(str(timeStamp) + str("%06d" % d.microsecond)) / 1000000

        return timeStamp
    except ValueError as e:
        strValue = strValue.replace('/', '-')
        d = datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S")
        t = d.timetuple()
        timeStamp = int(time.mktime(t))
        timeStamp = float(str(timeStamp) + str("%06d" % d.microsecond)) / 1000000

        return timeStamp

def getDateTime():
    '''
    获取当前日期时间，格式'20150708085159'
    '''
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def timestamp2string(timeStamp):
    try:
        d = datetime.fromtimestamp(timeStamp)
        str1 = d.strftime("%Y-%m-%d %H:%M:%S")
        return str1
    except Exception as e:
        print(traceback.format_exc())
        return ''

class MyTelegramBot(object):
    """
    处理TG 发送消息
    """
    def __init__(self):

        config = configparser.ConfigParser()
        config.read('{0}/../config/sscconfig.ini'.format(currpath), encoding='utf-8-sig')
        self._jenkins_url = config.get('JENKINS', 'JENKINS_URL')
        self._jenkins_user = config.get('JENKINS', 'JENKINS_USER')
        self._jenkins_api_token = config.get('JENKINS', 'JENKINS_API_TOKEN')
        self._sonar_url = config.get('SONAR', 'SONAR_URL')
        self._tg_token = config.get('telegram','TG_TOKEN')
        self._tg_chat_id = config.get('telegram','CHAT_ID')
        self._tg_chat_id_op = config.get('telegram','CHAT_ID_OP')
        self._tg_chat_id_ot = config.get('telegram','CHAT_ID_OT')
        self._tg_chat_id_cb = config.get('telegram','CHAT_ID_CB')
        self.bot = telegram.Bot(token=self._tg_token)
        self.server = jenkins.Jenkins(self._jenkins_url, username=self._jenkins_user, password=self._jenkins_api_token)

    def get_build_num(self,job_name):
        build_number = 0
        if self.server.job_exists(job_name):
            job_dict = self.server.get_job_info(job_name)
            build_number = job_dict['lastBuild']['number']

        return build_number

    def get_jenkins_job_info(self,job_name):
        """
        通过job 名称获取构建信息
        :param job_name:
        :return:
        """

        number = self.get_build_num(job_name)
        build_dict = {'username': None, 'sonarqubeDashboardUrl': None, 'artifacts': None, 'branch': None,
                      'attach': None, 'model': None,'timestamp': None}

        if number != 0:

            build_info = self.server.get_build_info(job_name, number)
            pprint(build_info)
            try:

                build_dict['sonarqubeDashboardUrl'] = build_info['actions'][9]['url']
            except:
                pass
            try:
                build_dict['username'] = build_info['actions'][1]['causes'][0]['userName']
            except:
                pass
            try:
                artifacts = build_info['artifacts'][0]['relativePath']
                build_dict['artifacts'] = artifacts
            except:
                pass
            try:
                build_dict['branch'] = build_info['actions'][0]['parameters'][0]['value']
            except:
                pass
            try:
                build_dict['attach'] = build_info['actions'][0]['parameters'][2]['value']
            except:
                pass
            try:
                build_dict['model'] = build_info['actions'][0]['parameters'][1]['value']
            except:
                pass
            try:
                build_dict['timestamp'] = build_info['timestamp']
            except:
                pass

        return build_dict

    def get_chat_id(self):
        return self.bot.get_updates(read_latency=5)
    def post_tg(self, job_name, notify_type='singal', chatid_type='none'):
        """
        通过机器人发送 代码扫描结果 通知
        :param job_name:
        :param notify_type singal 单项目扫描通知  sonar 汇总通知 fortify 汇总通知
        :param chat_id 群组ID
        :return:
        """

        job_info = self.get_jenkins_job_info(job_name)
        username = 'admin' if job_info['username'] ==None else job_info['username']
        scanTime = getDateTime() if job_info['timestamp'] is None else timestamp2string(job_info['timestamp'] / 1000)
        duration = 0 if job_info['timestamp'] is None else round(time.time()-job_info['timestamp'] /1000,3)

        if chatid_type == 'OP':
            chatid = self._tg_chat_id_op
        elif chatid_type == 'OT':
            chatid = self._tg_chat_id_ot
        elif chatid_type == 'CB':
            chatid = self._tg_chat_id_cb
        else:
            chatid = self._tg_chat_id

        if job_info == None:

            message = """
                ##########################################
             构建异常！！！！！！！！！！！！！！
            ##########################################
            """
        else:
            if notify_type =='sonar':

                message = """
   ##########################################
   #☆刚刚执行完成Sonar统计报告的生成#
   ##########################################
   #☆统计报告时间:  {scanTime}
   #☆生成报告耗时:  {duration}秒
   #☆汇总统计报告:  <a href="{jenkins_url}/job/{job_name}/ws//Sonar/Sonar_Sumarry.xlsx"> 统计报告下载</a>
   ##########################################
               """.format(jenkins_url=self._jenkins_url, job_name=job_name, username=username, scanTime=scanTime,duration=duration)
            elif notify_type == 'fortify':

                message = """
   ##########################################
   #☆刚刚执行完成Fortify 统计报告的生成#
   ##########################################
   #☆统计报告时间:  {scanTime}
   #☆生成报告耗时:  {duration}秒
   #☆汇总统计报告:  <a href="{jenkins_url}/job/{job_name}/ws/FortifyResult/FortifySumarry.xlsx"> 统计报告下载</a>
   ##########################################
               """.format(jenkins_url=self._jenkins_url, job_name=job_name, username=username, scanTime=scanTime,duration=duration)
            else:
                project_name = '{0}-{1}'.format(job_name.split('-')[1],job_info['model'])
                sonar_url = '{0}{1}'.format(self._sonar_url, project_name) if job_info['sonarqubeDashboardUrl'] is None else job_info['sonarqubeDashboardUrl']
                branchname = 'develop' if job_info['branch'] is None else job_info['branch'].split('/')[-1]
                artifacts_str = 'FortifyResult/{0}_of_{1}-fortify-result.xlsx'.format(project_name, branchname) if job_info['artifacts'] is None else job_info['artifacts']
                model = job_info['model']
                attachtype = "增量扫描" if job_info['attach'] =='True' else '全量扫描'
                message = """  ##########################################
    #☆刚刚执行完成代码扫描，扫描结果如下 ：#
    ##########################################
     扫描人员:  {username}
     扫描分支:  {branchname}
     扫描模块:  {model}
     扫描模式:  {attachtype}
     扫描时间:  {scanTime}
     扫描耗时： {duration} 秒
     安全扫描:  <a href="{jenkins_url}/job/{job_name}/ws/{artifacts_str}"> ☆{project_name}☆ Fortify静态代码扫描报告</a>
     Sonar扫描: <a href="{sonar_url}"> ☆{project_name}☆ Sonar代码规范扫描详情</a>
    ##########################################
                """.format(username=username, model=model, branchname=branchname, attachtype=attachtype, jenkins_url=self._jenkins_url, project_name=project_name, job_name=job_name,
                           artifacts_str=artifacts_str, sonar_url= sonar_url, scanTime=scanTime, duration=duration)

        self.bot.send_message(chat_id=chatid, text=message, parse_mode=telegram.ParseMode.HTML)


def arg_parser():
    parser = argparse.ArgumentParser(description='Telegram 通知程序')
    parser.add_argument('-j', '--jobname', help="jenkins job 名称", dest="jobname")
    parser.add_argument('-n', '--notify_type', help="通知类型", dest="notify_type")
    parser.add_argument('-c', '--chat_id_type', help="群组ID类型", dest="chat_id_type")
    args = parser.parse_args()

    logger.info(args)

    return args

def main(args):
    job_name = args.jobname.strip()
    tg = MyTelegramBot()
    notify_type = 'singal' if args.notify_type is None else args.notify_type.strip()
    chatid_type = 'none' if args.chat_id_type is None else args.chat_id_type.strip().upper()
    tg.post_tg(job_name, notify_type, chatid_type)


if __name__ == "__main__":
    main(arg_parser())
    # job_name = 'scan-OP-NETGAME'
    # job_name_fortify ='statistics-orient-fortifyReport'
    # job_name_sonar = 'statistics-orient-sonarReport'
    # tg = MyTelegramBot()
    # build_dict = tg.get_jenkins_job_info(job_name)
    #
    # tg.post_tg(job_name,notify_type=None)
