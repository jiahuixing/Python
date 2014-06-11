# !/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

import sys

from other.libs import *


def test1():
    msg = 'hahahahh'
    # msg = color_msg(msg)
    debug_msg(color_msg(msg))


def test2():
    msg = '\033[0;32m%s\033[0m' % 'woshiyansezi'
    debug_msg(msg)


def test3():
    print('哈哈哈哈哈')


def test4():
    arg = str.rstrip(sys.argv[1], '/')
    count = str.count(arg, '/')
    tmp_list = str.split(arg, '/')
    m_version = tmp_list[-1]
    m_folder = tmp_list[-2]
    work_path = str.replace(arg, m_version, '', 1)
    debug_msg(color_msg('arg=%s\ncount=%s\ntmp_list=%s\nm_version=%s\nm_folder=%s\nwork_path=%s\n' % (
        arg, count, tmp_list, m_version, m_folder, work_path)))


test4()