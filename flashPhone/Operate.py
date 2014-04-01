# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from libs import *
from data import *


class Operate:
    adb_device_list = []

    def __init__(self):
        debug('init')
        while len(self.adb_device_list) == 0:
            self.adb_device_list = get_adb_device_list()

    def root_remount(self):
        """

        @summary 获取root remount权限
        """
        device_list = self.adb_device_list
        root_devices(device_list)
        remount_devices(device_list)

    def push_files(self):
        device_list = self.adb_device_list
        t_cmd = 'adb -s '
        for device in device_list:
            for c in Push:
                cmd = t_cmd + device + c
                debug(cmd)
                os.system(cmd)

    def flash_phone(self):
        device_list = self.adb_device_list


rm = Operate()
rm.root_remount()
rm.push_files()

