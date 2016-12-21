#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 12/20/16
"""


class MyMiddleware(object):
    def process_request(self, request):
        pass

    def process_response(self, request, response):
        return response
