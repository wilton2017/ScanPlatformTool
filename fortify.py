# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fortify
   Description :
   Author :       admin
   date：          2020/1/5
-------------------------------------------------
   Change Activity:
                   2020/1/5:
-------------------------------------------------
"""
__author__ = 'admin'

import html
import cgi
import re
from xml.etree import cElementTree
from collections import namedtuple, OrderedDict
import os, sys
from os.path import exists, splitext
from zipfile import ZipFile
from tempfile import mkdtemp
from shutil import rmtree
from enum import Enum
import logging
import argparse
from datetime import datetime
from utils.MyDB import MysqlHelper
import traceback

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Severity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


dr = re.compile(r'<[^>]+>', re.S)
# Data Structures
File = namedtuple("File", "size timestamp type encoding name loc")
Build = namedtuple("Build", "build_id number_of_files loc java_class_path source_base_path scan_time source_files")
ClassInfo = namedtuple("ClassInfo", "class_id kingdom type subtype analyzer_name default_severity")
InstanceInfo = namedtuple("InstanceInfo", "instance_id confidence instance_severity medainfo")
Metainfo = namedtuple("Metainfo", "group")
Vulnerability = namedtuple("Vulnerability", "class_info instance_info analysis_info")
Location = namedtuple("Location", "path line_start line_end col_start col_end")
Context = namedtuple("Context", "function_name namespace enclosing_class decl_location")
ReplacementDefs = namedtuple("ReplacementDefinitions", "items location")
AnalysisInfo = namedtuple("AnalysisInfo", "context replacement_defs trace")
NodeRef = namedtuple("NodeRef", "id")
Node = namedtuple("Node", "is_default snippet_id source_location action reason knowledge")
Trace = namedtuple("Trace", "nodes nodes_ref")
KeyValue = namedtuple("KeyValue", "key value")
TypeValue = namedtuple("TypeValue", "type value")
Description = namedtuple("Description", "content_type class_id abstract explanation recommendations references")
Reference = namedtuple("Reference", "title author")
Snippet = namedtuple("Snippet", "id file line_start line_end text")
FunctionDef = namedtuple("FunctionDef", "name namespace enclosing_class")
EngineData = namedtuple("EngineData", "version properties rule_packs command_line errors machine_info license_info")
RulePack = namedtuple("RulePack", "sku name version mac")
RuleInfo = namedtuple("RuleInfo", "ruleId probability accuracy impact")
MachineInfo = namedtuple("MachineInfo", "hostname username platform")
LicenseInfo = namedtuple("LicenseInfo", "metadata capabilities")
Capability = namedtuple("Capability", "name expiration")
RuleMetaInfo = namedtuple("RuleMetaInfo", "probability accuracy impact")
ScanTimeInfo = namedtuple("ScanTimeInfo", "scan_date scan_time")


def formatdatime(str):
    sdate, stime = str.split(" ")
    year_s, mon_s, day_s = sdate.split('-')
    hour_s, minu_s, second_s = stime.split(':')
    return datetime(int(year_s), int(mon_s), int(day_s), int(hour_s), int(minu_s), int(second_s))


def _xpath(path):
    return path.strip().replace("/", "/{%s}" % "xmlns://www.fortifysoftware.com/schema/fvdl")


def _get_nodes(root, p, fn=lambda node: node):
    out = []
    try:
        for item in root.findall(_xpath(p)):
            out.append(fn(item))
        return out
    except:
        return None


def _get_node(root, p, fn=lambda node: node.text):
    try:
        return fn(root.findall(_xpath(p))[0])
    except:
        return None


def _get_attr(name):
    return lambda node: node.attrib.get(name, None)


def _get_text(node):
    return node.text


def _make_node_ref(root):
    return NodeRef(id=root.attrib.get("id", None))


def _make_node(root):
    return Node(
        is_default=root.attrib.get("isDefault", "false") == "true",
        source_location=_get_node(root, "./SourceLocation", _make_location),
        snippet_id=_get_node(root, "./SourceLocation", _get_attr("snippet")),
        action=_get_node(root, "./Action",
                         lambda node: TypeValue(type=node.attrib.get("type", None), value=node.text)),
        reason=_get_node(root, "./Reason/Rule", _get_attr("ruleID")),
        knowledge=_get_nodes(root, "./Knowledge", lambda node: (node.attrib.get("primary", None),
                                                                node.attrib.get("type", None), node.text)))


def _make_file(root):
    return File(
        size=root.attrib.get("size", None),
        timestamp=root.attrib.get("timestamp", None),
        type=root.attrib.get("type", None),
        encoding=root.attrib.get("encoding", None),
        name=_get_node(root, "./Name"),
        loc=_get_nodes(root, "./LOC",
                       lambda node: TypeValue(type=node.attrib.get("type", None), value=node.text)))


def _make_build(root):
    return Build(
        build_id=_get_node(root, "./Build/BuildID"),
        number_of_files=_get_node(root, "./Build/NumberFiles"),
        loc=_get_nodes(root, "./Build/LOC",
                       lambda node: TypeValue(type=node.attrib.get("type", None), value=node.text)),
        java_class_path=_get_node(root, "./Build/JavaClasspath"),
        source_base_path=_get_node(root, "./Build/SourceBasePath"),
        scan_time=_get_node(root, "./Build/ScanTime"),
        source_files=_get_nodes(root, "./Build/SourceFiles/File", _make_file))


def _make_class_info(root):
    return ClassInfo(
        class_id=_get_node(root, "./ClassID"),
        kingdom=_get_node(root, "./Kingdom"),
        type=_get_node(root, "./Type"),
        subtype=_get_node(root, "./Subtype"),
        analyzer_name=_get_node(root, "./AnalyzerName"),
        default_severity=_get_node(root, "./DefaultSeverity"))


def _make_ruleinfo(root):
    """
    :param root:
    :return:
    """
    groups = _get_nodes(root, "./MetaInfo/Group")
    accuracy = 0.0
    impact = 0.0
    probability = 0.0
    for group in groups:
        if group.attrib['name'] == 'Accuracy':
            accuracy = float(group.text)
        elif group.attrib['name'] == 'Impact':
            impact = float(group.text)
        elif group.attrib['name'] == 'Probability':
            probability = group.text
    return RuleInfo(
        ruleId=_get_node(root, ".", _get_attr("id")),
        accuracy=accuracy,
        impact=impact,
        probability=probability)
    # rule_meta_info=_get_node(root, "./MetaInfo"))


def _make_instance_info(root):
    return InstanceInfo(
        instance_id=_get_node(root, "./InstanceID"),
        confidence=_get_node(root, "./Confidence"),
        instance_severity=_get_node(root, "./InstanceSeverity"),
        medainfo=_get_node(root, "./MetaInfo", _make_metainfo),

    )


def _make_vulnerability(root):
    return Vulnerability(
        class_info=_get_node(root, "./ClassInfo", _make_class_info),
        instance_info=_get_node(root, "./InstanceInfo", _make_instance_info),
        analysis_info=_get_node(root, "./AnalysisInfo", _make_analysis_info))


def _make_location(root):
    return Location(
        path=root.attrib.get("path", None),
        line_start=root.attrib.get("line", None),
        line_end=root.attrib.get("lineEnd", None),
        col_start=root.attrib.get("colStart", None),
        col_end=root.attrib.get("colEnd", None))


def _make_context(root):
    return Context(
        function_name=_get_node(root, "./Function", _get_attr("name")),
        namespace=_get_node(root, "./Function", _get_attr("namespace")),
        enclosing_class=_get_node(root, "./Function", _get_attr("enclosingClass")),
        decl_location=_get_node(root, "./FunctionDeclarationSourceLocation", _make_location))


def _make_replacement_defs(root):
    return ReplacementDefs(
        location=_get_node(root, "./LocationDef", _make_location),
        items=_get_nodes(root, "./Def",
                         lambda node: KeyValue(key=node.attrib.get("key", None), value=node.attrib.get("value", None))))


def _make_trace(root):
    return Trace(
        nodes=_get_nodes(root, "./Entry/Node", _make_node),
        nodes_ref=_get_nodes(root, "./Entry/NodeRef", _make_node_ref))


def _make_metainfo(root):
    return Metainfo(group=_get_node(root, "./Group", _get_text))


def _make_analysis_info(root):
    return AnalysisInfo(
        context=_get_node(root, "./Unified/Context", _make_context),
        replacement_defs=_get_node(root, "./Unified/ReplacementDefinitions", _make_replacement_defs),
        trace=_get_node(root, "./Unified/Trace/Primary", _make_trace))


def _make_reference(root):
    return Reference(
        title=_get_node(root, "./Title", _get_text),
        author=_get_node(root, "./Author", _get_text))


def _make_description(root):
    return Description(
        content_type=root.attrib.get("contentType", None),
        class_id=root.attrib.get("classID", None),
        explanation=_get_node(root, "./Explanation", _get_text),
        abstract=_get_node(root, "./Abstract", _get_text),
        recommendations=_get_node(root, "./Recommendations", _get_text),
        references=_get_nodes(root, "./References/Reference", _make_reference))


def _make_snippet(root):
    return Snippet(
        id=root.attrib.get("id", None),
        file=_get_node(root, "./File", _get_text),
        line_start=_get_node(root, "./StartLine", _get_text),
        line_end=_get_node(root, "./EndLine", _get_text),
        text=_get_node(root, "./Text", _get_text))


def _make_function_def(root):
    return FunctionDef(
        name=root.attrib.get("name", None),
        namespace=root.attrib.get("namespace", None),
        enclosing_class=root.attrib.get("enclosingClass", None))


def _make_rule_pack(root):
    return RulePack(
        sku=root.attrib.get("SKU", None),
        name=root.attrib.get("Name", None),
        version=root.attrib.get("Version", None),
        mac=root.attrib.get("MAC", None))


def _make_property(root):
    return KeyValue(
        key=_get_node(root, "./name", _get_text),
        value=_get_node(root, "./value", _get_text))


def _make_error(root):
    return KeyValue(
        key=root.attrib.get("code", None),
        value=root.text)


def _make_machine_info(root):
    return MachineInfo(
        hostname=_get_node(root, "./Hostname", _get_text),
        username=_get_node(root, "./Username", _get_text),
        platform=_get_node(root, "./Platform", _get_text))


def _make_license_info(root):
    return LicenseInfo(
        metadata=_get_nodes(root, "./Metadata", lambda node: KeyValue(
            key=_get_node(node, "./name", _get_text),
            value=_get_node(node, "./value", _get_text))),
        capabilities=_get_nodes(root, "./Capability", lambda node: Capability(
            name=_get_node(node, "./Name", _get_text),
            expiration=_get_node(node, "./Expiration", _get_text))))


def _make_engine_data(root):
    return EngineData(
        version=_get_node(root, "./EngineVersion", _get_text),
        rule_packs=_get_nodes(root, "./RulePacks/RulePack", _make_rule_pack),
        properties=_get_nodes(root, "./Properties/Property", _make_property),
        command_line=_get_nodes(root, "./CommandLine/Argument", _get_text),
        errors=_get_nodes(root, "./Errors/Error", _make_error),
        machine_info=_get_node(root, "./MachineInfo", _make_machine_info),
        license_info=_get_node(root, "./LicenseInfo", _make_license_info))


def _make_scantime(root):
    return ScanTimeInfo(
        scan_date=root.attrib.get("date", None),
        scan_time=root.attrib.get("time", None)
    )


def fortify_replace(des, items):
    """

    :param des: 漏洞类型描述对象
    :param items: abstact 中的key value 列表
    :return: descdict
    """
    desdict = {"abstract": "", "explanation": "", "recommendations": ""}
    if len(des) == 0:
        return desdict
    else:
        des = des[0]
        if items == None:
            desdict['abstract'] = des.abstract
            desdict['explanation'] = des.explanation
            desdict['recommendations'] = des.recommendations
        else:
            tempstr = des.abstract
            for item in items:
                if item is not None:
                    tempstr = tempstr.replace('<Replace key="{0}" />'.format(item.key), item.value)
            desdict["abstract"] = tempstr
            if des.explanation is not None:
                tempstr = des.explanation
                for item in items:
                    if item is not None:
                        tempstr = tempstr.replace('<Replace key="{0}" />'.format(item.key), item.value)

                desdict["explanation"] = tempstr

            if des.recommendations is not None:
                tempstr = des.recommendations
                for item in items:
                    if item is not None:
                        tempstr = tempstr.replace('<Replace key="{0}" />'.format(item.key), item.value)
                desdict["recommendations"] = tempstr

        return desdict


class Rule:
    def __init__(self, ruleId, probability, accuracy, impact):
        self.probability = float(probability)
        self.ruleId = ruleId
        self.accuracy = float(accuracy)
        self.impact = float(impact)

    def calculateSeverity(self, confidence, prob):
        if (prob != -1):
            self.probability = prob
        likelihood = (self.accuracy * self.probability * confidence) / 25
        if self.impact >= 2.5:
            if likelihood >= 2.5:
                return Severity.CRITICAL
            else:
                return Severity.HIGH
        else:
            if likelihood >= 2.5:
                return Severity.MEDIUM
            else:
                return Severity.LOW

    def getRuleId(self):
        return self.ruleId


class FPR(object):

    def __init__(self, filename=None):
        if not exists(filename):
            raise Exception("{} does not exists!".format(filename))
        ext = splitext(filename)[1].lower().replace(".", "")
        srclist = filename.replace('\\', '/').split('/')
        self.temppath = mkdtemp("fvdl") if ext == "fpr" else None
        self.files = {}
        self.parsereport = {}
        self.src_code = '/'.join(srclist[0:-2])
        self.db = MysqlHelper()

        if self.temppath is not None:
            with ZipFile(filename, "r") as f:
                f.extractall(self.temppath)

            xml = cElementTree.parse("{}/src-archive/index.xml".format(self.temppath)).getroot()
            self.files = dict((entry.attrib["key"].strip().lower(), "{}/{}".format(self.temppath, entry.text.strip()))
                              for entry in xml.findall("entry"))
            root = cElementTree.parse("{}/audit.fvdl".format(self.temppath)).getroot()
        else:
            root = cElementTree.parse(filename).getroot()

        self.vulnerabilities = _get_nodes(root, "./Vulnerabilities/Vulnerability", _make_vulnerability)
        self.build = _make_build(root)
        self.descriptions = _get_nodes(root, "./Description", _make_description)
        self.scantime = _get_node(root, "./CreatedTS", _make_scantime)
        self.snippets = _get_nodes(root, "./Snippets/Snippet", _make_snippet)
        self.called_with_no_def = _get_nodes(root, "./ProgramData/CalledWithNoDef/Function", _make_function_def)
        self.engine_data = _get_node(root, "./EngineData", _make_engine_data)
        self.rules = _get_nodes(root, "./EngineData/RuleInfo/Rule", _make_ruleinfo)
        self.findings = []
        self.root = root

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self, clean=True):
        if self.temppath is None:
            return

        if clean:
            rmtree(self.temppath)

        self.temppath = None

    def get_build(self):
        return self.build.build_id

    def get_description_classid(self, classid):
        return [x for x in self.descriptions if x is not None and x.class_id == classid]

    def extractFindings(self):

        build = self.build.build_id.split("#")

        if len(build) > 1:
            projectname = build[0]
            branch = build[1]
        else:
            projectname = build[0]
            branch = "master"

        whitelist = self.getwhilerule_by_projectname(projectname) + self.db.basewhitlelist()

        scanTime = self.scantime.scan_date + " " + self.scantime.scan_time

        self.execupdatestatus(projectname, branch, scanTime)

        for vuln in self.vulnerabilities:

            kingdom = vuln.class_info.kingdom
            category = vuln.class_info.type

            if vuln.class_info.subtype != None:
                category = vuln.class_info.type + ': ' + vuln.class_info.subtype
            if vuln.analysis_info.context.function_name != None:

                function = vuln.analysis_info.context.function_name
            else:
                function = ''
            if vuln.analysis_info.context.decl_location != None:
                filename = vuln.analysis_info.context.decl_location.path
                line = vuln.analysis_info.context.decl_location.line_start
            else:
                filename = ''
                line = ''
            classid = vuln.class_info.class_id
            issueid = vuln.instance_info.instance_id
            confidence = float(vuln.instance_info.confidence)
            severity = Severity.LOW
            probability = -1

            for rule in self.rules:
                crule = Rule(rule.ruleId, rule.probability, rule.accuracy, rule.impact)
                if crule.getRuleId() == classid:
                    severity = crule.calculateSeverity(confidence, probability)
                    break
            if vuln.analysis_info.replacement_defs != None:
                items = vuln.analysis_info.replacement_defs.items
                des = fortify_replace(self.get_description_classid(classid), items)
                abstract = html.unescape(dr.sub('', str(des['abstract'])))
                recommendations = html.unescape(dr.sub('', str(des['recommendations'])))
                explanation = html.unescape(dr.sub('', str(des['explanation'])))
            else:
                des = fortify_replace(self.get_description_classid(classid), items=None)
                abstract = html.unescape(dr.sub('', str(des['abstract'])))
                recommendations = html.unescape(dr.sub('', str(des['recommendations'])))
                explanation = html.unescape(dr.sub('', str(des['explanation'])))
            issuedetail = OrderedDict()
            # 领域
            issuedetail['kingdom'] = kingdom
            # 漏洞类型
            issuedetail['category'] = category
            status = 0
            if category in whitelist:
                status = 2
            # 漏洞问题所在文件路径
            issuedetail['fullFileName'] = filename
            # 风险级别
            if severity.value == 4:
                friority = 'Critical'
            elif severity.value == 3:
                friority = 'High'

            elif severity.value == 2:
                friority = 'Medium'
            else:
                friority = 'Low'

            # 是否忽略
            issuedetail['status'] = status

            issuedetail['issueName'] = category

            issuedetail['friority'] = friority
            # 问题所在函数
            issuedetail['function'] = function
            # 问题所在行
            issuedetail['lineNumber'] = line
            # 问题描述
            issuedetail['overview'] = abstract
            # 问题说明
            issuedetail['detail'] = explanation
            # 推荐修改建议
            issuedetail['recommendation'] = recommendations
            # 问题trace路径
            # issuedetail['trace'] = trace

            info_id = self.db.get_job_info_id(projectname, branch)
            self.execfortifyscanresult(info_id, issueid, kingdom, category, filename, friority, function, line,
                                       abstract, explanation, recommendations, status)

            # self.execFortifyScanDetail(issueid,classid,projectname,branch,scanTime,kingdom, category, filename, friority, function, line, abstract, explanation, recommendations, status)

    def getwhilerule_by_projectname(self, projectname):
        """

        :param projectname: 扫描项目名称
        :param src_code_name: 代码模块目录
        :return:
        """
        sql = 'select rule_name from fortify_project_info p ,fortify_whitelist w where p.id=w.project_id' \
              ' and p.project_name="{0}" and p.status="0"'.format(projectname)
        baselist = []
        basewhites = self.db.executeSql(sql)
        for rule in basewhites:
            baselist.append(rule[0])
        return baselist

    def execupdatestatus(self, projectname, branchname, scantime):
        """

        :param projectname:
        :param branchname:
        :param scantime:
        :return:
        """

        # 更新扫描时间
        job_info_id = self.db.get_job_info_id(projectname, branchname)

        updatescan_sql = {"scanTime": str(scantime), "status": '1'}

        con_dict_scantime = {"id": str(job_info_id)}

        self.db.update('fortify_job_info', updatescan_sql, con_dict_scantime)

        # project_id 下的非branch 下的任务状态 为 过期状态 0

        update_status_branch = 'update fortify_job_info set status="0" where project_id = {0} and branch_name !="{1}";'.format(
            self.db.getProjectID(projectname, self.src_code), branchname)
        self.db.executeCommit(update_status_branch)

        # 首先更新job_info_id 下的status 为 1

        updatestatup = {"status": '1'}
        cond_dict_statu = {"job_info_id": str(job_info_id)}
        # cond_dict_statu1 = {"projectname": str(projectname)}

        self.db.update('fortify_scan_result', updatestatup, cond_dict_statu)

    def execfortifyscanresult(self, job_id, issueid, kingdom, category, filename, severity, function="",
                              line=1, abstract="", explanation="", recommendation="", status='0'):
        """
        :param job_id: 任务ID
        :param issueid: 问题ID
        :param classid: 规则ID

        :param kingdom: 领域
        :param category: 漏洞类型
        :param filename: 文件路径
        :param severity: 风险级别
        :param function: 方法
        :param line: 问题所在开始行
        :param abstract: 问题描述
        :param explanation: 问题详细说明
        :param recommendations: 修改建议
        :param status: 问题状态
        :return:
        """

        insertp = {"job_info_id": str(job_id), "issueid": str(issueid),
                   "kingdom": str(kingdom), 'filename': str(filename), "severity": str(severity.strip()),
                   "function": str(function), "abstract": html.escape(abstract),
                   "explanation": html.escape(explanation), "recommendation": html.escape(recommendation),
                   "status": str(status), 'category': str(category), "line": str(line)}

        updatep = {"status": str(status), "severity": severity.strip()}
        cond_dict = {'job_info_id': str(job_id), 'issueid': str(issueid)}

        # self.db.insert('fortify_scan_result', insertp)
        try:
            self.db.insert('fortify_scan_result', insertp)
        except Exception:
            self.db.update('fortify_scan_result', updatep, cond_dict)

    def execFortifyScanDetail(self, issueid, classid, projectname, branch, scantime,
                              kingdom, category, filename, severity, function="",
                              line=1, abstract="", explanation="", recommendations="", status=0):
        """
        :param issueid: 问题ID
        :param classid: 问题所属规则ID
        :param projectname: 项目名称
        :param branch: 扫描分支
        :param scantime: 扫描时间
        :param kingdom: 领域
        :param category: 漏洞类型
        :param filename: 文件路径
        :param severity: 风险级别
        :param function: 方法
        :param line: 问题所在开始行
        :param abstract: 问题描述
        :param explanation: 问题详细说明
        :param recommendations: 修改建议
        :param status: 问题状态
        :return:
        """
        # 如果存在，执行update 操作，如果不存在执行插入操作
        scanTime = formatdatime(scantime)
        insertp = {"issueid": str(issueid), "classid": str(classid), "projectName": projectname, "branch": str(branch),
                   "scanTime": str(scanTime),
                   "kingdom": str(kingdom), 'filename': str(filename), "severity": str(severity.strip()),
                   "function": str(function), "abstract": html.escape(abstract),
                   "explanation": html.escape(str(explanation)), "recommendations": html.escape(recommendations),
                   "status": str(status), 'category': category, "line": line}
        updatep = {'branch': str(branch), "status": str(status), "severity": severity.strip(),
                   "scanTime": str(scanTime)}
        cond_dict = {'projectName': projectname, 'issueid': str(issueid)}
        try:
            self.db.insert('fortifyscandetail', insertp)
            # print("插入成功")
        except Exception:
            self.db.update('fortifyscandetail', updatep, cond_dict)
            # print("更新成功")


if __name__ == "__main__":
    fp = FPR(
        r'E:\develop\PycharmProjects\ScanPlatformTool\code\fortify-OP-alibaba-dubbo\spring-cloud-alibaba-dubbo\fortify_reports\sca_result_file.fpr')
    fp.extractFindings()
