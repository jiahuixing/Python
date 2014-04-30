#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
import re
import sys

__author__ = 'jiahuixing'

from libs import *

WORK_PATH = '/home/jiahuixing/Python/flashPhone'


class FlashPhone:
    file_name = ''
    folder = ''
    date = ''
    xml = ''

    adb_device = ''
    fastboot_device = ''
    adb_device_list = list()
    fastboot_device_list = list()

    flag = 0

    def __init__(self):
        try:
            self.get_date()
            self.to_flash_phone()
        except KeyboardInterrupt:
            print('KeyboardInterrupt')

    def get_date(self):
        if len(sys.argv) > 1:
            self.date = sys.argv[1]
        else:
            self.date = get_date()
        if self.date > '4.4.28':
            self.xml = 'flash_phone_info.xml'
        else:
            self.xml = 'tmp_flash_phone_info.xml'

    # noinspection PyMethodMayBeStatic
    def download_tgz(self):
        msg = 'download_tgz'
        print(color_msg(msg, GREEN, WHITE))
        os.chdir(WORK_PATH)
        info_s = list()
        try:
            root = ET.parse(self.xml)
            if root:
                tag = 'device'
                contents = root.findall(tag)
                for content in contents:
                    tmp = list()
                    if isinstance(content, ET.Element):
                        children = list(content)
                        # debug(children)
                        for child in children:
                            if isinstance(child, ET.Element):
                                # debug(color_msg('tag:%s,text:%s' % (child.tag, child.text)))
                                tmp.append(child.text)
                        tmp[1] = tmp[1] % (tmp[0], self.date)
                        # debug(tmp)
                    info_s.append(tmp)
            # debug(color_msg(info_s))
            for i in xrange(len(info_s)):
                print(color_msg('%s:%s' % (i, info_s[i][0]), RED))
            i = input('Pls input ur choice num:')
            if isinstance(i, int):
                main_url = 'http://ota.n.miui.com/ota/'
                page = urllib2.urlopen(main_url, timeout=5).read()
                if self.date in page:
                    td_main_url = main_url + self.date + '/'
                    # debug(td_main_url)
                    choice = info_s[i]
                    rom = choice[0]
                    print('rom=%s' % rom)
                    pat = r'%s' % choice[1]
                    # debug('rom=%s,pat=%s' % (rom, pat))
                    page = urllib2.urlopen(td_main_url, timeout=5).read()
                    pattern = re.compile(pat)
                    # debug('pattern=%s' % pattern)
                    f_result = re.findall(pattern, page)
                    if f_result:
                        tgz_name = list(set(f_result))[0]
                        # debug('tgz_name=%s' % tgz_name)
                        td_tgz_url = td_main_url + tgz_name
                        # debug('td_tgz_url=%s' % td_tgz_url)
                        cmd = 'wget %s' % td_tgz_url
                        # debug(cmd)
                        os.system(cmd)
                        self.file_name = tgz_name
                        if os.path.exists(self.file_name):
                            self.flag += 1
                    else:
                        print('%s file not find on the site.' % self.date)
        except IOError:
            print('IOError')
        except TypeError:
            print('TypeError')
        except KeyboardInterrupt:
            print('KeyboardInterrupt')

    def to_flash_phone(self):
        self.download_tgz()
        self.un_tar()
        self.reboot_phone()
        self.flash_phone()

    # noinspection PyMethodMayBeStatic
    def un_tar(self):
        if self.flag == 1:
            msg = 'un_tar'
            print(color_msg(msg, GREEN, WHITE))
            file_name = self.file_name
            cmd = 'tar xvf %s' % file_name
            # debug(cmd)
            os.system(cmd)
            cmd = 'rm -rf %s' % file_name
            # debug(cmd)
            debug(color_msg('rm tgz.', RED, WHITE))
            os.system(cmd)
            self.folder = file_name[0:-len('_f0e572b4f6.tgz')]
            # debug('folder=%s' % self.folder)
            self.flag += 1

    def reboot_phone(self):
        if self.flag == 2:
            msg = 'reboot_phone'
            print(color_msg(msg, GREEN, WHITE))
            self.adb_device_list = get_adb_device_list()
            while len(self.adb_device_list) == 0:
                self.adb_device_list = get_adb_device_list()
                print('Waiting for ur adb device.')
                time.sleep(3)
            self.adb_device = self.adb_device_list[0]
            cmd = 'adb -s %s reboot bootloader' % self.adb_device
            # debug(cmd)
            os.system(cmd)
            self.flag += 1
            time.sleep(3)

    def flash_phone(self):
        if self.flag == 3:
            try:
                msg = 'flash_phone'
                print(color_msg(msg, GREEN, WHITE))
                self.fastboot_device_list = get_fastboot_device_list()
                while len(self.fastboot_device_list) == 0:
                    self.fastboot_device_list = get_fastboot_device_list()
                    print('Waiting for ur fastboot device.')
                    time.sleep(3)
                self.fastboot_device = self.fastboot_device_list[0]
                if os.path.exists(self.folder):
                    sh_files = list()
                    abs_folder = os.path.abspath(self.folder)
                    # debug(abs_folder)
                    # debug(os.listdir(abs_folder))
                    for file_name in os.listdir(abs_folder):
                        if file_name.endswith('.sh'):
                            sh_files.append(file_name)
                    # debug(sh_files)
                    for i in xrange(len(sh_files)):
                        print(color_msg('%s:%s' % (i, sh_files[i]), RED, WHITE))
                    i = input('Pls input ur choice num:')
                    if isinstance(i, int):
                        if i < len(sh_files):
                            flash_script = sh_files[i]
                            debug(color_msg('flash_script=%s' % flash_script, RED, WHITE))
                            os.chdir(self.folder)
                            if os.path.exists(flash_script):
                                cmd = 'chmod a+x %s' % flash_script
                                # debug(cmd)
                                os.system(cmd)
                                cmd = './%s' % flash_script
                                # debug(cmd)
                                os.system(cmd)
            except OSError:
                print('OSError')
            finally:
                os.chdir(WORK_PATH)
                cmd = 'rm -rf %s' % self.folder
                # debug(cmd)
                debug(color_msg('rm folder.', RED, WHITE))
                os.system(cmd)


if __name__ == '__main__':
    fp = FlashPhone()