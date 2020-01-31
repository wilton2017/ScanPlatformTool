# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mygitlab.py
   Description :
   Author :       wilton
   date：          2020/1/20 9:57
-------------------------------------------------
   Change Activity:
                   2020/1/20 9:57:
-------------------------------------------------
"""
__author__ = 'wilton'


import gitlab

import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

currpath = os.path.dirname(os.path.realpath(__file__))

class GitlabAPI(object):
    def __init__(self, *args, **kwargs):
        if os.path.exists('{0}/../config/python-gitlab.cfg'.format(currpath)):
            self.gl = gitlab.Gitlab.from_config('bwtgit', ['{0}/../config/python-gitlab.cfg'.format(currpath)])
        elif os.path.exists(os.getenv('HOME') + '/.python-gitlab.cfg'):
            self.gl = gitlab.Gitlab.from_config('bwtgit', [os.getenv('HOME') + '/.python-gitlab.cfg'])
        else:
            print('You need to make sure there is a file named "/etc/python-gitlab.cfg" or "~/.python-gitlab.cfg"')
            sys.exit(5)

    def get_user_id(self, username):
        user = self.gl.users.get_by_username(username)
        return user.id

    def get_group_id(self, groupname):
        group = self.gl.users.search(groupname)
        return group[0].id

    def get_all_projects(self):
        projects = self.gl.projects.list(all=True)
        result_list = []
        for project in projects:
            result_list.append(project.http_url_to_repo)
        return result_list

    def get_project_id(self, project_name):
        """
        查询git 项目的project_id
        :param project_name:
        :return:
        """
        project_id = 0
        for p in self.gl.projects.list(all=True, as_list=False):
            if p.name.upper() == project_name.upper():
                project_id = p.id
            else:
                pass
        return project_id

    def get_project_obj(self, project_id):
        """
        通过project_id 来获取对应的project 对象
        :param project_id:
        :return: project 对象

        """
        return self.gl.projects.get(project_id)


    def get_user_projects(self, userid):
        projects = self.gl.projects.owned(userid=userid, all=True)
        result_list = []
        for project in projects:
            result_list.append(project.http_url_to_repo)
        return result_list

    def get_group_projects(self, groupname):
        projects = self.gl.projects.owned(groupname=groupname, all=True)
        result_list = []
        for project in projects:
            result_list.append(project.http_url_to_repo)
        return result_list

    def get_branches_by_project(self, project_id):
        """
        获取项目下的所有分支
        :param project_id:
        :return: branch_list
        """
        try:
            project = self.get_project_obj(project_id)
            branch_list = list()
            branches = project.branches.list()
            for bh in branches:
                branch_list.append(bh.name)
            return sorted(branch_list, reverse=True)
        except gitlab.exceptions.GitlabGetError:
            logger.error('项目ID 不存在')

    def get_commit_project(self, branch_name, project_name):
        """
        输入分支名称、项目名称，获取commit 对象
        :param branch_name:
        :param project_name:
        :return: 返回commit 字典
        """
        try:
            project = self.get_project_obj(self.get_project_id(project_name))
            # 获取指定分支的属性
            branch = project.branches.get(branch_name)

            return branch.commit
        except gitlab.exceptions.GitlabGetError:
            logger.error('输入分支或者项目名称不存在')
    def get_commits_project(self,branch_name, project_name):
        """

        :param branch_name:
        :param project_name:
        :return:
        """
        try:
            project = self.get_project_obj(self.get_project_id(project_name))
            # 获取指定分支的属性
            branch = project.branches.get(branch_name)

            return branch.commit
        except gitlab.exceptions.GitlabGetError:
            logger.error('输入分支或者项目名称不存在')

    def get_tags_project(self,project_name):
        """
        获取指定仙姑的所有tages
        :param project_name:
        :return:
        """
        project_id = self.get_project_id(project_name)
        project = self.get_project_obj(project_id)
        tags = project.tags.list()
        taglist = list()
        for tag in tags:
            taglist.append(tag.name)
        return taglist


    def get_changefiles_compare(self, project_id, commit_id1, commit_id2):
        """
        Compare two branches, tags or commits，
        :param project:
        :param commit_id1:
        :param commit_id2:
        :return: changes files
        """
        update_files = list()
        try:
            project = self.get_project_obj(project_id)
            result = project.repository_compare(commit_id1, commit_id2)
            for file_diff in result['diffs']:
                srclist = file_diff['new_path'].split('.')
                if srclist[-1] in ['java', 'xml', 'properties'] and file_diff['new_path'] not in update_files:
                    update_files.append(file_diff['new_path'])
        except gitlab.exceptions.GitlabGetError:
            logger.error('输入参数异常，请检查是否有拼写错误')

        finally:
            return update_files


if __name__ == '__main__':

    git = GitlabAPI()
    project = git.get_project_obj(10)

    print(git.get_tags_project('NBTGAME'))

    # ---------------------------------------------------------------- #
    # 获取所有commit info
    commits = project.commits.list()
    for c in commits:
        print(c.author_name, c.message, c.title, c.created_at)


