# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

File_Path = [
    '/home/jiahuixing/Python/flashPhone/',
    'data.xml',
]

Tmp_File_Path = [
    '/home/jiahuixing/Python/flashPhone/',
    'data_tmp.xml',
]

tags = [
    'account_preview',
    'apk'
]

Tags = dict()

Attrs = dict()


def init_data():
    for tag in tags:
        print(tag)
        Tags[tag] = tag
    print(Tags)