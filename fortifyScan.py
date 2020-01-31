# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fortifyScan
   Description :
   Author :       admin
   date：          2020/1/5
-------------------------------------------------
   Change Activity:
                   2020/1/5:
-------------------------------------------------
"""
__author__ = 'admin'

import os
import sys
import configparser
import shutil
from fortify import FPR
from ReportWriter import ReportWriter
import logging
import time
import platform
from constant import Constant
import traceback

currpath = os.path.dirname(os.path.realpath(__file__))
try:
    from utils.ParseProperties import parse
except Exception:
    sys.path.append(currpath + '/utils')
    from ParseProperties import parse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FortifyScan(object):

    def __init__(self, src_path, config_path=currpath.replace('\\', '/') + Constant.SS_CONFIG_FILE.value):
        """

        :param src_path:
        :param config_path:
        """
        self.path = config_path
        config = configparser.ConfigParser()
        config.read(config_path, encoding='utf-8-sig')
        self._ant_home = config.get('ANT', 'ANT_HOME')
        self._src_path = src_path

    def scan_job_initialize(self, project, branch):
        """
        判断 目录是否有build-sca.properties 文件
        :return:
        """
        buildid = "{0}#{1}".format(project, branch)

        osname = platform.platform()

        try:
            logger.info('Copy file to:{0}'.format(self._src_path))
            if osname.find('Windows') >= 0:
                scafile = "{0}/{1}".format(self._src_path, Constant.ANT_BUILD_PROPERTIES.value)
                shutil.copy("{0}/config/{1}".format(currpath, Constant.ANT_BUILD_XML.value), self._src_path)
                shutil.copy("{0}/config/{1}".format(currpath, Constant.ANT_BUILD_PROPERTIES.value), self._src_path)
            else:
                scafile = "{0}/{1}".format(self._src_path, Constant.ANT_BUILD_PROPERTIES_LINUX.value)
                shutil.copy("{0}/config/{1}".format(currpath, Constant.ANT_BUILD_XML_LINUX.value), self._src_path)
                shutil.copy("{0}/config/{1}".format(currpath, Constant.ANT_BUILD_PROPERTIES_LINUX.value),
                            self._src_path)
            bo = parse(scafile)
            bo.put('project_name', project)
            bo.put('build_id', buildid)
            # bo.put('scan_attach', scan_attach)
            return True
        except Exception:
            logger.error(traceback.print_exc())
            return False

    def reportgenerate(self, report_path):

        logger.info("Create report ...")
        fpr_path = "{0}/{1}".format(self._src_path, Constant.FPR_FILE_PATH.value)
        if not os.path.exists(fpr_path):
            logger.error("No FPR file found :{0}".format(fpr_path))
            return 1
        try:
            fpr = FPR(fpr_path)
            build = fpr.get_build()
            projectname = build.split('#')[0]
            logger.info('project_name : {0}'.format(projectname))
            fpr.extractFindings()
            report_dir = "{0}/{1}".format(report_path, Constant.FORTIFY_RESULT_DIR.value)
            os.makedirs(report_dir, exist_ok=True)
            xlsx_report_file = "{0}/{1}-fortify-result.xlsx".format(report_dir, build.replace('#', '_of_'))
            logger.info("Save result to ：{0}".format(xlsx_report_file))
            rw = ReportWriter()
            rw.writeToExcel(projectname, xlsx_report_file)
            return 0
        except Exception:
            logger.error(traceback.print_exc())
            return 1

    def check_fpr_gen_done(self):
        """
        检查是否生成了fpr 文件
        :return:
        """

        lck_file = '{0}/{1}'.format(self._src_path, Constant.LCK_FILE_PATH.value)
        fpr_path = '{0}/{1}'.format(self._src_path, Constant.FPR_FILE_PATH.value)
        times = 0
        while times < 100:
            if not os.path.exists(lck_file) and os.path.exists(fpr_path):
                time.sleep(3)
                break
            time.sleep(1)
            times = times + 1


if __name__ == '__main__':
    src_path = r"E:\develop\PycharmProjects\ScanPlatformTool\code\fortify-sz-ai-server"
    report_path = r"E:\develop\PycharmProjects\ScanPlatformTool"
    sca = FortifyScan(src_path)
    sca.scan_job_initialize("fortify-sz-ai-server", "master")
    # sca.reportgenerate(report_path)
    # edit_sca_xml("E:\\develop\\PycharmProjects\\ScanPlatformTool\\code\\fortify-OP-alibaba-dubbo\\spring-cloud-alibaba-dubbo\\build_sca_local_linux.xml","False")
