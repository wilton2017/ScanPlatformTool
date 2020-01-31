# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ParseProperties
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
import tempfile
import traceback
import re


class Properties(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.properties = {}
        try:
            with open(file_name, encoding='utf-8') as fopen:
                for line in fopen:
                    if line.find('=') > 0 and not line.startswith('#'):
                        strs = line.split('=')
                        self.properties[strs[0].strip()] = strs[1].strip()
        except Exception:
            print('文件不存在：{}'.format(traceback.print_exc()))

    def has_key(self, key):
        return key in self.properties

    def get(self, key, default_value=''):
        if key in self.properties:
            return self.properties[key]
        return default_value

    def put(self, key, value):
        self.properties[key] = value
        replace_property(self.file_name, key + '.*=.*', key + '=' + str(value), True)


def parse(file_name):
    return Properties(file_name)


def replace_property(file_name, from_regex, to_str, append_on_not_exists=True):
    tmpfile = tempfile.TemporaryFile()

    if os.path.exists(file_name):
        pattern = re.compile(r'' + from_regex)
        found = None
        with open(file_name, encoding='utf-8') as r_open:
            for line in r_open:

                if pattern.search(line) and not line.strip().startswith('#'):
                    found = True

                    line = re.sub(from_regex, to_str, line.replace(' ', ''))

                tmpfile.write(bytes(line, encoding="utf8"))
        if not found and append_on_not_exists:
            tmpfile.write(bytes('\n' + to_str, encoding='utf8'))
        tmpfile.seek(0)

        content = tmpfile.read()

        if os.path.exists(file_name):
            os.remove(file_name)

        w_open = open(file_name, 'wb')
        w_open.write(content)
        w_open.close()

        tmpfile.close()
    else:
        print("file %s not found" % file_name)


if __name__ == "__main__":
    filenName = "test.properties"

    po = parse(filenName)
    po.put('project_name', 'sz-askbob-server')

    # p.load(open('test.properties'))
