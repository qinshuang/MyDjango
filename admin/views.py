#! /usr/bin/python
# -*- coding:utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse


def login(request):
    return HttpResponse(u'hello')


def index(request):
    return render(request, 'index.html')


def user_manage(request):
    return render(request, 'index.html')
