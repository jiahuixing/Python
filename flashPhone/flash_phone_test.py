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
    file_path = File_Path
    tag = Tags['push']
    cmd = read_xml_file(file_path, tag)


def test3():
    file_path = Tmp_File_Path[1]
    debug(file_path)
    root = ET.parse(file_path)
    tag = 'command'
    nodes = root.findall(tag)
    debug(type(nodes))
    debug(nodes)
    for node in list(nodes):
        assert isinstance(node, ET.Element)
        debug('tag=%s,attr=%s' % (node.tag, node.attrib))
        # for key in Attr_s.keys():
        #     attr = Attr_s[key]
        #     debug('attr=%s' % attr)


test3()