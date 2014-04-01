# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

import os
import time


def get_adb_device_list():
    """


    @return adb_device_list:
    @summary 获取adb devices list
    """
    adb_device_list = []
    cmd = 'adb devices'
    result = os.popen(cmd)
    for line in result.readlines():
        line = str.strip(line, '\r\n')
        if line:
            tmp = line.split()
            tmp_length = len(tmp)
            if tmp_length == 2:
                # print(tmp)
                adb_device_list.append(tmp[0])
                # debug(device_list)
        # debug(adb_device_list)
    # debug(sorted(adb_device_list))
    return sorted(adb_device_list)


def get_fastboot_device_list():
    """


    @return fastboot_device_list:
    @summary 获取fastboot device list
    """
    fastboot_device_list = []
    cmd = 'fastboot devices'
    result = os.popen(cmd)
    for line in result.readlines():
        line = str.strip(line, '\r\n')
        if line:
            tmp = line.split()
            tmp_length = len(tmp)
            if tmp_length == 2:
                # print(tmp)
                fastboot_device_list.append(tmp[0])
                # debug(device_list)
    return sorted(fastboot_device_list)


def root_devices(adb_device_list):
    """
    @param adb_device_list
    @summary 获取device的adb root权限

    """
    cmd = 'adb -s '
    root_cmd = []
    debug(adb_device_list)
    if isinstance(adb_device_list, list):
        for device in adb_device_list:
            debug(device)
            tmp = cmd + device + ' root'
            root_cmd.append(tmp)
        debug(root_cmd)
    else:
        print('not ins')

    if len(root_cmd) != 0:
        for r_cmd in root_cmd:
            os.system(r_cmd)


def remount_devices(adb_device_list):
    """
    @param adb_device_list
    @summary 获取device的adb remount权限

    """
    cmd = 'adb -s '
    succeeded = 'remount succeeded'
    remount_cmd = []
    debug(adb_device_list)
    if isinstance(adb_device_list, list):
        for device in adb_device_list:
            # print(device)
            tmp = cmd + device + ' remount'
            remount_cmd.append(tmp)
        print(remount_cmd)
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


def debug(msg, flag=1):
    if flag == 1:
        print(msg)