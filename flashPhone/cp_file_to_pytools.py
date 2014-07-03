#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from libs import *


class Info:
    def __init__(self):
        pass

    work_path = '/home/jiahuixing/Python/flashPhone'
    termini_path = '/home/jiahuixing/pytools'

    valid = [
        'py',
        'xml',
        'ini',
    ]

    ignore_files = [
        'cp_file.py',
        'mkdir.py',
        'test.py',
        'cp_file_to_pytools.py',
        'flash_phone_test.py',
    ]


# noinspection PyMethodMayBeStatic
class CpFiles:
    def __init__(self):
        pass

    def valid_or_ignore(self, file_name):
        value = 0
        if file_name in Info.ignore_files:
            value = 0
            return value
        for valid_file_suffix in Info.valid:
            if str.endswith(file_name, valid_file_suffix):
                value = 1
                break
        return value

    def cp_file(self):
        work_path = Info.work_path
        os.chdir(work_path)
        for file_name in os.listdir(work_path):
            if self.valid_or_ignore(file_name) == 1:
                self.do_cp_file(file_name)

    def do_cp_file(self, file_name):
        shell = 'sudo cp -r %s %s' % (file_name, Info.termini_path)
        colored_shell = 'sudo cp -r %s %s' % (color_msg(file_name), color_msg(Info.termini_path, RED))
        debug_msg(colored_shell)
        self.do_pexpect(shell)

    def chown_files(self):
        os.chdir(Info.termini_path)
        shell = 'sudo chown jiahuixing:jiahuixing *'
        colored_shell = color_msg('sudo chown jiahuixing:jiahuixing *')
        debug_msg(colored_shell)
        self.do_pexpect(shell)

    def do_pexpect(self, shell):
        child = pexpect.spawn(shell, timeout=5)
        try:
            i = child.expect('jiahuixing:')
            if i == 0:
                passwd = '1'
                child.sendline(passwd)
                child.expect(pexpect.EOF)
        except pexpect.TIMEOUT:
            print('pexpect.TIMEOUT')
        finally:
            child.close()


if __name__ == '__main__':
    cp = CpFiles()
    cp.cp_file()
    cp.chown_files()
