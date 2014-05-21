#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from libs import *

# root_path = '/home/jiahuixing'
# bug_path = 'bugreport'
svn_path = '/home/jiahuixing/SVN/Bugreport/trunk/'

bug_suffix = '.txt'
tgz_suffix = '.tar.gz'


class Bugreport:
    work_path = ''
    file_name = ''
    txt_name = ''
    tgz_name = ''
    adb_device_list = list()

    def __init__(self):
        # self.work_path = '%s/%s/' % (root_path, bug_path)
        adb_permission()

    def adb_devices_list(self):
        adb_device_list = []
        cmd = 'adb devices'
        child = os.popen(cmd)
        for line in child.readlines():
            line = str.strip(line, '\r\n')
            if line:
                tmp = line.split()
                tmp_length = len(tmp)
                if tmp_length == 2:
                    adb_device_list.append(tmp)
        self.adb_device_list = sorted(adb_device_list)

    def get_bugreport(self):
        debug_msg(color_msg('------get_bugreport------', RED))
        if len(self.adb_device_list) > 0:
            # debug_msg(self.work_path)
            # os.chdir(root_path)
            # if not os.path.exists(bug_path):
            #     os.mkdir(bug_path)
            for i in xrange(len(self.adb_device_list)):
                device = self.adb_device_list[i][0]
                now = time.strftime('%H_%M_%S')
                tpm = '%s-%s' % (get_date(), now)
                self.file_name = 'bugreport-%s-%s' % (device, tpm)
                self.txt_name = '%s%s' % (self.file_name, bug_suffix)
                # debug_msg(color_msg(self.txt_name))
                cmd = 'adb -s %s bugreport > %s%s' % (device, self.work_path, self.txt_name)
                color_cmd = 'adb -s %s bugreport > %s%s' % (device, self.work_path, color_msg(self.txt_name))
                debug_msg(color_cmd)
                os.system(cmd)
                self.tar_file()
                self.push_tgz()
        else:
            print('adb device not found.')

    # noinspection PyMethodMayBeStatic
    def tar_file(self):
        debug_msg(color_msg('------tar_file------', RED))
        self.tgz_name = '%s%s' % (self.file_name, tgz_suffix)
        # debug_msg(color_msg(self.tgz_name))
        # os.chdir(self.work_path)
        # cmd = 'tar -zcvf %s %s%s' % (self.tgz_name, self.file_name, bug_suffix)
        # color_cmd = 'tar -zcvf %s %s%s' % (color_msg(self.tgz_name), self.file_name, bug_suffix)
        cmd = 'tar -zcf %s %s%s' % (self.tgz_name, self.file_name, bug_suffix)
        color_cmd = 'tar -zcf %s %s%s' % (color_msg(self.tgz_name), self.file_name, bug_suffix)
        debug_msg(color_cmd)
        os.system(cmd)
        cmd = 'rm -rf %s' % self.txt_name
        color_cmd = 'rm -rf %s' % color_msg(self.txt_name)
        debug_msg(color_cmd)
        os.system(cmd)

    def push_tgz(self):
        debug_msg(color_msg('------push_tgz------', RED))
        cmd = 'sudo cp -rf %s %s' % (self.tgz_name, svn_path)
        color_cmd = 'sudo cp -rf %s %s' % (color_msg(self.tgz_name), svn_path)
        debug_msg(color_cmd)
        child = pexpect.spawn(cmd, timeout=5)
        try:
            i = child.expect(':')
            if i == 0:
                child.sendline('1')
                child.expect(pexpect.EOF)
        except pexpect.TIMEOUT:
            print('TIMEOUT')
        finally:
            child.close()
            cmd = 'rm -rf %s' % self.tgz_name
            color_cmd = 'rm -rf %s' % color_msg(self.tgz_name)
            debug_msg(color_cmd)
            os.system(cmd)


if __name__ == '__main__':
    bug = Bugreport()
    try:
        bug.adb_devices_list()
        bug.get_bugreport()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')