# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from libs import *


# noinspection PyPep8Naming
class device_list:
    def __init__(self):
        adb_permission()


def adb_devices_list():
    adb_device_list = []
    shell_command = 'adb devices'
    child = os.popen(shell_command)
    for line in child.readlines():
        line = str.strip(line, '\r\n')
        if line:
            tmp = line.split()
            tmp_length = len(tmp)
            if tmp_length == 2:
                adb_device_list.append(tmp)
    return sorted(adb_device_list)


def fastboot_devices_list():
    fastboot_devices = []
    shell_command = 'fastboot devices'
    child = os.popen(shell_command)
    for line in child.readlines():
        line = str.strip(line, '\r\n')
        if line:
            tmp = line.split()
            tmp_length = len(tmp)
            if tmp_length == 2:
                fastboot_devices.append(tmp)
    return sorted(fastboot_devices)


def get_product_name(m_device_id):
    m_product_name = ''
    shell_command = 'adb -s %s shell getprop ro.build.product' % m_device_id
    # debug_msg(shell_command)
    child = os.popen(shell_command)
    for line in child.readlines():
        m_product_name = str.strip(line, '\r\n')
    return m_product_name


if __name__ == '__main__':
    dl = device_list()
    adb_s = adb_devices_list()
    if len(adb_s) > 0:
        debug_msg(color_msg('adb devices', GREEN))
        for adb in adb_s:
            device_id = adb[0]
            product_name = get_product_name(device_id)
            debug_msg('device = %s | product = %s' % (color_msg(device_id), color_msg(product_name)))
    else:
        debug_msg(color_msg('no adb device.', RED))
    fastboot_s = fastboot_devices_list()
    if len(fastboot_s) > 0:
        debug_msg(color_msg('fastboot devices', GREEN))
        for fastboot in fastboot_s:
            debug_msg(fastboot)
    else:
        debug_msg(color_msg('no fastboot device.', RED))