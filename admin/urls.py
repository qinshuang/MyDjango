#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 12/19/16
"""
from django.conf.urls import url
from admin.views import *

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^user_manage/$', user_manage, name='user_manage'),
]
