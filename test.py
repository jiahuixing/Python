__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

from my_libs import *


def test1():
    m_folder = sys.argv[1]
    for root, dirs, files in os.walk(m_folder):
        for file_name in files:
            print(file_name)
            get_dev_type(file_name)


test1()