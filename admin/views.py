#! /usr/bin/python
# -*- coding:utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse


def login(request):
    return HttpResponse(u'hello')


def index(request):
    return render(request, 'index.html')


def sign_in(request):
    """
    注册
    :param request:
    :return:
    """
    if request.method == 'GET':
        pass
        return
    user_name = request.POST.get('user_name', None)
    password = request.POST.get('password', None)


def user_manage(request):
    return render(request, 'index.html')
