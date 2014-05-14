#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

import os
import pexpect


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
    file_or_folder = 0
    if os.path.isdir(file_name):
        if not str.startswith(file_name, '.'):
            is_in = 1
            file_or_folder = 1
    else:
        for i in xrange(len(valid_suffix)):
            suffix = valid_suffix[i]
            if str.endswith(file_name, suffix):
                is_in = 1
                break
    return is_in, file_or_folder


def cp_files():
    work_path = '/home/jiahuixing/Python'
    termini_path = '/home/jiahuixing/SVN/Tools/trunk/'
    os.chdir(work_path)
    for file_name in os.listdir(work_path):
        if file_name not in ignore_files:
            is_in, file_or_folder = file_suffix(file_name)
            if is_in == 1:
                print('------%s------' % file_name)
                cmd = 'sudo cp -r %s %s' % (file_name, termini_path)
                if file_or_folder == 0:
                    child = pexpect.spawn(cmd)
                    try:
                        i = child.expect('jiahuixing:')
                        if i == 0:
                            cmd = '1\r'
                            child.send(cmd)
                            k = 1
                    except pexpect.EOF:
                        print('pexpect.EOF')
                    except pexpect.TIMEOUT:
                        print('pexpect.TIMEOUT')
                else:
                    os.system(cmd)


cp_files()