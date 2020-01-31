# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     BaseReport
   Description :
   Author :       admin
   date：          2020/1/5
-------------------------------------------------
   Change Activity:
                   2020/1/5:
-------------------------------------------------
"""
__author__ = 'admin'

import xlsxwriter
import logging
import traceback
import configparser
try:
    from utils.MyDB import MysqlHelper
except Exception:

    from MyDB import MysqlHelper

import os
import html

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

currpath = os.path.dirname(os.path.realpath(__file__))

class OperateReport:
    def __init__(self, wd):
        self.wd = wd
        self.db = MysqlHelper()
        config = configparser.ConfigParser()
        config.read('{0}/../config/sscconfig.ini'.format(currpath), encoding='utf-8-sig')
        self._sonar_url = config.get('SONAR', 'SONAR_URL')

    def excgetissuename(self, issueid):
        sql = "SELECT ad.issuetypename from appscan_advisor ad where ad.ISSUETYPEID = '" + str(issueid) + "'"
        issueName = html.unescape(self.db.executeSql_one(sql)[0])
        return issueName

    def selectscanresult_by_distribute(self, distribute='ALL'):
        """

        :param distribute: 输入部门标识 ALL 标示所有部门 sz 深圳智慧医疗 sh 上海医疗 ZHYY 智慧医院
        :return:
        """

        if distribute == 'ALL':
            rptsql = "SELECT projectName as '项目',branch as '扫描分支',scanTime as '扫描时间',SUM(CASE WHEN severity in ('High','Critical') and status='0' THEN 1 ELSE 0 END ) as '漏洞',SUM(CASE WHEN severity in ('High','Critical') and status='2' THEN 1 ELSE 0 END ) as '忽略' FROM fortifyScandetail GROUP BY projectName,branch,scanTime"
        else:
            rptsql = "SELECT projectName as '项目',branch as '扫描分支',scanTime as '扫描时间',SUM(CASE WHEN severity in ('High','Critical') and status='0' THEN 1 ELSE 0 END ) as '漏洞',SUM(CASE WHEN severity in ('High','Critical') and status='2' THEN 1 ELSE 0 END ) as '忽略' FROM fortifyScandetail where projectName like '{0}-%' GROUP BY projectName,branch,scanTime".format(
                distribute)

        try:
            result = self.db.executeSql(rptsql)
            return result

        except Exception:
            logger.error('运行出错：{}'.format(traceback.print_exc()))
            return None

    def selectscanresult_by_project(self, project):
        """

        :param project: 项目名称
        :return:
        """
        selectsql = "SELECT category,SUM(case WHEN severity='Critical' and `status`='0' THEN 1 ELSE 0 END) as 'Critical'," \
                    "SUM(case WHEN severity='High' and `status`='0' THEN 1 ELSE 0 END) as 'High'," \
                    "SUM(case WHEN severity='Medium' and `status`='0' THEN 1 ELSE 0 END) as 'Medium' ," \
                    "SUM(case WHEN severity='LOW' and `status`='0' THEN 1 ELSE 0 END) as 'Low' ," \
                    "SUM(case WHEN `status`='2' THEN 1 ELSE 0 END) as 'suppressed' " \
                    "from fortifyScandetail where projectName='{0}'  GROUP BY category".format(project)

        try:
            result = self.db.executeSql(selectsql)
            return result

        except Exception:
            logger.error('运行出错：{}'.format(traceback.print_exc()))
            return None

    def selectscanresult_by_category(self, project, category):
        """

        :param project: 项目名称
        :return:
        """
        selectsql = "SELECT category, severity,kingdom,filename,function,line,abstract,explanation,recommendations,status from fortifyScandetail where projectName='{0}' and category='{1}' and status<>'1' GROUP BY category".format(
            project, category)

        try:
            result = self.db.executeSql(selectsql)
            return result

            # for row in result:
            #     result.append(row)
            #     print("项目名称:{0} 扫描分支:{1} 扫描时间:{2} 漏洞数量:{3}忽略:{4} \n".format(row[0],row[1],row[2],str(row[3]),str(row[4])))

        except Exception:
            logger.error('运行出错：{}'.format(traceback.print_exc()))
            return None

    def getReportStatics_by_distribute(self, distribute='ALL'):
        """

        :param distribute: 输入部门标识 ALL 标示所有部门 sz 深圳智慧医疗 sh 上海医疗 ZHYY 智慧医院
        :return:
        """
        statics_dict = dict()

        if distribute == 'ALL':
            rptsql = "SELECT projectName as '项目',branch as '扫描分支',scanTime as '扫描时间',SUM(CASE WHEN severity in ('High','Critical') and status='0' THEN 1 ELSE 0 END ) as '漏洞',SUM(CASE WHEN severity in ('High','Critical') and status='2' THEN 1 ELSE 0 END ) as '忽略' FROM fortifyScandetail GROUP BY projectName,branch,scanTime"
        else:
            rptsql = "SELECT projectName as '项目',branch as '扫描分支',scanTime as '扫描时间',SUM(CASE WHEN severity in ('High','Critical') and status='0' THEN 1 ELSE 0 END ) as '漏洞',SUM(CASE WHEN severity in ('High','Critical') and status='2' THEN 1 ELSE 0 END ) as '忽略' FROM fortifyScandetail where projectName like '{0}-%' GROUP BY projectName,branch,scanTime".format(
                distribute)

        try:
            projectsresult = self.db.executeSql(rptsql)
            for project in projectsresult:
                detailsql = "SELECT category, severity,kingdom,filename,function,line,abstract,explanation,recommendations,status FROM fortifyScandetail where projectName='{0}' and  `status`<>'1' and severity in ('Critical','High')".format(
                    project[0])
                detailresult = self.db.executeSql(detailsql)
                statics_dict[project] = detailresult
        except Exception:
            logger.error('运行出错：{}'.format(traceback.print_exc()))

        return statics_dict

    def excfortifytotal(self, projectname, level, number, zone):
        insertp = {'projectName': projectname, 'level': str(level), 'number': str(number), 'zone': zone}
        updatep = {'number': str(number)}
        cond_dict = {'projectName': projectname, 'level': str(level)}
        try:
            self.db.insert('fortifyResult', insertp)
        except Exception:
            self.db.update('fortifyResult', updatep, cond_dict)

    def excfortifydetail(self, projectname, bugtype, buglevel, bugnumber):

        insertp = {'projectName': projectname, 'bugLevel': str(buglevel), 'bugNumber': str(bugnumber),
                   'bugType': bugtype}
        updatep = {'bugNumber': str(bugnumber)}
        cond_dict = {'projectName': projectname, 'bugType': bugtype, 'bugLevel': str(buglevel)}
        try:
            self.db.insert('fortifyDetial', insertp)
        except Exception:
            self.db.update('fortifyDetial', updatep, cond_dict)

    def excSonar(self, projectname, level, number, zone):
        insertp = {'projectName': projectname, 'level': str(level), 'number': str(number), 'zone': zone}
        updatep = {'number': str(number)}
        cond_dict = {'projectName': projectname, 'level': str(level)}
        try:
            self.db.insert('sonarResult', insertp)
        except Exception:
            self.db.update('sonarResult', updatep, cond_dict)

    def monitor(self, parsereport):

        # workname = transcation[0:30]
        projectname = parsereport['projectname']
        branch = parsereport['branch']
        scantime = parsereport['scantime']
        info = parsereport['analysis']
        worksheet = self.wd.add_worksheet('Fortify安全扫描结果概要')

        worksheet.set_column("A:A", 50)
        worksheet.set_column("B:B", 12)
        worksheet.set_column("C:C", 12)
        worksheet.set_column("D:D", 12)
        worksheet.set_column("E:E", 12)
        worksheet.set_column("F:F", 12)

        for i in range(1, len(info.keys()) + 4):
            worksheet.set_row(i, 20)

        define_format_H1 = get_format(self.wd, {'bold': True, 'text_wrap': True, 'font_size': 18})
        define_format_H2 = get_format(self.wd, {'bold': True, 'font_size': 14})
        define_format_H3 = get_format(self.wd, {'bold': True, 'font_size': 12})

        define_format_H1.set_border(1)
        define_format_H2.set_border(1)
        define_format_H3.set_border(1)

        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H3.set_align("center")
        define_format_H1.set_bg_color("green")
        define_format_H2.set_bg_color("#C0C0C0")
        define_format_H3.set_bg_color("gray")
        define_format_H1.set_color("#ffffff")
        worksheet.merge_range('A1:F1', '{0} 项目 Fortify代码安全扫描概要'.format(projectname), define_format_H1)
        worksheet.merge_range('A2:A3', '缺陷类型', define_format_H2)
        worksheet.merge_range('B2:F2', '优先级', define_format_H3)
        _write_center_title(worksheet, "B3", 'Critical', self.wd, bgcolor='#FF0000')
        _write_center_title(worksheet, "C3", 'High', self.wd, bgcolor='#FF9900')
        _write_center_title(worksheet, "D3", 'Medium', self.wd, bgcolor='#FFCC00')
        _write_center_title(worksheet, "E3", 'Low', self.wd, bgcolor='#FFFF00')
        _write_center_title(worksheet, "F3", 'Suppress', self.wd, bgcolor='gray')

        temp = 4

        for isssue in sorted(info.keys()):
            isssuename = isssue.replace(':', '')[:28] + '_' + str(temp)
            issueSheet = self.wd.add_worksheet(isssuename)
            issueSheet.set_column("A:A", 30)
            issueSheet.set_column("B:B", 6)
            issueSheet.set_column("C:C", 8)
            issueSheet.set_column("D:D", 10)
            issueSheet.set_column("E:E", 50)
            issueSheet.set_column("F:F", 50)
            issueSheet.set_column("G:G", 50)
            issueSheet.set_column("H:H", 50)
            issueSheet.set_column("I:I", 16)
            issueSheet.set_column("J:J", 50)

            if 'Critical' not in info[isssue].keys():
                _write_center_title(worksheet, 'B' + str(temp), 0, self.wd)
            else:
                _write_center_title(worksheet, 'B' + str(temp), len(info[isssue]['Critical']),
                                    self.wd, bgcolor='#FF0000')
                self.excfortifydetail(projectname, isssue, 21, len(info[isssue]['Critical']))

            if 'High' not in info[isssue].keys():
                _write_center_title(worksheet, 'C' + str(temp), 0, self.wd)

            else:
                _write_center_title(worksheet, 'C' + str(temp), len(info[isssue]['High']),
                                    self.wd, bgcolor='#FF9900')
                self.excfortifydetail(projectname, isssue, 22, len(info[isssue]['High']))

            if 'Medium' not in info[isssue].keys():
                _write_center_title(worksheet, 'D' + str(temp), 0, self.wd)

            else:
                _write_center_title(worksheet, 'D' + str(temp), len(info[isssue]['Medium']),
                                    self.wd, bgcolor='#FFCC00')
                self.excfortifydetail(projectname, isssue, 23, len(info[isssue]['Medium']))

            if 'Low' not in info[isssue].keys():
                _write_center_title(worksheet, 'E' + str(temp), 0, self.wd)
            else:
                _write_center_title(worksheet, 'E' + str(temp), len(info[isssue]['Low']),
                                    self.wd, bgcolor='#FFFF00')
                self.excfortifydetail(projectname, isssue, 24, len(info[isssue]['Low']))

            if 'Suppress' not in info[isssue].keys():
                _write_center_title(worksheet, 'F' + str(temp), 0, self.wd)
            else:
                _write_center_title(worksheet, 'F' + str(temp), len(info[isssue]['Suppress']),
                                    self.wd, bgcolor='gray')
                self.excfortifydetail(projectname, isssue, 25, len(info[isssue]['Suppress']))

            issue_num = 2
            for priority in info[isssue].keys():
                issuedetails = info[isssue][priority]
                for i in range(1, len(issuedetails) + 1):
                    worksheet.set_row(i, 20)

                _write_center_title(issueSheet, "A1", '文件名称', self.wd, bgcolor='#FF9900')
                _write_center_title(issueSheet, "B1", '所在行', self.wd, bgcolor='#FF9900')
                _write_center_title(issueSheet, "C1", '优先级', self.wd, bgcolor='#FF9900')
                _write_center_title(issueSheet, "D1", '返回菜单页', self.wd, bgcolor='#FF9900')
                _write_center_title(issueSheet, "E1", '问题展示', self.wd, bgcolor='#FF9900')
                _write_center_title(issueSheet, "F1", '出现问题的详细原因', self.wd, bgcolor='#FF9900')
                _write_center_title(issueSheet, "G1", '推荐修改方法', self.wd, bgcolor='#FF9900')
                _write_center_title(issueSheet, "H1", '问题所在方法', self.wd, bgcolor='#FF9900')
                _write_center_title(issueSheet, "I1", '领域', self.wd, bgcolor='#FF9900')
                _write_center_title(issueSheet, "J1", '全文件路径', self.wd, bgcolor='#FF9900')
                _write_url_title(worksheet, 'A' + str(temp), "internal:'%s'!A1" % (isssuename), isssue, self.wd)
                for issuedetail in issuedetails:
                    _write_left_title(issueSheet, 'A' + str(issue_num), issuedetail['issueName'], self.wd)
                    _write_left_title(issueSheet, 'B' + str(issue_num), issuedetail['lineNumber'], self.wd)
                    _write_left_title(issueSheet, 'C' + str(issue_num), issuedetail['friority'], self.wd)
                    _write_url_title(issueSheet, 'D' + str(issue_num), "internal:'%s'!A%s" % ('Fortify安全扫描结果概要', temp),
                                     '返回', self.wd)

                    try:
                        _write_left_title(issueSheet, 'E' + str(issue_num), issuedetail['overview'], self.wd)
                    except KeyError:
                        _write_left_title(issueSheet, 'E' + str(issue_num), '同上', self.wd)
                    try:
                        _write_left_title(issueSheet, 'F' + str(issue_num), issuedetail['detail'], self.wd)
                    except KeyError:
                        _write_left_title(issueSheet, 'F' + str(issue_num), '同上', self.wd)
                    try:
                        _write_left_title(issueSheet, 'G' + str(issue_num), issuedetail['recommendation'], self.wd)
                    except KeyError:
                        _write_left_title(issueSheet, 'G' + str(issue_num), '同上', self.wd)

                    try:
                        _write_left_title(issueSheet, 'H' + str(issue_num), issuedetail['function'], self.wd)
                    except KeyError:
                        _write_left_title(issueSheet, 'H' + str(issue_num), '同上', self.wd)

                    _write_center_title(issueSheet, 'I' + str(issue_num), issuedetail['kingdom'], self.wd)
                    _write_left_title(issueSheet, 'J' + str(issue_num), issuedetail['fullFileName'], self.wd)

                    issue_num = issue_num + 1

            temp = temp + 1

        _write_left_title(worksheet, 'A' + str(temp), 'Total', self.wd, bgcolor='#DDDDDD')

        if len(info.keys()) == 0:
            _write_center_title(worksheet, 'B' + str(temp), 0, self.wd, bgcolor='#DDDDDD')
            _write_center_title(worksheet, 'C' + str(temp), 0, self.wd, bgcolor='#DDDDDD')
            _write_center_title(worksheet, 'D' + str(temp), 0, self.wd, bgcolor='#DDDDDD')
            _write_center_title(worksheet, 'E' + str(temp), 0, self.wd, bgcolor='#DDDDDD')
            _write_center_title(worksheet, 'F' + str(temp), 0, self.wd, bgcolor='#DDDDDD')



        else:

            _write_formula_title(worksheet, 'B' + str(temp), '=SUM(B4:B' + str(temp - 1) + ')', self.wd,
                                 bgcolor='#DDDDDD')
            _write_formula_title(worksheet, 'C' + str(temp), '=SUM(C4:C' + str(temp - 1) + ')', self.wd,
                                 bgcolor='#DDDDDD')
            _write_formula_title(worksheet, 'D' + str(temp), '=SUM(D4:D' + str(temp - 1) + ')', self.wd,
                                 bgcolor='#DDDDDD')
            _write_formula_title(worksheet, 'E' + str(temp), '=SUM(E4:E' + str(temp - 1) + ')', self.wd,
                                 bgcolor='#DDDDDD')
            _write_formula_title(worksheet, 'F' + str(temp), '=SUM(F4:F' + str(temp - 1) + ')', self.wd,
                                 bgcolor='#DDDDDD')

    def Sumarry_FortiFyReport_by_distribute(self,allInfo, distribute):

        worksheet = self.wd.add_worksheet('Fortify安全扫描结果汇总')
        worksheet.set_column("A:A", 30)  # 项目名称
        worksheet.set_column("B:B", 30)
        worksheet.set_column("C:C", 12)
        worksheet.set_column("D:D", 12)
        worksheet.set_column("E:E", 12)
        for i in (1, len(allInfo.keys()) + 2):
            worksheet.set_row(i, 20)

        define_format_H1 = get_format(self.wd, {'bold': True, 'font_size': 18})
        define_format_H2 = get_format(self.wd, {'bold': True, 'font_size': 14})
        define_format_H3 = get_format(self.wd, {'bold': True, 'font_size': 12})

        define_format_H1.set_border(1)
        define_format_H2.set_border(1)
        define_format_H3.set_border(1)

        define_format_H1.set_align("center")
        define_format_H2.set_align("left")
        define_format_H3.set_align("center")
        define_format_H1.set_bg_color("green")
        define_format_H3.set_bg_color("gray")

        temp = 3
        worksheet.merge_range('A1:E1', '各应用Fortify安全扫描结果统计', define_format_H1)

        _write_center_title(worksheet, "A2", '项目名称', self.wd, bgcolor='#C0C0C0')
        _write_center_title(worksheet, "B2", 'Critical', self.wd, bgcolor='#FF0000')
        _write_center_title(worksheet, "C2", 'High', self.wd, bgcolor='#FF9900')
        _write_center_title(worksheet, "D2", 'Medium', self.wd, bgcolor='#FFCC00')
        _write_center_title(worksheet, "E2", 'Low', self.wd, bgcolor='#FFFF00')

        for projectname in allInfo.keys():
            zone = projectname.split('-')[0]
            if zone not in ['sh', 'sz', 'bj']:
                zone = 'sh'
            info = allInfo[projectname]

            critical_count = 0
            High_count = 0
            Medium_count = 0
            Low_count = 0

            xlsxpath = 'Fortify_' + projectname + '.xlsx'

            _write_url_title(worksheet, 'A' + str(temp), r"external:%s" % (xlsxpath), projectname, self.wd)

            for isssue in sorted(info.keys()):

                if 'Critical' in info[isssue].keys():
                    critical_count = len(info[isssue]['Critical']) + critical_count
                else:
                    critical_count = critical_count + 0

                if 'High' in info[isssue].keys():
                    High_count = len(info[isssue]['High']) + High_count
                else:
                    High_count = 0 + High_count

                if 'Medium' in info[isssue].keys():
                    Medium_count = len(info[isssue]['Medium']) + Medium_count
                else:
                    Medium_count = 0 + Medium_count

                if 'Low' in info[isssue].keys():
                    Low_count = len(info[isssue]['Low']) + Low_count
                else:
                    Low_count = 0 + Low_count

            if len(info.keys()) == 0:
                _write_center_title(worksheet, 'B' + str(temp), 0, self.wd)
                _write_center_title(worksheet, 'C' + str(temp), 0, self.wd)
                _write_center_title(worksheet, 'D' + str(temp), 0, self.wd)
                _write_center_title(worksheet, 'E' + str(temp), 0, self.wd)


            else:

                if critical_count != 0:
                    _write_center_title(worksheet, 'B' + str(temp), critical_count, self.wd, bgcolor='#FF0000')

                else:
                    _write_center_title(worksheet, 'B' + str(temp), critical_count, self.wd)

                if High_count != 0:
                    _write_center_title(worksheet, 'C' + str(temp), High_count, self.wd, bgcolor='#FF9900')
                else:
                    _write_center_title(worksheet, 'C' + str(temp), High_count, self.wd)
                if Medium_count != 0:
                    _write_center_title(worksheet, 'D' + str(temp), Medium_count, self.wd, bgcolor='#FFCC00')
                else:
                    _write_center_title(worksheet, 'D' + str(temp), Medium_count, self.wd)
                if Low_count != 0:
                    _write_center_title(worksheet, 'E' + str(temp), Low_count, self.wd, bgcolor='#FFFF00')
                else:
                    _write_center_title(worksheet, 'E' + str(temp), Low_count, self.wd)

                self.excfortifytotal(projectname, 21, int(critical_count), zone)
                self.excfortifytotal(projectname, 22, int(High_count), zone)
                self.excfortifytotal(projectname, 23, int(Medium_count), zone)
                self.excfortifytotal(projectname, 24, int(Low_count), zone)

            temp = temp + 1

    def Sumarry_all_FortiFyReport(self, allInfo):

        worksheet = self.wd.add_worksheet('Fortify安全扫描结果汇总')
        worksheet.set_column("A:A", 30)
        worksheet.set_column("B:B", 12)
        worksheet.set_column("C:C", 12)
        worksheet.set_column("D:D", 12)
        worksheet.set_column("E:E", 12)
        for i in (1, len(allInfo.keys()) + 2):
            worksheet.set_row(i, 20)
        define_format_H1 = get_format(self.wd, {'bold': True, 'font_size': 18})
        define_format_H2 = get_format(self.wd, {'bold': True, 'font_size': 14})
        define_format_H3 = get_format(self.wd, {'bold': True, 'font_size': 12})

        define_format_H1.set_border(1)
        define_format_H2.set_border(1)
        define_format_H3.set_border(1)

        define_format_H1.set_align("center")
        define_format_H2.set_align("left")
        define_format_H3.set_align("center")
        define_format_H1.set_bg_color("green")
        define_format_H3.set_bg_color("gray")

        temp = 3
        worksheet.merge_range('A1:E1', '各应用Fortify安全扫描结果统计', define_format_H1)

        _write_center_title(worksheet, "A2", '项目名称', self.wd, bgcolor='#C0C0C0')
        _write_center_title(worksheet, "B2", 'Critical', self.wd, bgcolor='#FF0000')
        _write_center_title(worksheet, "C2", 'High', self.wd, bgcolor='#FF9900')
        _write_center_title(worksheet, "D2", 'Medium', self.wd, bgcolor='#FFCC00')
        _write_center_title(worksheet, "E2", 'Low', self.wd, bgcolor='#FFFF00')

        for projectname in allInfo.keys():
            zone = projectname.split('-')[0]
            if zone not in ['sh', 'sz', 'bj']:
                zone = 'sh'
            info = allInfo[projectname]

            critical_count = 0
            High_count = 0
            Medium_count = 0
            Low_count = 0

            xlsxpath = 'Fortify_' + projectname + '.xlsx'

            _write_url_title(worksheet, 'A' + str(temp), r"external:%s" % (xlsxpath), projectname, self.wd)

            # _write_center_title(worksheet, 'A' + str(temp),projectname , self.wd)

            for isssue in sorted(info.keys()):

                if 'Critical' in info[isssue].keys():
                    critical_count = len(info[isssue]['Critical']) + critical_count
                else:
                    critical_count = critical_count + 0

                if 'High' in info[isssue].keys():
                    High_count = len(info[isssue]['High']) + High_count
                else:
                    High_count = 0 + High_count

                if 'Medium' in info[isssue].keys():
                    Medium_count = len(info[isssue]['Medium']) + Medium_count
                else:
                    Medium_count = 0 + Medium_count

                if 'Low' in info[isssue].keys():
                    Low_count = len(info[isssue]['Low']) + Low_count
                else:
                    Low_count = 0 + Low_count

            if len(info.keys()) == 0:
                _write_center_title(worksheet, 'B' + str(temp), 0, self.wd)
                _write_center_title(worksheet, 'C' + str(temp), 0, self.wd)
                _write_center_title(worksheet, 'D' + str(temp), 0, self.wd)
                _write_center_title(worksheet, 'E' + str(temp), 0, self.wd)


            else:

                if critical_count != 0:
                    _write_center_title(worksheet, 'B' + str(temp), critical_count, self.wd, bgcolor='#FF0000')

                else:
                    _write_center_title(worksheet, 'B' + str(temp), critical_count, self.wd)

                if High_count != 0:
                    _write_center_title(worksheet, 'C' + str(temp), High_count, self.wd, bgcolor='#FF9900')
                else:
                    _write_center_title(worksheet, 'C' + str(temp), High_count, self.wd)
                if Medium_count != 0:
                    _write_center_title(worksheet, 'D' + str(temp), Medium_count, self.wd, bgcolor='#FFCC00')
                else:
                    _write_center_title(worksheet, 'D' + str(temp), Medium_count, self.wd)
                if Low_count != 0:
                    _write_center_title(worksheet, 'E' + str(temp), Low_count, self.wd, bgcolor='#FFFF00')
                else:
                    _write_center_title(worksheet, 'E' + str(temp), Low_count, self.wd)

                self.excfortifytotal(projectname, 21, int(critical_count), zone)
                self.excfortifytotal(projectname, 22, int(High_count), zone)
                self.excfortifytotal(projectname, 23, int(Medium_count), zone)
                self.excfortifytotal(projectname, 24, int(Low_count), zone)

            temp = temp + 1

    def SonarReport(self, sonarinfo, dist='OP'):

        if dist.upper() != 'ALL':
            dist = '{0} '.format(dist.upper())
        else:
            dist = '全公司'
        worksheet = self.wd.add_worksheet('{0}Sonar扫描结果汇总'.format(dist))
        worksheet.set_column("A:A", 30)
        worksheet.set_column("B:B", 10)
        worksheet.set_column("C:C", 10)
        worksheet.set_column("D:D", 10)
        worksheet.set_column("E:E", 10)
        worksheet.set_column("F:F", 10)
        worksheet.set_column("G:G", 10)
        worksheet.set_column("H:H", 10)
        worksheet.set_column("I:I", 10)

        for i in (1, len(sonarinfo.keys()) + 2):
            worksheet.set_row(i, 20)

        define_format_H1 = get_format(self.wd, {'bold': True, 'font_size': 20})
        define_format_H2 = get_format(self.wd,
                                      {'align': 'left', 'text_wrap': 1, 'bold': 1, 'font_size': 14, 'bg_color': 'gray',
                                       'border': 1})
        define_format_H3 = get_format(self.wd, {'bold': True, 'font_size': 14})

        define_format_H1.set_border(1)
        define_format_H3.set_border(1)
        define_format_H1.set_align("center")
        define_format_H3.set_align("center")
        define_format_H1.set_bg_color("green")
        define_format_H3.set_bg_color("gray")

        worksheet.merge_range('A1:I1', '{0}各应用Sonar扫描结果统计'.format(dist), define_format_H1)

        _write_center_title(worksheet, "A2", '应用名称', self.wd, bgcolor='#C0C0C0')
        _write_center_title(worksheet, "B2", '缺陷', self.wd, bgcolor='#FF0000')
        _write_center_title(worksheet, "C2", '漏洞', self.wd, bgcolor='#FF9900')
        _write_center_title(worksheet, "D2", '坏味道', self.wd, bgcolor='#FFCC00')
        _write_center_title(worksheet, "E2", '行覆盖率', self.wd, bgcolor='#C0C0C0')
        _write_center_title(worksheet, "F2", '条件覆盖率', self.wd, bgcolor='#C0C0C0')
        _write_center_title(worksheet, "G2", '行重复率', self.wd, bgcolor='#C0C0C0')
        _write_center_title(worksheet, "H2", '复杂度', self.wd, bgcolor='#C0C0C0')
        _write_center_title(worksheet, "I2", '传送门', self.wd, bgcolor='#C0C0C0')
        temp = 3

        for appliacation in sorted(sonarinfo.keys()):
            url = self._sonar_url + appliacation
            zone = appliacation.split('-')[0]
            try:
                bugs = sonarinfo[appliacation]['bugs']
            except KeyError:
                bugs = 0
            try:
                vulnerabilities = sonarinfo[appliacation]['vulnerabilities']
            except KeyError:
                vulnerabilities = '0'

            try:

                code_smells = sonarinfo[appliacation]['code_smells']
            except KeyError:
                code_smells = '0'
            try:
                coverage = str(sonarinfo[appliacation]['coverage'])
            except KeyError:
                coverage = '0'
            try:
                duplicated_lines_density = str(sonarinfo[appliacation]['duplicated_lines_density'])
            except KeyError:
                duplicated_lines_density = '0'
            try:
                line_coverage = str(sonarinfo[appliacation]['line_coverage'])
            except KeyError:
                line_coverage = '0'
            try:
                branch_coverage = str(sonarinfo[appliacation]['branch_coverage'])
            except KeyError:
                branch_coverage = '0'
            try:
                complexity = str(sonarinfo[appliacation]['complexity'])
            except KeyError:
                complexity = '0'
            # if dist =='all':

            if bugs == '0':
                _write_center_title(worksheet, 'B' + str(temp), bugs, self.wd)

            else:
                _write_center_title(worksheet, 'B' + str(temp), bugs, self.wd, bgcolor='#FF0000')

            if vulnerabilities == '0':
                _write_center_title(worksheet, 'C' + str(temp), vulnerabilities, self.wd)

            else:
                _write_center_title(worksheet, 'C' + str(temp), vulnerabilities, self.wd, bgcolor='#FF9900')
            if code_smells == '0':
                _write_center_title(worksheet, 'D' + str(temp), code_smells, self.wd)

            else:
                _write_center_title(worksheet, 'D' + str(temp), code_smells, self.wd, bgcolor='#FFCC00')

            if int(bugs) + int(vulnerabilities) > 0:
                _write_left_title(worksheet, 'A' + str(temp), appliacation, self.wd, bgcolor='#FFCC00')

            else:
                _write_left_title(worksheet, 'A' + str(temp), appliacation, self.wd)

            _write_center_title(worksheet, 'E' + str(temp), line_coverage + '%', self.wd)
            _write_center_title(worksheet, 'F' + str(temp), branch_coverage + '%', self.wd)
            _write_center_title(worksheet, 'G' + str(temp), duplicated_lines_density + '%', self.wd)
            _write_center_title(worksheet, 'H' + str(temp), complexity, self.wd)
            _write_url_title(worksheet, 'I' + str(temp), url, '传送', self.wd)

            self.excSonar(appliacation, 1, bugs, zone)
            self.excSonar(appliacation, 2, vulnerabilities, zone)
            self.excSonar(appliacation, 3, code_smells, zone)
            self.excSonar(appliacation, 4, coverage, zone)
            self.excSonar(appliacation, 5, duplicated_lines_density, zone)
            self.excSonar(appliacation, 6, line_coverage, zone)
            self.excSonar(appliacation, 7, branch_coverage, zone)
            self.excSonar(appliacation, 8, complexity, zone)

            temp = temp + 1
        worksheet.merge_range('A' + str(temp) + ':I' + str(temp + 3),
                              '说明：\nsonar 扫描已经添加了阿里开发编程规范的53条规则，命中这些规则的问题都属于坏味道，相比之前会增加更多的坏味道', define_format_H2)

    def close(self):
        self.wd.close()


def get_format(wd, option={}):
    return wd.add_format(option)


# 设置居中
def get_format_center(wd, num=1):
    return wd.add_format({'align': 'center', 'valign': 'vcenter', 'border': num})


# 设置边框
def set_border_(wd, num=1):
    return wd.add_format({}).set_border(num)


# 设置背景颜色
##FF8C00 橙色   green #008000 gray #808080 gold #FFD700 GreenYellow #ADFF2F
def get_format_bg_color(wd, bgcolor='#ffffff', num=1):
    return wd.add_format({'align': 'center', 'valign': 'top', 'border': num, 'bg_color': bgcolor, 'text_wrap': True})


def get_format_bg_left_color(wd, bgcolor='#ffffff', num=1):
    return wd.add_format({'align': 'left', 'valign': 'vcenter', 'border': num, 'bg_color': bgcolor, 'text_wrap': True})


# 写数据
def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))


def _write_center_title(worksheet, cl, data, wd, bgcolor='#FFFFF0'):
    return worksheet.write(cl, data, get_format_bg_color(wd, bgcolor))


def _write_left_title(worksheet, cl, data, wd, bgcolor='#FFFFF0'):
    return worksheet.write(cl, data, get_format_bg_left_color(wd, bgcolor))


def _write_url_title(worksheet, cl, url, string_name, wd, bgcolor='#CCCC99'):
    return worksheet.write_url(cl, url, get_format_bg_left_color(wd, bgcolor), string_name)


#    def write_formula(self, row, col, formula, cell_format=None, value=0):

def _write_formula_title(worksheet, cl, formula, wd, bgcolor='#CCCC99'):
    return worksheet.write_formula(cl, formula, get_format_bg_color(wd, bgcolor))


def set_row(worksheet, num, height):
    worksheet.set_row(num, height)


if __name__ == '__main__':
    workbook = xlsxwriter.Workbook('report.xlsx')
    wd = OperateReport(workbook)

    wd.close()
