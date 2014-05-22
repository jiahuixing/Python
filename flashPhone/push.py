#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

import os
import sys


PRI_MODELS = [
    'mocha',
]


# noinspection PyMethodMayBeStatic
class Push:
    apk = ''
    adb_device_list = list()
    device_list = list()

    def __init__(self):
        self.init_apk()
        self.adb_device_list = self.get_adb_device_list()

    def init_apk(self):
        if len(sys.argv) > 1:
            self.apk = str.replace(sys.argv[1], '/', '')
        else:
            self.apk = 'Music.apk'

    def get_adb_device_list(self):
        adb_device_list = []
        cmd = 'adb devices'
        result = os.popen(cmd)
        for line in result.readlines():
            line = str.strip(line, '\r\n')
            if line:
                tmp = line.split()
                tmp_length = len(tmp)
                if tmp_length == 2:
                    adb_device_list.append(tmp[0])
        return sorted(adb_device_list)

    def init_devices(self):
        if len(self.adb_device_list) > 0:
            for i in xrange(len(self.adb_device_list)):
                device_id = self.adb_device_list[i]
                print(device_id)
                device = Device(device_id)
                self.device_list.append(device)
        else:
            print('No device.')

    def push_apk(self):
        if len(self.device_list) > 0:
            rm_files = 'Music.*'
            for device in self.device_list:
                shell = 'adb -s %s shell rm %s%s' % (device.device_id, device.push_path, rm_files)
                print('shell=%s' % shell)
                os.system(shell)
                shell = 'adb -s %s push %s %s' % (device.device_id, self.apk, device.push_path)
                print('shell=%s' % shell)
                if os.path.exists(self.apk):
                    os.system(shell)
                    shell = 'adb -s %s reboot' % device.device_id
                    os.system(shell)
                else:
                    print('File not exist.')


class Device:
    device_id = ''
    model = ''
    push_path = ''

    def __init__(self, device_id):
        self.device_id = device_id
        self.get_device_type()
        self.get_push_path()

    def get_device_type(self):
        cmd = 'adb -s %s shell getprop ro.product.name' % self.device_id
        result = os.popen(cmd)
        self.model = result.readline().strip('\n').strip('\r')

    def get_push_path(self):
        if self.model in PRI_MODELS:
            self.push_path = '/system/priv-app/'
        else:
            self.push_path = '/system/app/'


if __name__ == '__main__':
    push = Push()
    push.init_devices()
    push.push_apk()