__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

import os
import sys


def testArgvs():
    length = len(sys.argv)
    print(length)


def testTryReturn():
    num = 0
    try:
        num = 1
    except KeyboardInterrupt:
        print('wrong')
    return num



num = testTryReturn()
print(type(num))
print(num)