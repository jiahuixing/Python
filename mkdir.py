# -*- coding: utf-8 -*-

import os
import sys
import time
import hashlib

BLOCK = ' '
PYTHON_FILE_PATH = '/data/files'
USER_OTA_PATH = '/data/ota/'
ENG_PATH = '/data/eng/'

DEV_MIUI = 'miui_'
ZIP = 'zip'
DEV_IMAGES = '_images_'
TAR = 'tgz'
STABLE_MIUI = 'J'
ORIGIN = 'N'

RomNames = ['M1/M1S-开发版', 'M1/M1S-开发版',
            'M1/M1S-稳定版', 'M1/M1S-稳定版',
            'M1/M1S-Android-原生版', 'M1/M1S-Android-原生版',
            'M2/M2S-开发版', 'M2/M2S-开发版',
            'M2/M2S-稳定版', 'M2/M2S-稳定版',
            'M2/M2S-CU-联通稳定版', 'M2/M2S-CU-联通稳定版',
            'M2/M2S-CT-电信稳定版', 'M2/M2S-CT-电信稳定版',
            'M2/M2S-体验版', 'M2/M2S-体验版',
            'M2/M2S-台湾稳定版', 'M2/M2S-台湾稳定版',
            'M2/M2S-香港稳定版', 'M2/M2S-香港稳定版',
            'M2/M2S-Android-原生版', 'M2/M2S-Android-原生版',
            'M2A-WCDMA-开发版', 'M2A-WCDMA-开发版',
            'M2A-WCDMA-稳定版', 'M2A-WCDMA-稳定版',
            'M2A-WCDMA-CU-联通稳定版', 'M2A-CDMA-CT-联通稳定版',
            'M2A-WCDMA-体验版', 'M2A-WCDMA-体验版',
            'M2A-TD-开发版', 'M2A-TD-开发版',
            'H2-TD-不稳定版', 'H2-TD-不稳定版',
            'H2-TD-稳定版', 'H2-TD-稳定版',
            'H2-TD-移动稳定版', 'H2-TD-移动稳定版',
            'H2-WCDMA-不稳定版', 'H2-WCDMA-不稳定版',
            'H2-WCDMA-稳定版', 'H2-WCDMA-稳定版',
            'H2-WCDMA-CU-联通稳定版', 'H2-WCDMA-CU-联通稳定版',
            'H2-WCDMA-HK-香港开发版', 'H2-WCDMA-HK-香港开发版',
            'H2-WCDMA-HK-香港稳定版', 'H2-WCDMA-HK-香港稳定版',
            'H2-WCDMA-TW-台湾开发版', 'H2-WCDMA-TW-台湾开发版',
            'H2-WCDMA-TW-台湾稳定版', 'H2-WCDMA-TW-台湾稳定版',
            'H2-WCDMA-SG-新加坡开发版', 'H2-WCDMA-SG-新加坡开发版',
            'H2-WCDMA-SG-新加坡稳定版', 'H2-WCDMA-SG-新加坡稳定版',
            'H2-WCDMA-MY-马来西亚开发版', 'H2-WCDMA-MY-马来西亚开发版',
            'H2-WCDMA-MY-马来西亚稳定版', 'H2-WCDMA-MY-马来西亚稳定版',
            'H2S-TD-不稳定版', 'H2S-TD-不稳定版',
            'H2S-TD-稳定版', 'H2S-TD-稳定版',
            'H2S-TD-CM-移动稳定版', 'H2S-TD-CM-移动稳定版',
            'H2S-WCDMA-不稳定版', 'H2S-WCDMA-不稳定版',
            'H2S-WCDMA-稳定版', 'H2S-WCDMA-稳定版',
            'H2S-WCDMA-CU-联通稳定版', 'H2S-WCDMA-CU-联通稳定版',
            'H2S-Plus-TD-不稳定版', 'H2S-Plus-TD-不稳定版',
            'H2S-Plus-TD-稳定版', 'H2S-Plus-TD-稳定版',
            'H2S-Plus-TD-CM-移动稳定版', 'H2S-Plus-TD-CM-移动稳定版',
            'H2S-Plus-WCDMA-不稳定版', 'H2S-Plus-WCDMA-不稳定版',
            'H2S-Plus-WCDMA-稳定版', 'H2S-Plus-WCDMA-稳定版',
            'H2S-Plus-WCDMA-CU-联通定制版', 'H2S-Plus-WCDMA-CU-联通定制版',
            'HM1S-不稳定版', 'HM1S-不稳定版',
            'HM1S-稳定版', 'HM1S-稳定版',
            'HM1S-Android-原生版', 'HM1S-Android-原生版',
            'H3-TD-不稳定版', 'H3-TD-不稳定版',
            'H3-TD-稳定版', 'H3-TD-稳定版',
            'H3-TD-移动定制版', 'H3-TD-移动定制版',
            'H3-WCDMA-不稳定版', 'H3-WCDMA-不稳定版',
            'H3-WCDMA-稳定版', 'H3-WCDMA-稳定版',
            'X3-TD-开发版', 'X3-TD-开发版',
            'X3-TD-稳定版', 'X3-TD-稳定版',
            'X3-TD-移动定制版', 'X3-TD-移动定制版',
            'X3-TD-Android-原生版', 'X3-TD-Android-原生版',
            'X3-WCDMA-开发版', 'X3-WCDMA-开发版',
            'X3-WCDMA-稳定版', 'X3-WCDMA-稳定版',
            'X3-WCDMA-TW-台湾开发版', 'X3-WCDMA-TW-台湾开发版',
            'X3-WCDMA-TW-台湾稳定版', 'X3-WCDMA-TW-台湾稳定版',
            'X3-WCDMA-HK-香港开发版', 'X3-WCDMA-HK-香港开发版',
            'X3-WCDMA-HK-香港稳定版', 'X3-WCDMA-HK-香港稳定版',
            'X3-WCDMA-SG-新加坡开发版', 'X3-WCDMA-SG-新加坡开发版',
            'X3-WCDMA-SG-新加坡稳定版', 'X3-WCDMA-SG-新加坡稳定版',
            'X3-WCDMA-MY-马来西亚开发版', 'X3-WCDMA-MY-马来西亚开发版',
            'X3-WCDMA-MY-马来西亚稳定版', 'X3-WCDMA-MY-马来西亚稳定版',
            'X3-WCDMA-CU-联通定制版', 'X3-WCDMA-CU-联通定制版',
            'X3-WCDMA-CT-电信定制版', 'X3-WCDMA-CT-电信定制版',
            'X3-WCDMA-Android-原生版', 'X3-WCDMA-Android-原生版', ]
str_Marks = ['_Mioneplus_4', 'mione_plus_images_4',
             '_Mioneplus_J', 'mione_plus_images_J',
             '_NativeMioneplus_', 'mione_android',
             '_MI2_4', 'aries_images_4',
             '_MI2_J', 'aries_images_J',
             'aries_chinaunicom_images', 'aries_chinaunicom_images',
             'aries_chinatelecom_images', 'aries_chinatelecom_images',
             '_MI2Alpha_', 'aries_alpha_',
             '_MI2TW_', 'aries_tw_',
             '_MI2HK_', 'aries_hk_',
             '_NativeMI2_', 'aries_images_',
             '_MI2A_4', 'taurus_images_4',
             '_MI2A_J', 'taurus_images_J',
             'taurus_chinaunicom_images', 'taurus_chinaunicom_images',
             '_MI2AAlpha_', 'taurus_alpha_images',
             '_MI2ATD_', 'taurus_td_images',
             '_HM2_4', 'wt93007_images_4',
             '_HM2_J', 'wt93007_images_J',
             'wt93007_chinamobile_images', 'wt93007_chinamobile_images',
             '_HM2W_4', 'HM2013023_images_4',
             '_HM2W_J', 'HM2013023_images_J',
             'wt98007_chinaunicom_images', 'wt98007_chinaunicom_images',
             '_HM2WHK_4', 'HM2013023_hk_images_4',
             '_HM2WHK_J', 'HM2013023_hk_images_J',
             '_HM2WTW_4', 'HM2013023_tw_images_4',
             '_HM2WTW_J', 'HM2013023_tw_images_J',
             '_HM2WSG_4', 'HM2013023_sg_images_4',
             '_HM2WSG_J', 'HM2013023_sg_images_J',
             '_HM2WMY_4', 'HM2013023_my_images_4',
             '_HM2WMY_J', 'HM2013023_my_images_J',
             '_H2S82TD_4', 'HM2014011_images_4',
             '_H2S82TD_J', 'HM2014011_images_J',
             'HM2014011_chinamobile_images', 'HM2014011_chinamobile_images',
             '_H2S82W_4', 'HM2014012_images_4',
             '_H2S82W_J', 'HM2014012_images_J',
             'HM2014012_chinaunicom_images', 'HM2014012_chinaunicom_images',
             '_H2S91TD_4', 'HM2014013_images_4',
             '_H2S91TD_J', 'HM2014013_images_J',
             'HM2014013_chinamobile_images', 'HM2014013_chinamobile_images',
             '_H2S91W_4', 'HM2014014_images_4',
             '_H2S91W_J', 'HM2014014_images_J',
             'HM2014014_chinaunicom_images', 'HM2014011_chinaunicom_images',
             '_H2A_4', 'armani_images_4',
             '_H2A_J', 'armani_images_J',
             '_NativeH2A', 'armani_images_Q',
             '_H3TD_4', 'lcsh92_wet_tdd_images_4',
             '_H3TD_J', 'lcsh92_wet_tdd_images_J',
             'lcsh92_wet_tdd_chinamobile_images', 'lcsh92_wet_tdd_chinamobile_images',
             '_H3W_4', 'lcsh92_wet_jb9_images_4',
             '_H3W_J', 'lcsh92_wet_jb9_images_J',
             '_MI3_4', 'pisces_images_4',
             '_MI3_J', 'pisces_images_J',
             'pisces_chinamobile_images', 'pisces_chinamobile_images',
             '_NativeMI3_N', 'pisces_images_N',
             '_MI3W_4', 'cancro_images_4',
             '_MI3W_J', 'cancro_images_J',
             '_MI3WTW_4', 'cancro_tw_images_4',
             '_MI3WTW_J', 'cancro_tw_images_J',
             '_MI3WHK_4', 'cancro_hk_images_4',
             '_MI3WHK_J', 'cancro_hk_images_J',
             '_MI3WSG_4', 'cancro_sg_images_4',
             '_MI3WSG_J', 'cancro_sg_images_J',
             '_MI3WMY_4', 'cancro_my_images_4',
             '_MI3WMY_J', 'cancro_my_images_J',
             'cancro_chinaunicom_images', 'cancro_chinaunicom_images',
             'cancro_chinatelecom_images', 'cancro_chinatelecom_images',
             '_NativeMI3W_Q', 'cancro_images_Q', ]


def walk_dir(m_folder, topdown=True):
    info = {}

    for root, dirs, files in os.walk(m_folder, topdown):
        for file_name in files:
            tmp = []
            print os.path.abspath(file_name)
            if DEV_MIUI in file_name and ZIP in file_name:
                print('开发版zip')
                c_name = get_rom_c_name(file_name)
                size = get_rom_size(os.path.join(root, file_name))
                md5 = get_file_md5(os.path.join(root, file_name))
                tmp.append(size)
                tmp.append(md5)
                tmp.append(file_name)
                if c_name not in info.keys():
                    info[c_name] = []
                    info[c_name].append(tmp)
                else:
                    info[c_name].append(tmp)
            elif DEV_IMAGES in file_name and TAR in file_name:
                print('开发版tgz')
                c_name = get_rom_c_name(file_name)
                size = get_rom_size(os.path.join(root, file_name))
                md5 = get_file_md5(os.path.join(root, file_name))
                tmp.append(size)
                tmp.append(md5)
                tmp.append(file_name)
                if c_name not in info.keys():
                    info[c_name] = []
                    info[c_name].append(tmp)
                else:
                    info[c_name].append(tmp)
                    #            elif file_name.startswith(STABLE_MIUI) and (TAR or ZIP) in file_name:
                    #                print('稳定版')
                    #            elif file_name.startswith(ORIGIN):
                    #                print('原生')
                    #print(info)
    return info


def get_file_md5(filename):
    if not os.path.isfile(filename):
        return
    my_hash = hashlib.md5()
    f = file(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        my_hash.update(b)
    f.close()
    return my_hash.hexdigest().lower()


def get_rom_c_name(name):
    rom_c_name = ''
    roms_length = len(RomNames)
    for i in xrange(roms_length):
        mark = str_Marks[i]
        if mark in name:
            rom_c_name = RomNames[i]
            break
    return rom_c_name


def get_rom_size(filename):
    size = os.path.getsize(filename) / 1024 / 1024
    size = str(size) + 'M'
    return size


def get_date():
    block = '.'
    year, mon, day = time.strftime('%Y'), time.strftime('%m'), time.strftime('%d')
    year = year[-1]
    mon = str(int(mon))
    day = str(int(day))
    m_date = year + block + mon + block + day
    return m_date


def get_version_type():
    num_letter = 0
    input_type = 0
    if len(sys.argv) < 2:
        num_letter = 1
        input_type = 0
    else:
        version = str(sys.argv[1])
        nums = '0123456789'
        letters = 'abcdefghijklmnopqrstuvwxyz'
        num_length = len(nums)
        letter_length = len(letters)
        #        print('num_length=%d'%num_length)
        #        print('letter_length=%d'%letter_length)
        if num_letter == 0:
            for i in xrange(num_length):
                num = nums[i]
                #                print('num=%s'%num)
                if version.startswith(num):
                    num_letter = 1
                    input_type = 0
                    break
                else:
                    continue
        if num_letter == 0:
            for j in xrange(letter_length):
                letter = letters[j].upper()
                #                print('letter=%s'%letter)
                if version.startswith(letter):
                    num_letter = 1
                    input_type = 1
                    break
                else:
                    continue
    if num_letter == 1:
    #        print('input_type=%d'%input_type)
        return input_type
    else:
        get_version_type()


def get_path_names():
    length = len(sys.argv)
    if length >= 2:
    #        print('argvs >= 2')
        version = sys.argv[1]
    else:
    #        print('argvs < 2')
        version = get_date()
    internal_version = version + '-internal'
    return version, internal_version


def create_path():
    cwd = str(os.getcwd()).strip('\n').strip('\r')
    version, internal_version = get_path_names()
    version_type = get_version_type()
    if cwd == PYTHON_FILE_PATH:
        print('File path correct,begin to create path.')
        if not os.path.exists(version):
            print('Path %s is not exist' % version)
            os.mkdir(version)
        else:
            print('Path %s is already exist' % version)
        if version_type == 0:
            if not os.path.exists(internal_version):
                print('Path %s is not exist' % internal_version)
                os.mkdir(internal_version)
            else:
                print('Path %s is already exist' % internal_version)
    else:
        print('Pls move this python file to path:%s.' % PYTHON_FILE_PATH)


def move_files_paths():
    cwd = str(os.getcwd()).strip('\n').strip('\r')
    version, internal_version = get_path_names()
    version_type = get_version_type()
    if cwd == PYTHON_FILE_PATH:
        move_internal = 'mv *internal* ' + internal_version
        move_other = 'mv *' + version + '*.zip* *' + version + '*.tgz* ' + version
        if version_type == 0:
            print('Move internal files to path:%s.' % internal_version)
            os.system(move_internal)
            print('Move xml files to path:%s.' % internal_version)
            mv_xml = 'mv *' + version + '*.xml ' + internal_version
            os.system(mv_xml)
        elif version_type == 1:
            mv_xml = 'mv *' + version + '*.xml ' + version
            os.system(mv_xml)
        print('Move zip and tgz files to path:%s.' % version)
        os.system(move_other)
        move_user_ota = 'mv ' + version + BLOCK + USER_OTA_PATH
        print('Move ota path to path:%s.' % USER_OTA_PATH)
        os.system(move_user_ota)
        if version_type == 0:
            move_eng = 'mv ' + internal_version + BLOCK + ENG_PATH
            print('Move internal path to path:%s.' % ENG_PATH)
            os.system(move_eng)
    else:
        print('Pls move this python file to path:%s.' % PYTHON_FILE_PATH)


def write_print_format(version, msg):
    read_mode = 'w'
    file_name = version + '-url.txt'
    file_obj = open(file_name, read_mode)
    file_obj.write(msg)
    file_obj.close()


class Generate:
    m_folder = ''
    m_version = ''

    def __init__(self):
        self.get_version()
        self.get_folder()

    def get_folder(self):
        argv_len = len(sys.argv)
        if argv_len >= 2:
            m_folder = sys.argv[1]
        else:
            m_folder = get_date()
        self.m_folder = USER_OTA_PATH + m_folder

    def get_version(self):
        if len(sys.argv) >= 2:
            version = sys.argv[1]
        else:
            version = get_date()
        self.m_version = version

    def get_download_url(self):

        m_folder = self.m_folder
        info = walk_dir(m_folder)
        version = self.m_version
        body = ''
        head = '【升级提醒】\n—————————————————————————————————————————————————— \n\n'
        end = ' '
        url_head = 'http://ota.n.miui.com/ota/' + version + '/'
        for key in info.keys():
            if key != '':
                #print('key:%s'%key)
                length = len(info[key])
                #print('length:%s'%length)
                c_name = key
                body += "%s %s\n" % (c_name, version)
                for i in xrange(length):
                    #print('i:%d'%i)
                    tmp = info[key][i]
                    size = tmp[0]
                    md5 = tmp[1]
                    name = tmp[2]
                    if 'tgz' in name:
                        rom_type = 'Fastboot线刷包 '
                    else:
                        rom_type = '系统升级卡刷包 '
                    body = '%s%s%s MD5: %s\n%s%s \n\n' % (body, rom_type, size, md5, url_head, name)
                body += '—————————————————————————————————————————————————— \n\n'
        m_url = head + body + end
        return m_url


if __name__ == '__main__':
    create_path()
    move_files_paths()
    generate = Generate()
    url = generate.get_download_url()
    print url
    #write_print_format(generate.mVersion,url)

