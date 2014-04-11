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
    os.chdir(Tmp_File_Path[0])
    file_path = Tmp_File_Path[1]
    debug(file_path)
    root = ET.parse(file_path)
    commands_tag = 'commands'
    commands_nodes = root.findall(commands_tag)
    debug(type(commands_nodes))
    debug(commands_nodes)
    for commands_node in list(commands_nodes):
        assert isinstance(commands_node, ET.Element)
        debug('tag=%s,attr=%s' % (commands_node.tag, commands_node.attrib))
        command_tag = 'command'
        command_nodes = commands_node.findall(command_tag)
        for command_node in list(command_nodes):
            assert isinstance(command_node, ET.Element)
            debug('tag=%s,attr=%s,text=%s' % (command_node.tag, command_node.attrib, command_node.text))


def test4():
    cmd = read_xml_file(Tmp_File_Path, 'commands', 'push')


def test5():
    init_data()


test5()