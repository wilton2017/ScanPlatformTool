# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ReoirtWriter
   Description :
   Author :       admin
   date：          2020/1/5
-------------------------------------------------
   Change Activity:
                   2020/1/5:
-------------------------------------------------
"""
__author__ = 'admin'

import logging
import html
import sys
from utils.MyDB import MysqlHelper

import traceback

try:
    from xlsxwriter.workbook import Workbook
except ImportError:
    print("You should install xlsxwriter library, before using this script.")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

column_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

col_names = ['漏洞级别', '文件路径', '方法', '行号', '问题展示', '问题详细原因', '推荐修改方法', '漏洞类型', '所属领域', "误报"]
col_index = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J']


def get_format_bg_left_color(wd, bgcolor='#ffffff', num=1):
    return wd.add_format(
        {'align': 'left', 'valign': 'vcenter', 'border': num, 'bg_color': bgcolor, 'text_wrap': True})


def write_url_title(worksheet, cl, url, string_name, wd, bgcolor='#CCCC99'):
    return worksheet.write_url(cl, url, get_format_bg_left_color(wd, bgcolor), string_name)


class ReportWriter:

    def __init__(self):
        self.db = MysqlHelper()

    def writeWorksheet(self, project, name):

        fs = self.orderFindings(project, name)
        if len(fs) > 0:
            worksheet = self._workbook.add_worksheet(name)
            self.add_first_column_names(worksheet, col_names)  # 第一行是标题
            self.set_width_of_columns(worksheet, fs)
            cell_formats = [self._low_cell_format, self._medium_cell_format, self._high_cell_format,
                            self._critical_cell_format]
            worksheet.set_row(0, 20)
            i = 2  # 从第二行起开始写入数据
            for finding in fs:
                if finding[0].lower() == 'critical':
                    severity_cell_format = cell_formats[3]
                elif finding[0].lower() == 'high':
                    severity_cell_format = cell_formats[2]
                elif finding[0].lower() == 'medium':
                    severity_cell_format = cell_formats[1]
                elif finding[0].lower() == 'low':
                    severity_cell_format = cell_formats[0]

                data = [finding[0].upper(), finding[1], finding[2], html.unescape(finding[4]),
                        html.unescape(finding[5]), html.unescape(finding[6]), finding[7], finding[8]]
                formats = [severity_cell_format, None, None, None, None, None, None, None]
                for x, y, z in zip(col_index, data, formats):
                    z = self._str_cell_format if z is None else z
                    worksheet.write(x + str(i), y, z)

                worksheet.write("D" + str(i), finding[3], self._str_cell_format)
                if finding[9] == '2':
                    worksheet.write("J" + str(i), 'True', self._str_cell_format)
                else:
                    worksheet.write("J" + str(i), 'False', self._str_cell_format)

                i = i + 1
            worksheet.autofilter('A1:J' + str(len(fs)))

    def writeStaticsIssuedetail(self, fs, name):

        if len(fs) > 0:
            worksheet = self._workbook.add_worksheet(name)
            self.add_first_column_names(worksheet, col_names)  # 第一行是标题
            self.set_width_of_columns(worksheet, fs)
            cell_formats = [self._low_cell_format, self._medium_cell_format, self._high_cell_format,
                            self._critical_cell_format]
            worksheet.set_row(0, 20)
            i = 2  # 从第二行起开始写入数据
            for finding in fs:
                if finding[0].lower() == 'critical':
                    severity_cell_format = cell_formats[3]
                elif finding[0].lower() == 'high':
                    severity_cell_format = cell_formats[2]
                elif finding[0].lower() == 'medium':
                    severity_cell_format = cell_formats[1]
                elif finding[0].lower() == 'low':
                    severity_cell_format = cell_formats[0]

                data = [finding[0].upper(), finding[1], finding[2], html.unescape(finding[4]),
                        html.unescape(finding[5]), html.unescape(finding[6]), finding[7], finding[8]]
                formats = [severity_cell_format, None, None, None, None, None, None, None]
                for x, y, z in zip(col_index, data, formats):
                    z = self._str_cell_format if z is None else z
                    worksheet.write(x + str(i), y, z)
                worksheet.write("D" + str(i), finding[3], self._str_cell_format)
                if finding[9] == '2':
                    worksheet.write("J" + str(i), 'True', self._str_cell_format)
                else:
                    worksheet.write("J" + str(i), 'False', self._str_cell_format)

                i = i + 1
            worksheet.autofilter('A1:J' + str(len(fs)))

    def _init_xlsx(self, filename):
        """
        :param filename:
        :return:
        """
        self._workbook = Workbook(filename)
        self._merge_title_format = self.generate_cell_format(bgcolor='009966', font_size=16)  # 汇总统计页面的标题格式
        self._merge_cell_format = self.generate_cell_format(bgcolor='#78C4EB', font_size=14)  # 其他有合并的单元格格式
        self._merge_white_format = self.generate_cell_format(bgcolor='yellow', font_size=14,
                                                             align='left')  # 白名单有合并的单元格格式
        self._critical_cell_format = self.generate_cell_format(bgcolor='#FF0000')  # critical 单元格格式
        self._high_cell_format = self.generate_cell_format(bgcolor='#FF9900')  # high 单元格格式
        self._medium_cell_format = self.generate_cell_format(bgcolor='#FFCC00')  # medium 单元格格式
        self._low_cell_format = self.generate_cell_format(bgcolor='gray')  # low 单元格格式
        self._suppress_cell_format = self.generate_cell_format(bgcolor='#FFFF00')  # suppress 单元格格式
        self._number_cell_format = self.generate_cell_format(align='center')  # 数字的单元格格式
        self._str_cell_format = self.generate_cell_format(align='left')  # 字符串的单元格格式
        self._sum_str_cell_format = self.generate_cell_format(align='left', bgcolor='#CCCC99', font_size=14)
        self._sum_num_cell_format = self.generate_cell_format(bold=True, align='center', bgcolor='#CCCC99',
                                                              font_size=14)

    def writeToExcel(self, project, filename):
        """
        :param project:
        :param filename:
        :return:
        """
        self._init_xlsx(filename)
        self.write_summary_sheet(project)
        self.writeWorksheet(project, 'critical')
        self.writeWorksheet(project, 'high')
        self.writeWorksheet(project, 'medium')
        self.writeWorksheet(project, 'low')
        self.writeWorksheet(project, 'WhileList')
        self._workbook.close()

    def addColumnNames(self, worksheet, colNames, cell_format):

        for i in range(0, len(colNames)):
            worksheet.write(chr(ord('A') + i) + '1', colNames[i], cell_format)

    def generate_cell_format(self, bold=False, fgcolor='black', bgcolor='white', align='center', valign='top',
                             font_size=12, border=1):
        cell_format = self._workbook.add_format()
        cell_format.set_border(border)
        cell_format.set_bold(bold)
        cell_format.set_font_color(fgcolor)
        cell_format.set_bg_color(bgcolor)
        cell_format.set_align(align)  # 水平
        cell_format.set_valign(valign)  # 垂直
        cell_format.set_font_size(font_size)
        cell_format.set_text_wrap()
        return cell_format

    def generateCellFormat(self, workbook, bold=False, fgcolor='black', bgcolor='white'):
        """
        :param workbook:
        :param bold:
        :param fgcolor:
        :param bgcolor:
        :return:
        """

        cell_format = workbook.add_format({'border': 1, })
        if bold:
            cell_format.set_bold()
        cell_format.set_font_color(fgcolor)
        cell_format.set_text_wrap()
        cell_format.set_bg_color(bgcolor)
        return cell_format

    def write_summary_sheet(self, project):
        """
        :param project:
        :return:
        """
        fs = self._summary_handler(project)
        worksheet = self._workbook.add_worksheet("summary")
        worksheet.set_row(0, 25)
        worksheet.set_row(1, 20)
        worksheet.set_row(2, 20)
        max_len = max([len(row[0]) for row in fs]) + 1
        worksheet.set_column('A:A', max_len)
        worksheet.merge_range("A1:E1", "{0}安全扫描结果概要".format(project), self._merge_title_format)
        worksheet.merge_range("A2:A3", "缺陷类型", self._merge_cell_format)
        worksheet.merge_range("B2:E2", "缺陷等级", self._merge_cell_format)
        worksheet.write("B3", "严重", self._critical_cell_format)
        worksheet.write("C3", "高", self._high_cell_format)
        worksheet.write("D3", "中", self._medium_cell_format)
        worksheet.write("E3", "低", self._low_cell_format)
        index = 4
        for finding in fs:
            if int(finding[5]) > 0:
                continue
            else:
                worksheet.write("A" + str(index), finding[0], self._str_cell_format)

                data = [finding[1], finding[2], finding[3], finding[4]]
                if int(finding[1]) > 0:
                    formats = [self._critical_cell_format, self._number_cell_format, self._number_cell_format,
                               self._number_cell_format]
                elif int(finding[2]) > 0:
                    formats = [self._number_cell_format, self._high_cell_format, self._number_cell_format,
                               self._number_cell_format]
                elif int(finding[3]) > 0:
                    formats = [self._number_cell_format, self._number_cell_format, self._medium_cell_format,
                               self._number_cell_format]
                elif int(finding[4]) > 0:
                    formats = [self._number_cell_format, self._number_cell_format, self._number_cell_format,
                               self._low_cell_format]
                else:
                    formats = [self._number_cell_format, self._number_cell_format, self._number_cell_format,
                               self._low_cell_format]

                [worksheet.write_number(x + str(index), y, z) for x, y, z in zip(['B', 'C', 'D', 'E'], data, formats)]
                index = index + 1
        white_list_number = sum([int(x[5]) for x in fs])
        # 增加汇总信息
        self._make_summary(worksheet, index)
        self._make_white_list_info(worksheet, white_list_number, index + 1)

    def _writesummarysheet(self, project):
        """
        写汇总报表
        :param project:
        :return:
        """
        fs = self._summary_handler(project)
        worksheet = self._workbook.add_worksheet(project)
        worksheet.set_row(0, 25)
        worksheet.set_row(1, 20)
        worksheet.set_row(2, 20)
        max_len = max([len(row[0]) for row in fs]) + 1
        worksheet.set_column('A:A', max_len)
        worksheet.merge_range("A1:E1", "{0}安全扫描结果概要".format(project), self._merge_title_format)
        worksheet.merge_range("A2:A3", "缺陷类型", self._merge_cell_format)
        worksheet.merge_range("B2:E2", "缺陷等级", self._merge_cell_format)
        worksheet.write("B3", "严重", self._critical_cell_format)
        worksheet.write("C3", "高", self._high_cell_format)
        worksheet.write("D3", "中", self._medium_cell_format)
        worksheet.write("E3", "低", self._low_cell_format)
        index = 4
        for finding in fs:

            if int(finding[5]) > 0:
                continue
            else:
                worksheet.write("A" + str(index), finding[0], self._str_cell_format)

                data = [finding[1], finding[2], finding[3], finding[4]]
                if int(finding[1]) > 0:
                    formats = [self._critical_cell_format, self._number_cell_format, self._number_cell_format,
                               self._number_cell_format]
                elif int(finding[2]) > 0:
                    formats = [self._number_cell_format, self._high_cell_format, self._number_cell_format,
                               self._number_cell_format]
                elif int(finding[3]) > 0:
                    formats = [self._number_cell_format, self._number_cell_format, self._medium_cell_format,
                               self._number_cell_format]
                elif int(finding[4]) > 0:
                    formats = [self._number_cell_format, self._number_cell_format, self._number_cell_format,
                               self._low_cell_format]
                else:
                    formats = [self._number_cell_format, self._number_cell_format, self._number_cell_format,
                               self._low_cell_format]

                [worksheet.write_number(x + str(index), y, z) for x, y, z in zip(['B', 'C', 'D', 'E'], data, formats)]
                index = index + 1
        white_list_number = sum([int(x[5]) for x in fs])
        # 增加汇总信息
        self._make_summary(worksheet, index)
        self._make_white_list_info(worksheet, white_list_number, index + 1)

    def _make_white_list_info(self, worksheet, white_list_number, row_num):
        """
        处理白名单的命中的漏洞
        :param worksheet:
        :param white_list_number:
        :param row_num:
        :return:
        """
        if white_list_number > 0:
            info = "共有 %s 条扫描结果列入白名单中，未标记为缺陷，详情见 WhiteList 页." % str(white_list_number)
            worksheet.set_row(row_num - 1, 30)
            worksheet.merge_range("A{0}:E{1}".format(row_num, row_num + 1), info, self._merge_white_format)

    def write_stattics_sheet(self, distribute, filename):
        """

        :param distribute:
        :param filename:
        :return:
        """
        self._init_xlsx(filename)
        # fs = self.selectscanresult_by_distribute(distribute)

        fs = self.getReportStatics_by_distribute(distribute)
        worksheet = self._workbook.add_worksheet("Fortify安全扫描结果汇总")
        worksheet.set_row(0, 25)
        worksheet.set_row(1, 20)
        try:
            max_len = max([len(row[0]) for row in fs]) + 1
            max_branch_len = max([len(row[1]) for row in fs]) + 1
        except ValueError:
            logger.error('没有返回结果数据，请检查{0}下是否存在扫描项目！'.format(distribute))
            sys.exit(1)
        worksheet.set_column('A:A', max_len)
        worksheet.set_column('B:B', max(max_branch_len, 10))
        worksheet.set_column('C:C', 20)
        if distribute == 'ALL':
            region = '全公司'
        else:
            region = distribute.upper()

        worksheet.merge_range("A1:E1", "{0}各应用Fortify安全扫描结果统计".format(region), self._merge_title_format)
        # worksheet.merge_range("A1:E1", "各项目Fortify安全扫描结果统计", self._merge_title_format)
        worksheet.write("A2", "项目名称", self._suppress_cell_format)
        worksheet.write("B2", "扫描分支", self._suppress_cell_format)
        worksheet.write("C2", "扫描时间", self._suppress_cell_format)
        worksheet.write("D2", "漏洞数量", self._suppress_cell_format)
        worksheet.write("E2", "忽略数量", self._suppress_cell_format)
        index = 3
        for finding in fs:
            worksheet.write("A" + str(index), finding[0], self._str_cell_format)
            worksheet.write("B" + str(index), finding[1], self._str_cell_format)
            worksheet.write("C" + str(index), finding[2], self._str_cell_format)
            worksheet.write("D" + str(index), finding[3], self._number_cell_format)
            worksheet.write("E" + str(index), finding[4], self._number_cell_format)
            self._writesummarysheet(finding[0][0:31])
            write_url_title(worksheet, "A" + str(index), "internal:'%s'!A1" % (finding[0][:31]), finding[0],
                            self._workbook)

            index = index + 1
        self._workbook.close()

    def writesumarrysheet(self, distribute, filename):
        """

        :param distribute: 部门缩写
        :param filename: 生成Excel文件名称
        :return:
        """
        self._init_xlsx(filename)
        fs = self.getReportStatics_by_distribute(distribute)
        worksheet = self._workbook.add_worksheet("Fortify安全扫描结果汇总")
        worksheet.set_row(0, 25)
        worksheet.set_row(1, 20)
        try:
            max_len = max([len(row[0]) for row in fs]) + 1
            max_branch_len = max([len(row[1]) for row in fs]) + 1
        except ValueError:
            logger.error('没有返回结果数据，请检查{0}下是否存在扫描项目！'.format(distribute))
            sys.exit(1)
        worksheet.set_column('A:A', max_len)
        worksheet.set_column('B:B', max(max_branch_len, 10))
        worksheet.set_column('C:C', 20)
        if distribute.upper() == 'ALL':
            region = '全公司'
        else:
            region = distribute.upper()

        worksheet.merge_range("A1:F1", "{0}各应用Fortify安全扫描结果统计".format(region), self._merge_title_format)
        worksheet.write("A2", "项目名称", self._suppress_cell_format)
        worksheet.write("B2", "扫描分支", self._suppress_cell_format)
        worksheet.write("C2", "扫描时间", self._suppress_cell_format)
        worksheet.write("D2", "扫描次数", self._suppress_cell_format)
        worksheet.write("E2", "漏洞数量", self._suppress_cell_format)
        worksheet.write("F2", "忽略数量", self._suppress_cell_format)
        index = 3
        for finding, value in fs.items():
            # worksheet.write("A"+str(index),finding[0],self._str_cell_format)
            worksheet.write("B" + str(index), finding[1], self._str_cell_format)
            worksheet.write("C" + str(index), finding[2], self._str_cell_format)
            worksheet.write("D" + str(index), finding[6], self._number_cell_format)
            worksheet.write("E" + str(index), finding[3], self._number_cell_format)
            worksheet.write("F" + str(index), finding[4], self._number_cell_format)
            self.writeStaticsIssuedetail(value, finding[0][:31])
            write_url_title(worksheet, "A" + str(index), "internal:'%s'!A1" % (finding[0][:31]), finding[0],
                            self._workbook)

            index = index + 1
        self._workbook.close()

    def _make_summary(self, worksheet, index):
        """

        :param worksheet:
        :param index:
        :return:
        """
        worksheet.set_row(index - 1, 20)
        worksheet.write('A' + str(index), 'Summary', self._sum_str_cell_format)
        for row in ['B', 'C', 'D', 'E']:
            formula = '=sum(%s:%s)' % (row + str(4), row + str(index - 1))
            worksheet.write_formula(row + str(index), formula, self._sum_num_cell_format)

    @staticmethod
    def set_width_of_columns(worksheet, fs):
        """

        :param worksheet:
        :param fs:
        :return:
        """
        severity_len = line_len = 10
        filename_len = len('文件路径')
        function_len = len('方法')
        abstract_len = explanation_len = recommendations_len = 50
        category_len = len("漏洞类型") + 3
        kingdom_len = len("所属领域")
        for f in fs:
            filename_len = max(filename_len, len(f[1]))
            function_len = max(function_len, len(f[2]))
            category_len = max(category_len, len(f[7]))
            kingdom_len = max(kingdom_len, len(f[8]))
        col_index.append('D')
        lens = [severity_len, filename_len, function_len, abstract_len, explanation_len, recommendations_len,
                category_len, kingdom_len, line_len]
        [worksheet.set_column(x + ':' + x, y) for x, y in zip(col_index, lens)]

    def add_first_column_names(self, worksheet, col_names):
        cell_format = self.generate_cell_format(True, 'white', 'blue')
        for i in range(0, len(col_names)):
            worksheet.write(chr(ord('A') + i) + '1', col_names[i], cell_format)

    def orderFindings(self, project, severity):

        # col_names = ['漏洞级别', '文件路径', '方法', '行号', '问题展示', '问题详细原因', '推荐修改方法', '漏洞类型', '所属领域']

        job_info_id = self.db.get_job_id(project)
        if severity == 'WhileList':
            fssql = "SELECT severity,filename,`function`,line,abstract,explanation,recommendation,category,kingdom,status from fortify_scan_result where job_info_id='{0}' and status = '2' order by category".format(
                job_info_id)
        elif severity == 'critical':
            fssql = "SELECT severity,filename,`function`,line,abstract,explanation,recommendation,category,kingdom,status from fortify_scan_result where job_info_id='{0}' and severity='Critical' and status<>'1' order BY category".format(
                job_info_id)
        elif severity == 'high':
            fssql = "SELECT severity,filename,`function`,line,abstract,explanation,recommendation,category,kingdom,status from fortify_scan_result where job_info_id='{0}' and severity='High' and status<>'1' order BY category".format(
                job_info_id)
        elif severity == 'medium':
            fssql = "SELECT severity,filename,`function`,line,abstract,explanation,recommendation,category,kingdom,status from fortify_scan_result where job_info_id='{0}' and severity='Medium' and status<>'1' order BY category".format(
                job_info_id)
        elif severity == 'low':
            fssql = "SELECT severity,filename,`function`,line,abstract,explanation,recommendation,category,kingdom,status from fortify_scan_result where job_info_id='{0}' and severity='Low' and status<>'1' order BY category".format(
                job_info_id)
        else:
            fssql = "SELECT severity,filename,`function`,line,abstract,explanation,recommendation,category,kingdom ,status from fortify_scan_result where job_info_id='{0}' and status<>'1' order BY category".format(
                job_info_id)

        fs = self.db.executeSql(fssql)
        return fs

    def _summary_handler(self, project):
        """

        :param project: 项目名称
        :return:
        """

        # 首先通过项目名，获取job_info_id
        job_info_id = self.db.get_job_id(project)

        selectsql = "SELECT category,SUM(case WHEN severity='Critical' and `status`='0' THEN 1 ELSE 0 END) as 'Critical'," \
                    "SUM(case WHEN severity='High' and `status`='0' THEN 1 ELSE 0 END) as 'High'," \
                    "SUM(case WHEN severity='Medium' and `status`='0' THEN 1 ELSE 0 END) as 'Medium' ," \
                    "SUM(case WHEN severity='Low' and `status`='0' THEN 1 ELSE 0 END) as 'Low' ," \
                    "SUM(case WHEN `status`='2' THEN 1 ELSE 0 END) as 'suppressed' " \
                    "from fortify_scan_result where job_info_id='{0}'  GROUP BY category ORDER BY category".format(
            job_info_id)

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
        # 首先通过项目名，获取job_info_id
        job_info_id = self.db.get_job_id(project)
        selectsql = "select category, severity, kingdom, filename, function, line, abstract, explanation, recommendation, status from fortify_scan_result where job_info_id= '{0}' and category='{1}' and status<>'1' GROUP BY category".format(
            job_info_id, category)

        try:
            result = self.db.executeSql(selectsql)
            return result

        except Exception:
            logger.error('运行出错：{}'.format(traceback.print_exc()))
            return None

    def getReportStatics_by_distribute(self, distribute='ALL'):
        """

        :param distribute: 输入部门标识 ALL  所有部门 OP  OP项目组  OT OT 项目组 CB CB项目
        :return:
        """
        statics_dict = dict()

        if distribute == 'ALL':
            rptsql = "select project_name , branch_name ,scanTime ,SUM(CASE WHEN severity in ('High','Critical') and status='0' THEN 1 ELSE 0 END ) as 'ld',SUM(CASE WHEN severity in ('High','Critical') " \
                     "and status='2' THEN 1 ELSE 0 END ) as 'hl', s.job_info_id,job_num from (select j.id as job_info_id, p.project_name as project_name ,j.branch_name as branch_name,j.scanTime as scanTime" \
                     ", p.region as region ,j.job_num as job_num from fortify_job_info j ,fortify_project_info p where j.project_id = p.id and p.status='0' and j.status='1') jp " \
                     ",fortify_scan_result s where jp.job_info_id = s.job_info_id  GROUP BY project_name,branch_name,scanTime, s.job_info_id, job_num;"
        else:
            rptsql = "select project_name , branch_name ,scanTime ,SUM(CASE WHEN severity in ('High','Critical') and status='0' THEN 1 ELSE 0 END ) as 'ld'," \
                     "SUM(CASE WHEN severity in ('High','Critical') and status='2' THEN 1 ELSE 0 END ) as 'hl', s.job_info_id ,jp.job_num from " \
                     "(select j.id as job_info_id, p.project_name as project_name ,j.branch_name as branch_name,j.scanTime as scanTime, p.region as region, j.job_num as job_num from fortify_job_info j ,fortify_project_info p where j.project_id = p.id and p.status='0' and j.status='1') jp ," \
                     "fortify_scan_result s where jp.job_info_id = s.job_info_id and jp.region='{0}'  GROUP BY project_name,branch_name,scanTime, s.job_info_id,jp.job_num;".format(
                distribute)
        try:
            projectsresult = self.db.executeSql(rptsql)
            for project in projectsresult:
                detailsql = "SELECT severity,filename,function,line,abstract,explanation,recommendation,category,kingdom ,status FROM fortify_scan_result where job_info_id ='{0}' and  `status`<>'1' and severity in ('Critical','High')".format(
                    project[5])
                detailresult = self.db.executeSql(detailsql)
                statics_dict[project] = detailresult
        except Exception:
            logger.error('运行出错：{}'.format(traceback.print_exc()))

        return statics_dict


if __name__ == '__main__':
    rw = ReportWriter()
    # xlsx_report_file = "{0}/{1}-fortify-result.xlsx".format(report_dir,build.replace('#','_of_'))
    # projectname ='sz-ai-server'
    # branch = 'master'
    rw.writesumarrysheet('ALL', r'C:\Users\wilton\PycharmProjects\ScanPlatformTool\FortifyResult\FortifySumarry.xlsx')

    # rw.writeToExcel('sz-ai-server', r'E:\develop\PycharmProjects\ScanPlatformTool\FortifyResult\{0}_of_{1}-fortifyresult.xlsx'.format(projectname, branch))
