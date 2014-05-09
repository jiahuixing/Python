#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from libs import *

root_path = '/home/jiahuixing'
bug_path = 'bugreport'


class Bugreport:
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
        work_path = '%s/%s/' % (root_path, bug_path)
        debug(work_path)
        os.chdir(root_path)
        if not os.path.exists(bug_path):
            os.mkdir(bug_path)
        for i in xrange(len(self.adb_device_list)):
            device = self.adb_device_list[i][0]
            now = time.strftime('%H_%M_%S')
            tpm = '%s_%s' % (get_date(), now)
            name = 'bugreport-%s-%s' % (device, tpm)
            bug_suffix = '.txt'
            txt_name = '%s%s' % (name, bug_suffix)
            debug(color_msg(txt_name))
            cmd = 'adb -s %s bugreport > %s%s' % (device, work_path, txt_name)
            debug(cmd)
            os.system(cmd)
            tgz_suffix = '.tar.gz'
            tgz_name = '%s%s' % (name, tgz_suffix)
            debug(color_msg(tgz_name))
            os.chdir(work_path)
            cmd = 'tar -zcvf %s %s%s' % (tgz_name, name, bug_suffix)
            debug(cmd)
            os.system(cmd)
            cmd = 'rm -rf %s' % txt_name
            debug(cmd)
            os.system(cmd)


if __name__ == '__main__':
    bug = Bugreport()
    bug.adb_devices_list()
    bug.get_bugreport()