#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from libs import *


def test1():
    msg = 'hahahahh'
    # msg = color_msg(msg)
    debug_msg(color_msg(msg))


def test2():
    msg = '\033[0;32m%s\033[0m' % 'woshiyansezi'
    debug_msg(msg)


test1()

test2()