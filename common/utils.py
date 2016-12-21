#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 11/13/16.
"""

import uuid
import os
import json
from datetime import datetime, date


class MyException(Exception):
    pass


def get_uuid(type=1):
    if type == 1:
        return uuid.uuid1().hex
    return uuid.uuid4().hex


# ========================================
# 文件操作
# 文件夹的增删改查
def is_dir(path):
    return os.path.exists(path)


def remove_dir(path):
    if not is_dir(path):
        return True
    try:
        os.rmdir(path)
        return True
    except BaseException as e:
        return False


def create_dir(path, create_all=False):
    try:
        if not create_all:
            os.mkdir(path)
        else:
            os.makedirs(path)
        return True
    except:
        return False


# ========================================
# json dumps
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

# ========================================

