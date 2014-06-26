#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

import os
import pexpect

from flashPhone.libs import color_msg, debug_msg


valid_suffix = [
    'py',
    'xml',
    'ini',
    'sh',
]

ignore_files = [
    'flash_phone_test.py',
]


def file_suffix(file_name):
    is_in = 0
    file_or_folder = 0
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


def cp_files():
    work_path = '/home/jiahuixing/Python'
    termini_path = '/home/jiahuixing/SVN/Tools/trunk/'
    os.chdir(work_path)
    for file_name in os.listdir(work_path):
        if file_name not in ignore_files:
            is_in = file_suffix(file_name)
            if is_in == 1:
                do_cp_file(file_name, termini_path)


def do_cp_file(file_name, path):
    cmd = 'sudo cp -rf %s %s' % (file_name, path)
    color_cmd = 'sudo cp -rf %s %s' % (color_msg(file_name), path)
    debug_msg('cmd = %s' % color_cmd)
    child = pexpect.spawn(cmd)
    try:
        i = child.expect('jiahuixing:')
        if i == 0:
            cmd = '1'
            child.sendline(cmd)
            child.expect(pexpect.EOF)
    except pexpect.TIMEOUT:
        print('pexpect.TIMEOUT')
    finally:
        child.close()


cp_files()