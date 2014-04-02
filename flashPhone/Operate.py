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
        file_path = File_Path
        tag = Tags['push']
        commands = read_xml_file(file_path, tag)
        if len(commands) > 0:
            for device in device_list:
                for command in commands:
                    cmd = command % device
                    debug(cmd)
                    os.system(cmd)

    def flash_phone(self):
        device_list = self.adb_device_list
        debug(device_list)


rm = Operate()
rm.root_remount()
rm.push_files()
