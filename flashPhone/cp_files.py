#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from libs import *


valid_suffix = [
    'py',
    'xml',
    'ini',
    'sh',
]

ignore_files = [
    'cp_files.py',
    'flash_phone_test.py',
]


def file_suffix(file_name):
    is_in = 0
    for i in xrange(len(valid_suffix)):
        suffix = valid_suffix[i]
        if str.endswith(file_name, suffix):
            is_in = 1
            break
    return is_in


def cp_files():
    work_path = '/home/jiahuixing/Python/flashPhone'
    termini_path = '/home/jiahuixing/SVN/Tools/trunk'
    os.chdir(work_path)
    for file_name in os.listdir(work_path):
        if file_name not in ignore_files:
            if file_suffix(file_name) == 1:
                debug(file_name)
                cmd = 'sudo cp %s %s' % (file_name, termini_path)
                child = pexpect.spawn(cmd)
                try:
                    i = child.expect('jiahuixing:')
                    if i == 0:
                        cmd = '1\r'
                        child.send(cmd)
                except pexpect.EOF:
                    print('pexpect.EOF')
                except pexpect.TIMEOUT:
                    print('pexpect.TIMEOUT')


cp_files()