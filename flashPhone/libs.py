# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

import os
import time


def get_device_list():
    device_list = []
    cmd = 'adb devices'
    result = os.popen(cmd)
    for line in result.readlines():
        line = str.strip(line, '\r\n')
        if line:
            tmp = line.split()
            tmp_length = len(tmp)
            if tmp_length == 2:
                # print(tmp)
                device_list.append(tmp[0])
    print(device_list)
    return device_list


def root_devices():
    device_list = get_device_list()
    cmd = 'adb -s '
    root_cmd = []
    # print(type(device_list))
    if isinstance(device_list, list):
        if len(device_list) != 0:
            for device in device_list:
                # print(device)
                tmp = cmd + device + ' root'
                root_cmd.append(tmp)
            print(root_cmd)
        else:
            print('device_list len=0')
    else:
        print('not ins')

    if len(root_cmd) != 0:
        for r_cmd in root_cmd:
            os.system(r_cmd)


def remount_devices():
    device_list = get_device_list()
    cmd = 'adb -s '
    succeeded = 'remount succeeded'
    remount_cmd = []
    # print(type(device_list))
    if isinstance(device_list, list):
        if len(device_list) != 0:
            for device in device_list:
                # print(device)
                tmp = cmd + device + ' remount'
                remount_cmd.append(tmp)
            print(remount_cmd)
        else:
            print('device_list len=0')
    else:
        print('not ins')

    if len(remount_cmd) != 0:
        for r_cmd in remount_cmd:
            i = 0
            while i != 1:
                remount_result = os.popen(r_cmd)
                for line in remount_result.readlines():
                    # print('line=%s' % line)
                    if succeeded in line:
                        print('succeeded')
                        i = 1
                        break
                if i != 1:
                    print('wait 3 seconds.')
                    time.sleep(3)