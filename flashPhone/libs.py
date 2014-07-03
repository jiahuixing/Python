# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

import os
import pexpect
import time
# noinspection PyPep8Naming
from xml.etree import ElementTree as ET
import urllib2
import json
# import memcache
import threading


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
    debug_msg(adb_device_list)
    if isinstance(adb_device_list, list):
        for device in adb_device_list:
            debug_msg(device)
            tmp = cmd + device + ' root'
            root_cmd.append(tmp)
        debug_msg(root_cmd)
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
    debug_msg(adb_device_list)
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


def read_xml_file(file_path, tag, attr_key=''):
    """



    @param file_path:
    @param attr_key:
    @param file_path must be a list include file_abs_path and file_name:
    @param tag:
    @copyright http://www.open-open.com/lib/view/open1329403902937.html
    @return command
    """
    command = []
    if isinstance(file_path, list):
        path = file_path[0]
        os.chdir(path)
        file_name = file_path[1]
        debug_msg('file_name=%s,tag=%s,attr_key=%s' % (file_name, tag, attr_key))
        debug_msg('abs=%s' % os.path.abspath(file_name))
        if os.path.exists(file_name):
            root = ET.parse(file_name)
            debug_msg('root=%s' % root)
            tmp_s = root.findall(tag)
            debug_msg('tmp_s=%s' % tmp_s)
            for tmp in tmp_s:
                if isinstance(tmp, ET.Element):
                    # children = tmp.getchildren()
                    emp_dict = dict()
                    # debug('emp_dict=%s' % emp_dict)
                    if tmp.attrib == emp_dict or tmp.attrib['type'] == attr_key:
                        children = list(tmp)
                        for child in children:
                            if isinstance(child, ET.Element):
                                # msg = 'tag:%s,text=%s' % (child.tag, child.text)
                                # debug(msg)
                                tmp_cmd = child.text
                                # debug(tmp_cmd)
                                command.append(tmp_cmd)
        else:
            print('not exists.')
    else:
        print('file_path not list.')
    debug_msg(command)
    return command


def json_analyse():
    url_result = urllib2.urlopen('http://fm.duokanbox.com/category').read()
    debug_msg('url_result=%s' % url_result)
    json_r = json.loads(url_result)
    debug_msg('json_r=%s' % json_r)
    # debug(type(json_r))
    if isinstance(json_r, dict):
        keys = json_r.keys()
        debug_msg('keys=%s' % keys)
        for item in json_r.items():
            # debug(type(item))
            # debug(item)
            # for i in xrange(len(item)):
            debug_msg('%s:%s' % (item[0], item[len(item) - 1]))


def debug_msg(msg, flag=1):
    if flag == 1:
        print('-----------------------------------')
        print(msg)


def adb_permission():
    """

    @summary 获取adb permission
    """
    no_per = 0
    cmd = 'adb devices'
    result = os.popen(cmd)
    for line in result.readlines():
        if 'no permissions' in line:
            no_per = 1
            break
    if no_per == 1:
        debug_msg(color_msg('no permissions', RED))
        cmd = 'su'
        password = '1\r'
        child = pexpect.spawn(cmd, timeout=5)
        try:
            i = child.expect('：')
            if i == 0:
                debug_msg(color_msg('expect :'))
                child.send(password)
                i = child.expect('#')
                if i == 0:
                    debug_msg(color_msg('expect #'))
                    cmd = 'cd /home/jiahuixing/sdk/platform-tools/\r'
                    child.send(cmd)
                    # cmd = 'ls -la\r'
                    # child.send(cmd)
                    debug_msg(color_msg('adb kill-server'))
                    cmd = './adb kill-server\r'
                    child.send(cmd)
                    debug_msg(color_msg('adb start-server'))
                    cmd = './adb devices\r'
                    child.send(cmd)
                    debug_msg(color_msg('exit'))
                    cmd = 'exit\r'
                    child.send(cmd)
        except pexpect.EOF:
            debug_msg('EOF')
        except pexpect.TIMEOUT:
            debug_msg('TIMEOUT')
        finally:
            child.close()


COLOR_START = '\033[0'
COLOR_END = '\033[0m'
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def color_msg(msg, fg=GREEN, bg=None):
    """

    @param msg:
    @param fg:
    @param bg:
    @return:
    """
    color = list()
    if fg is not None:
        color_fg = '3%d' % fg
        # debug('color_fg=%s' % color_fg)
        color.append(color_fg)
    if bg is not None:
        color_bg = '4%d' % bg
        # debug('color_bg=%s' % color_bg)
        color.append(color_bg)
    if len(color) > 0:
        color_str = ';'.join(color)
        # debug(color)
        # debug(color_str)
        msg = '%s%sm%s%s' % (COLOR_START, color_str, msg, COLOR_END)
    # if color == 2:
    # return '%s%s%s%s%s' % (COLOR_START, color_fg, color_bg, msg, COLOR_END)
    return msg


def get_date():
    """


    @return m_date:
    @summary 获取格式日期
    """
    block = '.'
    year, mon, day = time.strftime('%Y'), time.strftime('%m'), time.strftime('%d')
    year = year[-1]
    mon = str(int(mon))
    day = str(int(day))
    m_date = year + block + mon + block + day
    return m_date


class MyThread(threading.Thread):
    def __init__(self, thread_name):
        """

        @param thread_name:
        @see http://www.cnblogs.com/tqsummer/archive/2011/01/25/1944771.html
        """
        threading.Thread.__init__(self, name=thread_name)

    def run(self):
        debug_msg('thread_name=%s' % self.getName())
        super(MyThread, self).run()



