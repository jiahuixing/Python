# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from libs import *

CONST = {
    'block': ' ',
    'WORK_PATH': '/home/jiahuixing/pytools',
}


class Operate:
    adb_device_list = []

    def __init__(self):
        debug_msg('init')
        adb_permission()
        while len(self.adb_device_list) == 0:
            self.adb_device_list = get_adb_device_list()
            if len(self.adb_device_list) == 0:
                debug_msg('wait for 3 seconds.')
                time.sleep(3)

    def root_and_remount(self):
        """

        @summary 获取root remount权限
        """
        device_list = self.adb_device_list
        root_devices(device_list)
        remount_devices(device_list)


def opr():
    try:
        op = Operate()
        op.root_and_remount()
    except KeyboardInterrupt:
        print('KeyboardInterrupt.')
    except IOError:
        print('IOError.')
    except NameError:
        print('NameError.')


if __name__ == '__main__':
    opr()