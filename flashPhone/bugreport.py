#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from libs import *


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
        for i in xrange(self.adb_device_list):
            device = self.adb_device_list[i][0]
            now = time.strftime('%H_%M_%S')
            tpm = '%s_%s' % (get_date(), now)
            file_path = '/home/jiahuixing/bugreport/'
            file_name = '%s%s-%s' % (file_path, device, tpm)
            cmd = 'adb -s %s bugreport > %s' % (device, file_name)
            debug(color_msg('cmd'))
            os.system(cmd)


if __name__ == '__main__':
    bug = Bugreport()
    bug.adb_devices_list()
    bug.get_bugreport()