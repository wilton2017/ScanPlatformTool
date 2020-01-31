# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       admin
   date：          2020/1/5
-------------------------------------------------
   Change Activity:
                   2020/1/5:
-------------------------------------------------
"""
__author__ = 'admin'

from constant import Constant
import traceback
from ReportWriter import ReportWriter
from fortifyScan import FortifyScan
import os
import sys
import configparser
import argparse
import logging
import platform
import shutil
from utils.MyDB import MysqlHelper
from utils.mygitlab import GitlabAPI
from utils.ParseProperties import parse

mydb = MysqlHelper()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

currpath = os.path.dirname(os.path.realpath(__file__))

config = configparser.ConfigParser()
config.read(currpath + '/config/sscconfig.ini', encoding='utf-8-sig')
ant_home = config.get('ANT', 'ANT_HOME')

git = GitlabAPI()


def arg_parser():
    parser = argparse.ArgumentParser(description='Fortify静态扫描 报告生成工具')
    parser.add_argument('-A', '--attach', default='False', choices=['True', 'False'], help="是否进行增量扫描", dest="attach")
    parser.add_argument('-i', '--whitelist', help="为项目添加白名单", dest="whitelist")
    parser.add_argument('-u', '--repository_url', help="源代码git地址", dest="repository_url")
    parser.add_argument('-r', '--report', help="报告生成目录", dest="report")
    parser.add_argument('-w', '--workspace', help="Job工作空间路径", dest="workspace")
    parser.add_argument('-s', '--srcpath', help="源码文件目录", dest='srcpath')
    parser.add_argument('-n', '--jobname', help="任务名称", dest='jobname')
    parser.add_argument('-b', '--branch', help="代码分支名称", dest='branch')
    parser.add_argument('-z', '--reporttype', choices=['OP', 'OT', 'CB', 'ALL'],
                        help="输入部门缩写OP、OT、CB、ALL\n ALL 表示统计所有部门", dest='zone')
    args = parser.parse_args()

    if args.report is None or args.report.strip() == '':
        logger.info('report path is None ,use {0}/FortifyResult instead'.format(args.workspace))
        args.report = args.workspace

    args.branch = 'master' if args.branch is None else args.branch

    logger.info(args)
    return args


def copy_update_files(repost_url, branch_name, workspace ):
    """

    :param repost_url:  git_url 地址，获取工程名称
    :param branch_name: 分支
    :param workspace: commit.properties 目录
    :param dest_path: 拷贝目标路径
    :return:
    """
    commifile = '{0}/commit.properties'.format(workspace.replace('\\','/'))
    project_name = repost_url.replace('.git', '').split('/')[-1]
    project_id = git.get_project_id(project_name)
    if project_id == None:
        return False
    commit = git.get_commit_project(branch_name, project_name)
    if commit == None:
        return False
    if not os.path.exists(commifile):
        f = open(commifile, 'ab')
        testnote = 'commit_id1={0}'.format(commit['id'])
        f.write(testnote.encode('utf-8'))
        f.close()
        commit_id1 = commit['id']
    else:
        bo = parse(commifile)
        commit_id1 = bo.get('commit_id1')
    commit_id2 = commit['id']
    fils = git.get_changefiles_compare(project_id, commit_id1, commit_id2)
    if len(fils) == 0:
        return False

    for file in fils:
        copyfile(file, workspace)
    bo = parse(commifile)
    bo.put('commit_id1', commit['id'])
    return True

def copyfile(file, workspace):
    """
    复制变更文件到目的目录
    :param file:
    :param workspace:
    :return:
    """
    files = '/'.join(file.replace('\\', '/').split('/')[0:-1])
    dest = '{0}/attach_dir/{1}'.format(workspace, files)
    srcfile = "{0}/{1}".format(workspace.replace('\\', '/'), file)
    if not os.path.exists(dest):
        os.makedirs(dest, exist_ok=True)
        if not os.path.exists(srcfile):
            return False
        else:
            shutil.copy(srcfile, dest)
            return True
    else:
        if not os.path.exists(srcfile):
            return False
        else:
            shutil.copy(srcfile, dest)
            return True


def write_commitid( repost_url, branch_name, workspace):
    """
    往commit.properties 写commit_id1 的内容
    :param repost_url:
    :param branch_name:
    :param workspace: 工作空间目录

    :return: 返回 True 写成功，FLASE 写失败
    """
    commitfile = '{0}/commit.properties'.format(workspace.replace('\\','/'))

    project_name = repost_url.replace('.git', '').split('/')[-1]
    project_id = git.get_project_id(project_name)
    if project_id == None:
        return False
    commit = git.get_commit_project(branch_name, project_name)
    if commit == None:
        return False
    if not os.path.exists(commitfile):
        f = open(commitfile, 'ab')
        testnote = 'commit_id1={0}'.format(commit['id'])
        f.write(testnote.encode('utf-8'))
        f.close()
    else:
        bo = parse(commitfile)
        bo.put('commit_id1', commit['id'])
    return True


def genSumarryreport(distribute, report_path):
    logger.info("Create report ...")
    try:
        report_dir = "{0}/{1}".format(report_path, Constant.FORTIFY_RESULT_DIR.value)
        os.makedirs(report_dir, exist_ok=True)
        xlsx_report_file = "{0}/FortifySumarry.xlsx".format(report_dir)
        rw = ReportWriter()
        rw.writesumarrysheet(distribute, xlsx_report_file)
        return 0
    except Exception:
        logger.error(traceback.print_exc())
        return 1

def main(args):
    if args.report is None or args.report.strip() == '':
        logger.info('report path is None, use {0}/FortifyResult instead'.format(currpath))
        args.report = currpath

    report = args.report.strip()
    zone = args.zone
    if zone is not None:
        res = genSumarryreport(zone, report)
        sys.exit(res)
    else:
        branch = args.branch.strip()
        branch = "" if branch is None else branch.replace(r'origin/', '')
        repository_url = args.repository_url.strip()
        workspace = args.workspace.strip().replace('\\', '/')
        srcpath = args.srcpath.strip().replace('\\', '/')

        if args.attach.upper() == "TRUE":
            attach_dir = "{0}/{1}".format(workspace, 'attach_dir')
            module = srcpath.split('/')[-1]
            if os.path.exists(attach_dir):
                shutil.rmtree(attach_dir)
            flag = copy_update_files(repository_url, branch, workspace)
            if flag == True:
                srcpath = attach_dir+'/'+module
            else:
                logger.warning('前后扫描的文件无变更，故无需扫描，扫描结果还是上次上面的结果')
                sys.exit(0)
        if srcpath.split('/')[-1].lower() == 'none':
            srcpath = '/'.join(srcpath.split('/')[0:-1])

        projectname = args.jobname.strip()
        projectname = "unknown-project" if projectname is None else projectname.replace(r'scan-', '')
        whilestr = args.whitelist.strip()
        sca = FortifyScan(srcpath)
        flag = sca.scan_job_initialize(projectname, branch)
        if flag:
            osname = platform.platform()
            if osname.find('Windows') >= 0:
                ant_cmd = '{0}/ant.bat -file {1}/{2} -Divy.home={3}&& exit %%ERRORLEVEL%%'.format(ant_home, srcpath,
                                                                                                  Constant.ANT_BUILD_XML.value,
                                                                                                  srcpath)
                if not os.path.exists(
                        '{0}/{1}'.format(srcpath, Constant.ANT_BUILD_PROPERTIES.value)) or not os.path.exists(
                        '{0}/{1}'.format(srcpath, Constant.ANT_BUILD_XML.value)):
                    logger.info("Config file of Fortify not exist")
                    sys.exit(1)
            else:
                if not os.path.exists(
                        '{0}/{1}'.format(srcpath, Constant.ANT_BUILD_PROPERTIES_LINUX.value)) or not os.path.exists(
                        '{0}/{1}'.format(srcpath, Constant.ANT_BUILD_XML_LINUX.value)):
                    logger.info("Config file of Fortify not exist")
                    sys.exit(1)
                ant_cmd = '{0}/ant -file {1}/{2} -Divy.home={3}'.format(
                    ant_home, srcpath, Constant.ANT_BUILD_XML_LINUX.value,
                    srcpath)

            mydb.init_fortifyscan_data(projectname, branch, srcpath, repository_url)

            logger.info("Starting Fortify scan ...  ")

            cmd_result = os.system(ant_cmd)
            if cmd_result == 0:
                sca.check_fpr_gen_done()
                if whilestr == 'kong':
                    pass
                else:
                    projectid = mydb.getProjectID(projectname, srcpath)
                    mydb.insertwhitelist(projectid, whilestr)

                fortifyresult = workspace+'/FortifyResult'

                if os.path.exists(fortifyresult):
                    shutil.rmtree(fortifyresult)

                res = sca.reportgenerate(report)
                write_commitid(repository_url, branch, workspace)
                sys.exit(res)

            else:
                logger.info('execute fortify scan fail')
                sys.exit(1)
        else:
            sys.exit(1)


if __name__ == '__main__':
    main(arg_parser())

