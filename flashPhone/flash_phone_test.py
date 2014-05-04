import re
import sys

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


def test9():
    msg = color_msg('hahaha')
    debug(msg)


import threading

mylock = threading.RLock()
num = 0


class My_Thread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.setName(name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print '\nThread(%s) locked, Number: %d' % (self.getName(), num)
            if num >= 4:
                mylock.release()
                print '\nThread(%s) released, Number: %d' % (self.getName(), num)
                break
            num += 1
            print '\nThread(%s) released, Number: %d' % (self.getName(), num)
            mylock.release()


def test():
    thread1 = My_Thread('A')
    thread2 = My_Thread('B')
    thread1.start()
    thread2.start()


def test10():
    cmd = 'su'
    password = '1\r'
    child = pexpect.spawn(cmd, timeout=5)
    try:
        i = child.expect(':')
        debug('i=%s' % i)
        if i == 0:
            child.send(password)
            i = child.expect('#')
            debug('i=%s' % i)
            if i == 0:
                cmd = 'cd /home/jiahuixing/sdk/platform-tools/\r'
                child.send(cmd)
                cmd = 'ls -la\r'
                child.send(cmd)
                cmd = './adb kill-server\r'
                child.send(cmd)
                cmd = './adb devices\r'
                child.send(cmd)
                cmd = 'exit\r'
                child.send(cmd)
    except pexpect.EOF:
        debug('pexpect.EOF')
        child.close()
    except pexpect.TIMEOUT:
        debug('pexpect.TIMEOUT')
        child.close()


def test11():
    debug(len(sys.argv))
    debug(sys.argv[1])


def test12():
    pat = r'%s_%s_4\.[0-9]{1}_cn_[a-z0-9]{10}\.tgz' % ('cancro_images', '4.4.29')
    debug(pat)
    pattern = re.compile(pat)
    page = urllib2.urlopen('http://ota.n.miui.com/ota/4.4.29').read()
    find = re.findall(pattern, page)
    debug(list(set(find)))


def compare_date(date1, date2):
    dt1 = str.split(date1, '.')
    dt2 = str.split(date2, '.')
    for i in xrange(len(dt1)):
        tmp = int(dt1[i])
        dt1.pop(i)
        # noinspection PyTypeChecker
        dt1.insert(i, tmp)
    for j in xrange(len(dt2)):
        tmp = int(dt2[j])
        dt2.pop(j)
        # noinspection PyTypeChecker
        dt2.insert(j, tmp)
    debug(dt1)
    debug(dt2)
    if dt1[0] > dt2[0]:
        result = 1
    elif dt1[0] == dt2[0]:
        if dt1[1] > dt2[1]:
            result = 1
        elif dt1[1] == dt2[1]:
            if dt1[2] > dt2[2]:
                result = 1
            else:
                result = 2
        else:
            result = 2
    else:
        result = 2

    return result


def test13():
    # date = get_date()
    date = '4.4.3'
    compare = '4.4.28'
    cmp_result = compare_date(date, compare)
    debug('cmp_result=%s' % cmp_result)
    if cmp_result == 1:
        debug('%s > %s' % (date, compare))
    else:
        debug('%s > %s' % (compare, date))


if __name__ == '__main__':
    test13()
