# -*- coding: utf-8 -*-
import re
import sys

__author__ = 'jiahuixing'

from libs import *

work_path = '/home/jiahuixing/Python/flashPhone'


class FlashPhone:
    tgz = '.tgz'
    file_name = ''
    folder = '/home/jiahuixing/roms'
    date = '4.4.26'
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
            debug('KeyboardInterrupt')

    def get_date(self):
        if len(sys.argv) > 1:
            self.date = sys.argv[1]
        else:
            self.date = get_date()

    # noinspection PyMethodMayBeStatic
    def download_tgz(self):
        xml = 'flash_phone_info.xml'
        # date = get_date()
        os.chdir(work_path)
        info_s = list()
        try:
            root = ET.parse(xml)
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
                debug(color_msg('%s:%s' % (i, info_s[i][0]), RED))
            i = input('Pls input ur choice num:')
            if isinstance(i, int):
                main_url = 'http://ota.n.miui.com/ota/'
                page = urllib2.urlopen(main_url, timeout=5).read()
                if self.date in page:
                    td_main_url = main_url + self.date + '/'
                    # debug(td_main_url)
                    choice = info_s[i]
                    rom = choice[0]
                    debug('rom=%s' % rom)
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
            debug('IOError')
        except TypeError:
            debug('TypeError')
        except KeyboardInterrupt:
            debug('KeyboardInterrupt')

    def to_flash_phone(self):
        self.download_tgz()
        self.un_tar()
        self.reboot_phone()
        self.flash_phone()

    # noinspection PyMethodMayBeStatic
    def un_tar(self):
        if self.flag == 1:
            file_name = self.file_name
            cmd = 'tar xvf %s' % file_name
            # debug(cmd)
            os.system(cmd)
            cmd = 'rm -rf %s' % file_name
            # debug(cmd)
            os.system(cmd)
            self.folder = file_name[0:-len('_f0e572b4f6.tgz')]
            # debug('folder=%s' % self.folder)
            self.flag += 1

    def reboot_phone(self):
        if self.flag == 2:
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

    def flash_phone(self):
        if self.flag == 3:
            self.fastboot_device_list = get_fastboot_device_list()
            while len(self.fastboot_device_list) == 0:
                self.fastboot_device_list = get_fastboot_device_list()
                print('Waiting for ur fastboot device.')
                time.sleep(3)
            self.fastboot_device = self.fastboot_device_list[0]
            if os.path.exists(self.folder):
                os.chdir(self.folder)
                flash_all_except = 'flash_all_except_storage.sh'
                # flash_all = 'flash_all.sh'
                if os.path.exists(flash_all_except):
                    cmd = 'chmod a+x %s' % flash_all_except
                    # debug(cmd)
                    os.system(cmd)
                    cmd = './%s' % flash_all_except
                    # debug(cmd)
                    os.system(cmd)
                    os.chdir(work_path)
                    cmd = 'rm -rf %s' % self.folder
                    # debug(cmd)
                    os.system(cmd)


if __name__ == '__main__':
    fp = FlashPhone()