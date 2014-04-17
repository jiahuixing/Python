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


def test6():
    json_analyse()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def test7():
    print bcolors.OKGREEN + "OK: Install was fininsh" + bcolors.ENDC
    print bcolors.FAIL + "Fail: Not found this file" + bcolors.ENDC


BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def test8(fg=None, bg=None):
    codes = []
    if fg is not None: codes.append('3%d' % fg)
    if bg is not None: codes.append('10%d' % bg)
    debug(codes)
    return '\033[%sm' % ';'.join(codes) if codes else ''


# rrr = test8(WHITE, BLUE) + 'hahahaaha'
# debug(rrr)


import threading

mylock = threading.RLock()
num = 0


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        global num
        while True:
            mylock.acquire()
            print '\nThread(%s) locked, Number: %d' % (self.t_name, num)
            if num >= 4:
                mylock.release()
                print '\nThread(%s) released, Number: %d' % (self.t_name, num)
                break
            num += 1
            print '\nThread(%s) released, Number: %d' % (self.t_name, num)
            mylock.release()


def test():
    thread1 = myThread('A')
    thread2 = myThread('B')
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    test6()
