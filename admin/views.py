#! /usr/bin/python
# -*- coding:utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse


def login(request):
    request.session.set('test','hello world')
    return HttpResponse(u'hello')


def user_manage(requst):
    return Http404(u'url 参数错误')
