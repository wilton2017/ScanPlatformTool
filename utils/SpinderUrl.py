# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     SpinderUrl
   Description :
   Author :       admin
   date：          2020/1/5
-------------------------------------------------
   Change Activity:
                   2020/1/5:
-------------------------------------------------
"""
__author__ = 'admin'

import json
from utils.markjson import test

# url_dict = test['entries']
url_dict = {}
post_list = []
get_list = []
for enter in test['log']['entries']:
    if enter['request']['method'] == 'GET':

        url = enter['request']['url']

        if url not in post_list:
            post_list.append(url)
            print(url)
