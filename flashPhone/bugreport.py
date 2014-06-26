#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from libs import *

svn_path = '/home/jiahuixing/SVN/Bugreport/trunk/'

bug_suffix = '.txt'
tgz_suffix = '.tar.gz'


# noinspection PyMethodMayBeStatic
class Bugreport:
    work_path = ''
    file_name = ''
    txt_name = ''
    tgz_name = ''
    adb_device_list = list()

    def __init__(self):
        adb_permission()

    def adb_devices_list(self):
        adb_device_list = []
        cmd = 'adb devices'
        child = os.popen(cmd)
        for line in child.readlines():
            line = str.strip(line, '\r\n')
            if line:
                tmp = line.split()
                tmp_length = len(tmp)
                if tmp_length == 2:
                    adb_device_list.append(tmp)
        self.adb_device_list = sorted(adb_device_list)

    def get_bugreport(self):
        debug_msg(color_msg('------get_bugreport------', RED))
        if len(self.adb_device_list) > 0:
            for i in xrange(len(self.adb_device_list)):
                device = self.adb_device_list[i][0]
                now = time.strftime('%H_%M_%S')
                tpm = '%s-%s' % (get_date(), now)
                self.file_name = 'bugreport-%s-%s' % (device, tpm)
                self.txt_name = '%s%s' % (self.file_name, bug_suffix)
                cmd = 'adb -s %s bugreport > %s%s' % (device, self.work_path, self.txt_name)
                color_cmd = 'adb -s %s bugreport > %s%s' % (device, self.work_path, color_msg(self.txt_name))
                debug_msg(color_cmd)
                os.system(cmd)
                self.tar_file()
                self.push_tgz_txt()
        else:
            print('adb device not found.')

    # noinspection PyMethodMayBeStatic
    def tar_file(self):
        debug_msg(color_msg('------tar_file------', RED))
        self.tgz_name = '%s%s' % (self.file_name, tgz_suffix)
        cmd = 'tar -zcf %s %s%s' % (self.tgz_name, self.file_name, bug_suffix)
        color_cmd = 'tar -zcf %s %s%s' % (color_msg(self.tgz_name), self.file_name, bug_suffix)
        debug_msg(color_cmd)
        os.system(cmd)

    def push_tgz_txt(self):
        debug_msg(color_msg('------push_tgz------', RED))
        self.mv_file(self.tgz_name, svn_path)
        self.mv_file(self.txt_name, svn_path)

    def mv_file(self, file_name, dir_name):
        cmd = 'sudo mv -f %s %s' % (file_name, dir_name)
        color_cmd = 'sudo mv -f %s %s' % (color_msg(file_name), dir_name)
        debug_msg(color_cmd)
        child = pexpect.spawn(cmd, timeout=5)
        try:
            i = child.expect(':')
            if i == 0:
                child.sendline('1')
                child.expect(pexpect.EOF)
        except pexpect.TIMEOUT:
            print('TIMEOUT')
        finally:
            child.close()

if __name__ == '__main__':
    bug = Bugreport()
    try:
        bug.adb_devices_list()
        bug.get_bugreport()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')