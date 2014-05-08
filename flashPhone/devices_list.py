# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from libs import *


# noinspection PyPep8Naming
class device_list:
    def __init__(self):
        adb_permission()

    @staticmethod
    def adb_devices_list():
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
        return sorted(adb_device_list)


    @staticmethod
    def fastboot_devices_list():
        fastboot_devices = []
        cmd = 'fastboot devices'
        child = os.popen(cmd)
        for line in child.readlines():
            line = str.strip(line, '\r\n')
            if line:
                tmp = line.split()
                tmp_length = len(tmp)
                if tmp_length == 2:
                    fastboot_devices.append(tmp)
        return sorted(fastboot_devices)


if __name__ == '__main__':
    dl = device_list()
    adb_s = dl.adb_devices_list()
    if len(adb_s) > 0:
        debug(color_msg('adb devices', GREEN, WHITE))
        for adb in adb_s:
            debug(adb)
    else:
        debug(color_msg('no adb device.', RED, WHITE))
    fastboot_s = dl.fastboot_devices_list()
    if len(fastboot_s) > 0:
        debug(color_msg('fastboot devices', GREEN, WHITE))
        for fastboot in fastboot_s:
            debug(fastboot)
    else:
        debug(color_msg('no fastboot device.', RED, WHITE))