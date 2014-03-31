__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

from tmp_libs import *


def test1():
    m_folder = sys.argv[1]
    for root, dirs, files in os.walk(m_folder):
        for file_name in files:
            print(file_name)
            a_version = get_android_version(file_name)
            print('a_version=%s' % a_version)


test1()


