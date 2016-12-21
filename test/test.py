#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 12/19/16
"""

from django.test import SimpleTestCase

from common.utils import *


class CommonUtilsUnitTest(SimpleTestCase):
    def test_get_uuid(self):
        print 'uuid1:%s' % get_uuid(0)
        print 'uuid4:%s' % get_uuid()

    def test_is_dir(self):
        self.assertEqual(is_dir('/tmp'), True)
        self.assertEqual(is_dir('/tmp1'), False)

    def test_create_and_delete_dir(self):
        self.assertEqual(create_dir('/tmp/testdir/'), True)
        self.assertEqual(is_dir('/tmp/testdir/'), True)
        self.assertEqual(remove_dir('/tmp/testdir/'), True)
        self.assertEqual(is_dir('/tmp/testdir/'), False)

        self.assertEqual(create_dir('/tmp/testdir/testdir/testdir/', create_all=True), True)
        self.assertEqual(is_dir('/tmp/testdir/testdir/testdir/'), True)
        self.assertEqual(remove_dir('/tmp/testdir/testdir/testdir/'), True)
        self.assertEqual(is_dir('/tmp/testdir/testdir/testdir/'), False)
        self.assertEqual(remove_dir('/tmp/testdir/testdir/'), True)
        self.assertEqual(is_dir('/tmp/testdir/testdir/'), False)
        self.assertEqual(remove_dir('/tmp/testdir/'), True)
        self.assertEqual(is_dir('/tmp/testdir/'), False)

    def test_data_json(self):
        import json
        import datetime
        print json.dumps(dict(a=datetime.datetime.now()),cls=CJsonEncoder)
