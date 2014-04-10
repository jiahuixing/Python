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

    def push_file(self, file_name):
        device_list = self.adb_device_list
        work_path = '/home/jiahuixing/music'
        os.chdir(work_path)
        push_command = 'adb -s %s push '
        push_path = ' /data/system/'
        reboot_command = 'adb -s %s reboot'
        for device in device_list:
            if os.path.exists(file_name):
                debug(device)
                debug('file exists.')
                push_cmd = (push_command % device) + file_name + push_path
                reboot_cmd = reboot_command % device
                os.system(push_cmd)
                os.system(reboot_cmd)

    def delete_file(self, file_name):
        delete_command = 'adb -s %s shell rm '
        reboot_command = 'adb -s %s reboot'
        file_path = '/data/system/'
        device_list = self.adb_device_list
        for device in device_list:
            debug(device)
            delete_cmd = (delete_command % device) + file_path + file_name
            reboot_cmd = reboot_command % device
            os.system(delete_cmd)
            os.system(reboot_cmd)

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
    op.root_and_remount()
    info = '''
Input num:
1.push_file:%s
2.delete_file:%s
    '''
    local_file_name = 'account_preview'
    input_num = input(info % (local_file_name, local_file_name))
    if isinstance(input_num, int):
        if input_num == 1:
            op.push_file(local_file_name)
        elif input_num == 2:
            op.delete_file(local_file_name)
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