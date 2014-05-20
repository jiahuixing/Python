#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from libs import *

root_path = '/home/jiahuixing'
bug_path = 'bugreport'

bug_suffix = '.txt'
tgz_suffix = '.tar.gz'


class Bugreport:
    work_path = ''
    file_name = ''
    txt_name = ''
    adb_device_list = list()

    def __init__(self):
        self.work_path = '%s/%s/' % (root_path, bug_path)
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
        if len(self.adb_device_list) > 0:
            debug_msg(self.work_path)
            os.chdir(root_path)
            if not os.path.exists(bug_path):
                os.mkdir(bug_path)
            for i in xrange(len(self.adb_device_list)):
                device = self.adb_device_list[i][0]
                now = time.strftime('%H_%M_%S')
                tpm = '%s-%s' % (get_date(), now)
                self.file_name = 'bugreport-%s-%s' % (device, tpm)
                self.txt_name = '%s%s' % (self.file_name, bug_suffix)
                debug_msg(color_msg(self.txt_name))
                cmd = 'adb -s %s bugreport > %s%s' % (device, self.work_path, self.txt_name)
                debug_msg(cmd)
                os.system(cmd)
                self.tar_file()
        else:
            print('adb device not found.')

    # noinspection PyMethodMayBeStatic
    def tar_file(self):
        tgz_name = '%s%s' % (self.file_name, tgz_suffix)
        debug_msg(color_msg(tgz_name))
        os.chdir(self.work_path)
        cmd = 'tar -zcvf %s %s%s' % (tgz_name, self.file_name, bug_suffix)
        debug_msg(cmd)
        os.system(cmd)
        cmd = 'rm -rf %s' % self.txt_name
        debug_msg(cmd)
        os.system(cmd)


if __name__ == '__main__':
    bug = Bugreport()
    bug.adb_devices_list()
    bug.get_bugreport()