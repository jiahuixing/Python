#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

import os
import pexpect

from libs import *


valid_suffix = [
    'py',
    'xml',
    'ini',
    'sh',
]

ignore_files = [
    'cp_file.py',
    'mkdir.py',
    'test.py',
]


def file_suffix(file_name):
    is_in = 0
    if os.path.isdir(file_name):
        if not str.startswith(file_name, '.'):
            is_in = 1
    else:
        for i in xrange(len(valid_suffix)):
            suffix = valid_suffix[i]
            if str.endswith(file_name, suffix):
                is_in = 1
                break
    return is_in


def cp_file():
    work_path = '/home/jiahuixing/Python/gen_url'
    termini_path = '/home/jiahuixing/SVN/Friday/trunk/'
    os.chdir(work_path)
    for file_name in os.listdir(work_path):
        if file_name not in ignore_files:
            is_in = file_suffix(file_name)
            if is_in == 1:
                file_name = color_msg(file_name)
                cmd = 'sudo cp -rf %s %s' % (file_name, termini_path)
                print('cmd = %s' % cmd)
                # if file_or_folder == 0:
                child = pexpect.spawn(cmd)
                try:
                    i = child.expect('jiahuixing:')
                    if i == 0:
                        # print('i=%s' % i)
                        cmd = '1'
                        child.sendline(cmd)
                except pexpect.EOF:
                    print('pexpect.EOF')
                except pexpect.TIMEOUT:
                    print('pexpect.TIMEOUT')
                    # else:
                    #     os.system(cmd)


cp_file()
