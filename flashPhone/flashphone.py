#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
import re
import sys

__author__ = 'jiahuixing'

from libs import *


# noinspection PyClassHasNoInit
class FlashInfo:
    work_path = '/home/jiahuixing/pytools'
    main_url = 'http://ota.n.miui.com/ota/'
    Sign = [
        'http://ota.n.miui.com',
        '.tgz',
    ]


class FlashPhone:
    tgz_name = ''
    folder = ''
    date = ''
    xml = ''

    adb_device = ''
    product_name = ''
    fastboot_device = ''
    adb_device_list = list()
    fastboot_device_list = list()

    info_s = list()

    sign = 0
    flag = 0

    def __init__(self):
        self.get_date()

    def get_date(self):
        if len(sys.argv) > 1:
            self.date = sys.argv[1]
        else:
            self.date = get_date()
        if FlashInfo.Sign[0] in self.date and FlashInfo.Sign[1] in self.date:
            self.sign = 1
        else:
            dev = self.dev_or_stable(self.date)
            debug_msg(color_msg('dev = %s' % dev))
            if self.dev_or_stable(self.date) == 1:
                tmp_date = '4.4.28'
                t_tmp_date = '4.3.8'
                cmp_result = self.compare_date(self.date, tmp_date)
                if cmp_result == 1:
                    self.xml = 'flash_phone_info.xml'
                else:
                    cmp_result = self.compare_date(self.date, t_tmp_date)
                    if cmp_result == 1:
                        self.xml = 'tmp_flash_phone_info.xml'
                    else:
                        self.xml = 't_tmp_flash_phone_info.xml'
            else:
                self.xml = 't_tmp_flash_phone_info.xml'

    # noinspection PyMethodMayBeStatic
    def dev_or_stable(self, file_name):
        file_name = str.lower(file_name)
        dev_version = r'[0-9]{1}\.[0-9]{1,2}\.[0-9]{1,2}'
        stable_version = r'[a-z]{3,7}[0-9]{1,2}\.[0-9]{1,2}'
        pattern_dev = re.compile(dev_version)
        pattern_stable = re.compile(stable_version)
        dev_search_result = re.findall(pattern_dev, file_name)
        stable_search_result = re.findall(pattern_stable, file_name)
        if dev_search_result:
            dev = 1
        elif stable_search_result:
            dev = 2
        else:
            dev = 0
        return dev

    @staticmethod
    def compare_date(date1, date2):
        abc = r'[a-zA-Z]{1}'
        pattern = re.compile(abc)
        find = re.findall(pattern, date1)
        if len(find) > 0:
            result = 2
        else:
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

    def get_info(self):
        debug_msg('date=%s,xml=%s' % (self.date, self.xml))
        info_s = list()
        root = ET.parse(self.xml)
        if root:
            tag = 'device'
            contents = root.findall(tag)
            for content in contents:
                tmp = list()
                if isinstance(content, ET.Element):
                    children = list(content)
                    for child in children:
                        if isinstance(child, ET.Element):
                            tmp.append(child.text)
                    tmp[1] = tmp[1] % (tmp[0], self.date)
                info_s.append(tmp)
        self.info_s = info_s

    # noinspection PyMethodMayBeStatic
    def download_tgz(self):
        msg = 'download_tgz'
        os.chdir(FlashInfo.work_path)
        print(color_msg(msg, GREEN))
        if self.sign == 0:
            self.get_info()
            info_s = self.info_s
            for i in xrange(len(info_s)):
                print(color_msg('%s:%s' % (i, info_s[i][0]), RED))
            i = input('Pls input ur choice num:')
            if isinstance(i, int):
                main_url = FlashInfo.main_url
                page = urllib2.urlopen(main_url, timeout=5).read()
                if self.date in page:
                    td_main_url = main_url + self.date + '/'
                    choice = info_s[i]
                    rom = choice[0]
                    pat = r'%s' % choice[1]
                    debug_msg(color_msg('rom=%s' % rom))
                    debug_msg(color_msg('pat=%s' % pat))
                    page = urllib2.urlopen(td_main_url, timeout=5).read()
                    pattern = re.compile(pat)
                    f_result = re.findall(pattern, page)
                    if f_result:
                        tgz_name = list(set(f_result))[0]
                        td_tgz_url = td_main_url + tgz_name
                        cmd = 'wget %s' % td_tgz_url
                        os.system(cmd)
                        self.tgz_name = tgz_name
                        if os.path.exists(self.tgz_name):
                            self.flag += 1
                    else:
                        print('%s file not find on the site.' % self.date)
        else:
            cmd = 'wget %s' % self.date
            os.system(cmd)
            tgz_name = str.split(self.date, '/')[-1]
            self.tgz_name = tgz_name
            if os.path.exists(self.tgz_name):
                self.flag += 1

    # noinspection PyMethodMayBeStatic
    def un_tar(self):
        if self.flag == 1:
            msg = 'un_tar'
            print(color_msg(msg, GREEN))
            cmd = 'tar xvf %s' % self.tgz_name
            os.system(cmd)
            self.folder = self.tgz_name[0:-len('_f0e572b4f6.tgz')]
            self.flag += 1

    # noinspection PyMethodMayBeStatic
    def input_msg(self, input_type):
        if len(self.adb_device_list) > 0:
            input_msg = 'Pls input ur choice num:'
            i = input(input_msg)
            if isinstance(i, int):
                pass
            if input_type == 0:
                pass
            elif input_type == 1:
                pass

    # noinspection PyMethodMayBeStatic
    def get_adb_device_type(self):
        product_name = None
        if self.adb_device != '':
            cmd = 'adb -s %s shell getprop ro.product.name' % self.adb_device
            result = os.popen(cmd)
            product_name = result.readline().strip('\n').strip('\r')
        return product_name

    def reboot_phone(self):
        if self.flag == 2:
            msg = 'reboot_phone'
            print(color_msg(msg, GREEN))
            self.fastboot_device_list = get_fastboot_device_list()
            if len(self.fastboot_device_list) > 0:
                self.flag += 1
            else:
                self.adb_device_list = get_adb_device_list()
                while len(self.adb_device_list) == 0:
                    self.adb_device_list = get_adb_device_list()
                    print('Waiting for ur adb device.')
                    time.sleep(3)
                self.adb_device = self.adb_device_list[0]
                cmd = 'adb -s %s reboot bootloader' % self.adb_device
                os.system(cmd)
                self.flag += 1
                time.sleep(3)

    def flash_phone(self):
        if self.flag == 3:
            msg = 'flash_phone'
            print(color_msg(msg, GREEN))
            self.fastboot_device_list = get_fastboot_device_list()
            while len(self.fastboot_device_list) == 0:
                self.fastboot_device_list = get_fastboot_device_list()
                print('Waiting for ur fastboot device.')
                time.sleep(3)
            self.fastboot_device = self.fastboot_device_list[0]
            if os.path.exists(self.folder):
                sh_files = list()
                abs_folder = os.path.abspath(self.folder)
                for file_name in os.listdir(abs_folder):
                    if file_name.endswith('.sh'):
                        sh_files.append(file_name)
                for i in xrange(len(sh_files)):
                    print(color_msg('%s:%s' % (i, sh_files[i]), RED))
                i = input('Pls input ur choice num:')
                if isinstance(i, int):
                    if i < len(sh_files):
                        flash_script = sh_files[i]
                        debug_msg(color_msg('flash_script=%s' % flash_script, RED))
                        os.chdir(self.folder)
                        if os.path.exists(flash_script):
                            cmd = 'chmod a+x %s' % flash_script
                            os.system(cmd)
                            cmd = './%s' % flash_script
                            debug_msg(color_msg(cmd))
                            os.system(cmd)

    def delete_file(self):
        os.chdir(FlashInfo.work_path)
        if self.tgz_name != '':
            if os.path.exists(self.tgz_name):
                cmd = 'rm -rf %s' % self.tgz_name
                debug_msg(color_msg('rm file \"%s\".' % self.tgz_name, RED))
                os.system(cmd)
        if self.folder != '':
            if os.path.exists(self.folder):
                cmd = 'rm -rf %s' % self.folder
                debug_msg(color_msg('rm folder \"%s\".' % self.folder, RED))
                os.system(cmd)

    def to_flash_phone(self):
        start_time = time.time()
        try:
            self.download_tgz()
            self.un_tar()
            self.reboot_phone()
            self.flash_phone()
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
        except IndexError:
            print('IndexError')
        except OSError:
            print('OSError')
        except IOError:
            print('IOError')
        except TypeError:
            print('TypeError')
        except NameError:
            print('NameError')
        except urllib2.HTTPError, e:
            print('HTTPError:%s' % e.code)
        finally:
            self.delete_file()
            end_time = time.time()
            cost_time = int(end_time - start_time)
            debug_msg(color_msg('cost_time = %s seconds' % cost_time, RED))


# import threading
#
# def input_func( context ):
# context[ 'data' ] = input( 'input:' )
#
# context = { 'data' : 'default' }
# t = threading.Thread( target = input_func ,args = ( context , ) )
# t.start( )
# t.join( 10 )        #等待10秒
# print( context )


if __name__ == '__main__':
    fp = FlashPhone()
    fp.to_flash_phone()