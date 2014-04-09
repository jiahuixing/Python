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
            if len(self.adb_device_list) == 0:
                debug('wait for 3 seconds.')
                time.sleep(3)

    def root_and_remount(self):
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
                    # debug(cmd)
                    os.system(cmd)

    def flash_phone(self):
        device_list = self.adb_device_list
        debug(device_list)


try:
    op = Operate()
    info = '''
Input num:
1.root_and_remount
    '''
    input_num = input(info)
    if isinstance(input_num, int):
        if input_num == 1:
            op.root_and_remount()
        # elif input_num == 2:
        #     op.push_files()
        else:
            print('Input wrong num:%s.' % input_num)
    else:
        print('Not a num:%s.' % input_num)
except KeyboardInterrupt:
    print('KeyboardInterrupt.')
except IOError:
    print('IOError.')
except NameError:
    print('NameError.')