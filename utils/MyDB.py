# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MyDB.py
   Description :
   Author :       admin
   date：          2020/1/5
-------------------------------------------------
   Change Activity:
                   2020/1/5:
-------------------------------------------------
"""
__author__ = 'admin'

import pymysql
import re
import configparser
import os

currpath = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read('{0}/../config/sscconfig.ini'.format(currpath), encoding='utf-8-sig')
db_host = config.get('MySQL', 'host')
db_user = config.get('MySQL', 'user')
db_password = config.get('MySQL', 'password')
db_port = config.get('MySQL', 'port')
db_name = config.get('MySQL','db')


class MysqlHelper:
    # 构造函数
    def __init__(self, host=db_host, user=db_user, pwd=db_password, port=db_port, db=db_name):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.port = port
        self.db = db
        self.conn = None
        self.cur = None

        try:
            self.con = pymysql.connect(host=self.host, user=self.user, passwd=self.pwd, port=self.port, db=self.db)
            # 所有的查询，都在连接 con 的一个模块 cursor 上面运行的
            self.cur = self.con.cursor()
        except:
            raise pymysql.err.IntegrityError

    def close(self):
        """关闭数据库连接

        """
        if not self.con:
            self.con.close()
        else:
            raise pymysql.err.IntegrityError

    def getVersion(self):
        """获取数据库的版本号

        """
        self.cur.execute("SELECT VERSION()")
        return self.getOneData()

    def getOneData(self):
        # 取得上个查询的结果，是单个结果
        data = self.cur.fetchone()
        return data

    def creatTable(self, tablename, attrdict, constraint):
        """创建数据库表

            args：
                tablename  ：表名字
                attrdict   ：属性键值对,{'book_name':'varchar(200) NOT NULL'...}
                constraint ：主外键约束,PRIMARY KEY(`id`)
        """
        if self.isExistTable(tablename):
            return
        sql = ''
        sql_mid = '`id` bigint(11) NOT NULL AUTO_INCREMENT,'
        for attr, value in attrdict.items():
            sql_mid = sql_mid + '`' + attr + '`' + ' ' + value + ','
        sql = sql + 'CREATE TABLE IF NOT EXISTS %s (' % tablename
        sql = sql + sql_mid
        sql = sql + constraint
        sql = sql + ') ENGINE=InnoDB DEFAULT CHARSET=utf8'
        self.executeCommit(sql)

    def executeSql(self, sql=''):
        """执行sql语句，针对读操作返回结果集

            args：
                sql  ：sql语句
        """
        try:
            self.cur.execute(sql)
            records = self.cur.fetchall()
            return records
        except pymysql.Error as e:
            error = 'MySQL execute failed! ERROR (%s): %s' % (e.args[0], e.args[1])
            print(error)

    def executeSql_one(self, sql=''):
        try:
            self.cur.execute(sql)
            records = self.getOneData()
            return records
        except pymysql.Error as e:
            error = 'MySQL execute failed! ERROR (%s): %s' % (e.args[0], e.args[1])
            print(error)

    def executeCommit(self, sql=''):
        """执行数据库sql语句，针对更新,删除,事务等操作失败时回滚

        """
        try:
            self.cur.execute(sql)
            self.con.commit()
        except pymysql.Error as e:
            self.con.rollback()
            # error = 'MySQL execute failed! ERROR (%s): %s' %(e.args[0],e.args[1])
            raise pymysql.err.IntegrityError

    def insert(self, tablename, params):
        """创建数据库表

            args：
                tablename  ：表名字
                key        ：属性键
                value      ：属性值
        """
        key = []
        value = []
        for tmpkey, tmpvalue in params.items():
            key.append(tmpkey)
            if isinstance(tmpvalue, str):
                value.append("\'" + tmpvalue + "\'")
            else:
                value.append(tmpvalue)
        attrs_sql = '({0})'.format(','.join(key))
        values_sql = ' values({0})'.format(','.join(value))
        sql = 'insert into {0}{1}{2}'.format(tablename, attrs_sql, values_sql)
        self.executeCommit(sql)

    def basewhitlelist(self):
        """
        查询基础的常用误报的漏洞类型
        :return:
        """
        basewhitesql = 'select rulename from base_white_list'

        basewhites = self.executeSql(basewhitesql)
        baselist = []
        for rule in basewhites:
            baselist.append(rule[0])
        return baselist

    def getProjectID(self, projectname, srcpath):
        """
        通过项目名获取项目ID
        :param projectname:
        :return:
        """
        idsql = "select id from fortify_project_info where project_name='{0}' and scan_model='{1}' and status='0'".format(
            projectname, srcpath)
        try:
            projectID = self.executeSql_one(idsql)[0]
        except Exception:
            projectID = 0
        return projectID

    def insertwhitelist(self, projectID, whilestr):
        """
        该方法的作用是向项目白名单插入忽略的漏洞扫描规则
        :param projectname: 项目ID
        :param whilestr:  白名单字符串，多个规则名之间用半角符 的逗号隔开
        :return:
        """
        whilelist = whilestr.replace("，", ",").split(",")
        for rulename in whilelist:
            instersql = 'insert into fortify_whitelist(project_id,rule_name) values({0},"{1}");'.format(projectID,
                                                                                                        rulename)

            try:
                self.executeCommit(instersql)
            except Exception as e:
                pass

    def select(self, tablename, cond_dict='', order='', fields='*'):
        """查询数据

            args：
                tablename  ：表名字
                cond_dict  ：查询条件
                order      ：排序条件

            example：
                print mydb.select(table)
                print mydb.select(table, fields=["name"])
                print mydb.select(table, fields=["name", "age"])
                print mydb.select(table, fields=["age", "name"])
        """
        consql = ' '
        if cond_dict != '':
            for k, v in cond_dict.items():
                consql = consql + k + '=' + v + ' and'
        consql = consql + ' 1=1 '
        if fields == "*":
            sql = 'select * from %s where ' % tablename
        else:
            if isinstance(fields, list):
                fields = ",".join(fields)
                sql = 'select %s from %s where ' % (fields, tablename)
            else:
                raise pymysql.err.IntegrityError
        sql = sql + consql + order
        return self.executeSql(sql)

    def insertMany(self, table, attrs, values):
        """插入多条数据

            args：
                tablename  ：表名字
                attrs        ：属性键
                values      ：属性值

            example：
                table='test_mysqldb'
                key = ["id" ,"name", "age"]
                value = [[101, "liuqiao", "25"], [102,"liuqiao1", "26"], [103 ,"liuqiao2", "27"], [104 ,"liuqiao3", "28"]]
                mydb.insertMany(table, key, value)
        """
        values_sql = ['%s' for v in attrs]
        attrs_sql = '(' + ','.join(attrs) + ')'
        values_sql = ' values(' + ','.join(values_sql) + ')'
        sql = 'insert into %s' % table
        sql = sql + attrs_sql + values_sql
        try:
            for i in range(0, len(values), 20000):
                self.cur.executemany(sql, values[i:i + 20000])
                self.con.commit()
        except pymysql.Error as e:
            self.con.rollback()
            raise pymysql.err.IntegrityError

    def delete(self, tablename, cond_dict):
        """删除数据

            args：
                tablename  ：表名字
                cond_dict  ：删除条件字典

            example：
                params = {"name" : "caixinglong", "age" : "38"}
                mydb.delete(table, params)

        """
        consql = ' '
        if cond_dict != '':
            for k, v in cond_dict.items():
                if isinstance(v, str):
                    v = "\'" + v + "\'"
                consql = consql + tablename + "." + k + '=' + v + ' and '
        consql = consql + ' 1=1 '
        sql = "DELETE FROM %s where%s" % (tablename, consql)
        return self.executeCommit(sql)

    def update(self, tablename, attrs_dict, cond_dict):
        """更新数据

            args：
                tablename  ：表名字
                attrs_dict  ：更新属性键值对字典
                cond_dict  ：更新条件字典

            example：
                params = {"name" : "caixinglong", "age" : "38"}
                cond_dict = {"name" : "liuqiao", "age" : "18"}
                mydb.update(table, params, cond_dict)

        """
        attrs_list = []
        consql = ' '
        for tmpkey, tmpvalue in attrs_dict.items():
            if isinstance(tmpvalue, str):
                attrs_list.append("`" + tmpkey + "`" + "=" + "\'" + tmpvalue + "\'")
            else:
                attrs_list.append("`" + tmpkey + "`" + "= {0}".format(tmpvalue))
        attrs_sql = ",".join(attrs_list)
        if cond_dict != '':
            for k, v in cond_dict.items():
                if isinstance(v, str):
                    v = "\'" + v + "\'"
                consql = consql + "`" + tablename + "`." + "`" + k + "`" + '=' + v + ' and '
        consql = consql + ' 1=1 '
        sql = "UPDATE {0} SET {1} where{2}".format(tablename, attrs_sql, consql)
        return self.executeCommit(sql)

    def dropTable(self, tablename):
        """删除数据库表

            args：
                tablename  ：表名字
        """
        sql = "DROP TABLE  %s" % tablename
        self.executeCommit(sql)

    def deleteTable(self, tablename):
        """清空数据库表

            args：
                tablename  ：表名字
        """
        sql = "DELETE FROM %s" % tablename
        self.executeCommit(sql)

    def isExistTable(self, tablename):
        """判断数据表是否存在

            args：
                tablename  ：表名字

            Return:
                存在返回True，不存在返回False
        """
        sql = "select * from %s" % tablename
        result = self.executeCommit(sql)
        if result is None:
            return True
        else:
            if re.search("doesn't exist", result):
                return False
            else:
                return True

    def init_fortifyscan_data(self, projectname, branch_name, scan_model, repository_url=''):
        """
        初始化fortify 扫描任务，扫描项目
        :param projectname: 扫描项目名
        :param branch_name: 扫描分支名
        :param scan_model: 扫描源代码路径
        :param repository_url: 扫描代码git 地址
        :return:
        """

        insert_project_dict = {"project_name": projectname, "scan_model": scan_model,
                               "region": projectname.split('-')[0]}

        query_sql = 'select count(1) from fortify_project_info where project_name="{0}" and scan_model="{1}" ;'.format(
            projectname, scan_model)

        flag = self.executeSql_one(query_sql)[0]
        if int(flag) == 0:  # 检查是否存在记录，不存在则插入，存在则跳过
            try:
                self.insert('fortify_project_info', insert_project_dict)
            except Exception:
                pass

        update_state_sql = "update fortify_project_info set status='1' where project_name='{0}' and scan_model !='{1}';".format(
            projectname, scan_model)
        self.executeCommit(update_state_sql)
        project_id = self.getProjectID(projectname, scan_model)
        job_sql = {"project_id": str(project_id), "branch_name": str(branch_name),
                   "repository_url": str(repository_url)}

        update_job_status_sql = "update fortify_job_info set status='0' where project_id={0}".format(project_id)

        self.executeCommit(update_job_status_sql)

        update_job_sql = 'update fortify_job_info set job_num=job_num+1 , repository_url="{2}" where project_id={0} ' \
                         'and branch_name="{1}";'.format(project_id, branch_name, repository_url)
        try:
            self.insert("fortify_job_info", job_sql)
        except Exception:
            self.executeCommit(update_job_sql)

    def get_job_info_id(self, projectname, branchname):
        """
        通过项目名称、分支获取任务ID
        :param projectname:
        :param branchname:
        :param scan_model:

        :return:
        """

        job_info_sql = "select j.id from fortify_job_info j, fortify_project_info p where p.id = j.project_id and p.project_name='{0}' and j.branch_name='{1}' and p.status='0' ;".format(
            projectname, branchname)
        try:
            job_info_id = self.executeSql_one(job_info_sql)[0]
        except Exception:
            job_info_id = 0
        return job_info_id

    def get_job_id(self, projectname):
        """

        :param projectname:
        :return:
        """
        job_info_sql = "select j.id from fortify_job_info j, fortify_project_info p where j.project_id = p.id and p.project_name='{0}' and j.status='1' and p.status='0';".format(
            projectname)
        try:
            job_info_id = self.executeSql_one(job_info_sql)[0]
        except Exception:
            job_info_id = 0
        return job_info_id


if __name__ == "__main__":
    mydb = MysqlHelper()
    # table='sonarResult'
    # insertsql ={"projectname":"sz-ai-server"}
    # try:
    #     mydb.insert('fortify_project_info', insertsql)
    #     print("插入成功")
    # except Exception:
    #     print(mydb.getProjectID("sz-ai-server"))
    #     #print("插入失败")

    mydb.init_fortifyscan_data('OP-alibaba-dubbo', 'master',
                               'E:/develop/PycharmProjects/ScanPlatformTool/code/fortify-OP-alibaba-dubbo/spring-cloud-alibaba-dubbo',
                               r'https://github.com/heyingqin2017/spring-cloud-alibaba.git')

    # print(mydb.get_job_info_id('sz-ai-server', 'master'))

    # mydb.insertwhitelist(1,'Insecure Randomness,Unreleased Resource: Streams')
