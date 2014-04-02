__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

from libs import *
from data import *


def test1():
    device_list = get_adb_device_list()
    if device_list:
        root_devices(device_list)
        remount_devices(device_list)


def test2():
    file_path = 'data.xml'
    tag = Tags['push']
    cmd = read_xml_file(file_path, tag)


test2()