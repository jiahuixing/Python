__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

from libs import *


def test():
    device_list = get_device_list()
    if device_list:
        root_devices()
        remount_devices()


test()
