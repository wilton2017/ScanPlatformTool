# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     constant
   Description :
   Author :       admin
   date：          2020/1/5
-------------------------------------------------
   Change Activity:
                   2020/1/5:
-------------------------------------------------
"""
__author__ = 'admin'

from enum import Enum


class Constant(Enum):
    SS_CONFIG_FILE = "/config/sscconfig.ini"
    ANT_BUILD_XML = "build_sca_local.xml"
    ANT_BUILD_XML_LINUX = "build_sca_local_linux.xml"
    ANT_BUILD_PROPERTIES_LINUX = "build_sca_local_linux.properties"

    ANT_BUILD_PROPERTIES = "build_sca_local.properties"
    FPR_FILE_PATH = "fortify_reports/sca_result_file.fpr"
    LCK_FILE_PATH = "fortify_reports/sca_scan.log.lck"
    FORTIFY_RESULT_DIR = "FortifyResult"
