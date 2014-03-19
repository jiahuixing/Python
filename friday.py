__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

import os
import sys
import time
import hashlib

Rom_Properties = [
    ['小米手机1/1S', '开发版 MIUI', 'miui_Mioneplus_4', ], #MI1开发版卡刷包
    ['小米手机1/1S', '稳定版 MIUI', 'miui_Mioneplus_JMA', ], #MI1稳定版卡刷包
    ['小米手机1/1S', '开发版 MIUI', 'mione_plus_images_4', ], #MI1开发版线刷包
    ['小米手机1/1S', '稳定版 MIUI', 'mione_plus_images_JMA', ], #MI1稳定版线刷包
    ['小米手机1/1S', '原生版 ', 'miui_NativeMioneplus', ], #MI1原生版卡刷包
    ['小米手机1/1S', '原生版', 'mione_android', ], #MI1原生版线刷包

    ['小米手机2/2S', '开发版 MIUI', 'miui_MI2_4', ], #MI2开发版卡刷包
    ['小米手机2/2S', '开发版 MIUI', 'aries_images_4', ], #MI2开发版线刷包
    ['小米手机2/2S', '稳定版 MIUI', 'miui_MI2_JLB', ], #MI2稳定版卡刷包
    ['小米手机2/2S', '稳定版 MIUI', 'aries_images_JLB', ], #MI2稳定版线刷包
    ['小米手机2/2S', '体验版 MIUI', 'miui_MI2Alpha_', ], #MI2体验版卡刷包
    ['小米手机2/2S', '体验版 MIUI', 'aries_alpha_', ], #MI2体验版线刷包
    ['小米手机2/2S', '台湾版 MIUI', 'miui_MI2TW_JLB', ], #MI2台湾版卡刷包
    ['小米手机2/2S', '台湾版 MIUI', 'aries_tw_', ], #MI2台湾版线刷包
    ['小米手机2/2S', '香港版 MIUI', 'miui_MI2HK_JLB', ], #MI2香港版卡刷包
    ['小米手机2/2S', '香港版 MIUI', 'aries_hk_', ], #MI2香港版线刷包
    ['小米手机2/2S', '电信版 MIUI', 'aries_chinatelecom_images', ], #MI2电信版线刷包
    ['小米手机2/2S', '联通版 MIUI', 'aries_chinaunicom_images', ], #MI2联通版线刷包

    ['小米手机2A', '开发版 MIUI', 'miui_MI2AAlpha_', ], #MI2A开发版卡刷包
    ['小米手机2A', '开发版 MIUI', 'taurus_images_', ], #MI2A开发版线刷包
    ['小米手机2A', '联通版 MIUI', 'miui_MI2A_CU_JLB', ], #MI2A联通版线刷包
    ['小米手机2A', '稳定版 MIUI', 'miui_MI2A_JLB', ], #MI2A稳定版卡刷包、线刷包
    ['小米手机2A', '体验版 MIUI', 'miui_MI2AAlpha_', ], #MI2A体验版卡刷包
    ['小米手机2A', '体验版 MIUI', 'taurus_alpha_images_', ], #MI2A体验版线刷包
    ['小米手机2A_TD', '开发版 MIUI', 'miui_MI2ATD_', ], #MI2A-TD开发版卡刷包

    ['小米手机3-TD', '开发版 MIUI', 'pisces_images_', ], #MI3TD开发版线刷包
    ['小米手机3-TD', '开发版 MIUI', 'miui_MI3_4', ], #MI3TD开发版卡刷包
    ['小米手机3-TD', '稳定版 MIUI', 'miui_MI3_JXC', ], #MI3TD稳定版卡刷包
    ['小米手机3-TD', '稳定版 MIUI', 'miui_MI3-TD_JXC', ], #MI3TD稳定版线刷包
    ['小米手机3-TD', '移动版 MIUI', 'miui_MI3-TD_CM_JXC', ], #MI3TD移动版线刷包

    ['小米手机3-WCDMA/CDMA', '开发版 MIUI', 'cancro_images_', ], #MI3W开发版线刷包
    ['小米手机3-WCDMA/CDMA', '开发版 MIUI', 'miui_MI3W_4', ], #MI3W开发版卡刷包
    ['小米手机3-WCDMA/CDMA', '稳定版 MIUI', 'miui_MI3W_JXD', ], #MI3W稳定版卡刷包
    ['小米手机3-WCDMA/CDMA', '稳定版 MIUI', 'miui_MI3-WCDMA_JXD', ], #MI3W稳定版线刷包
    ['小米手机3-WCDMA', '联通版 MIUI', 'miui_MI3-WCDMA_CU_JXD', ], #MI3W联通版线刷包
    ['小米手机3-WCDMA', '香港版 MIUI', 'miui_MI3-WCDMA_HK_JXD', ], #MI3W香港版线刷包
    ['小米手机3-WCDMA', '香港版 MIUI', 'miui_MI3WHK_JXD', ], #MI3W香港版卡刷包
    ['小米手机3-WCDMA', '台湾版 MIUI', 'miui_MI3-WCDMA_TW_JXD', ], #MI3W台湾版线刷包
    ['小米手机3-WCDMA', '台湾版 MIUI', 'miui_MI3WTW_JXD', ], #MI3W台湾版卡刷包
    ['小米手机3-WCDMA', '新加坡版 MIUI', 'miui_MI3-WCDMA_SG_JXD', ], #MI3W新加坡版线刷包
    ['小米手机3-WCDMA', '新加坡版 MIUI', 'miui_MI3WSG_JXD', ], #MI3W新加坡版卡刷包
    ['小米手机3-WCDMA', '马来西亚版 MIUI', 'miui_MI3-WCDMA_MY_JXD', ], #MI3W马来西亚版线刷包
    ['小米手机3-WCDMA', '马来西亚版 MIUI', 'miui_MI3WMY_JXD', ], #MI3W马来西亚版卡刷包
    ['小米手机3-WCDMA/CDMA', '电信版 MIUI', 'miui_MI3-WCDMA_CT_JXD', ], #MI3W电信版线刷包



    ['红米手机_WCDMA', '稳定版 MIUI', 'miui_HM2W_JHBCN', ], #HMW稳定版卡刷包
    ['红米手机_TD', '稳定版 MIUI', 'miui_HM2_JHACN', ], #HMTD稳定版卡刷包
    ['红米手机_WCDMA', '香港版 MIUI', 'miui_HM2WHK', ], #HMW香港版卡刷包
    ['红米手机_WCDMA', '台湾版 MIUI', 'miui_HM2WTW', ], #HMW台湾版卡刷包
    ['红米手机_WCDMA', '新加坡版 MIUI', 'miui_HM2WSG_JHBSG', ], #HMW新加坡版卡刷包
    ['红米手机_1S', '稳定版 MIUI', 'miui_H1S_JHCCN', ], #HM1S稳定版线刷包
    ['红米手机_1S', '稳定版 MIUI', 'miui_H2A_JHCCN', ], #HM1S稳定版卡刷包
    ['红米手机_1S', '电信版 MIUI', 'miui_H1S_CT_JHCCN', ], #HM1S电信版线刷包

]

Rom_Type = [
    ['zip', '卡刷包', ],
    ['tgz', '线刷包', ],
    ['tar', '线刷包'],
]


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


def get_rom_size(filename):
    if not os.path.isfile(filename):
        return
    size = os.path.getsize(filename) / 1024 / 1024
    size = str(size) + 'M'
    return size


def get_version():
    block = '.'
    argv_len = len(sys.argv)
    if argv_len >= 3:
        version = sys.argv[2]
    else:
        year, mon, day = time.strftime('%Y'), time.strftime('%m'), time.strftime('%d')
        year = year[-1]
        mon = str(int(mon))
        day = str(int(day))
        version = year + block + mon + block + day
    return version


def get_rom_detail(rom_name):
    length = len(Rom_Properties)
    index = 0
    for i in xrange(length):
        rom_property = Rom_Properties[i][2]
        if rom_property in rom_name:
            index = i + 1
            break
    return index


def get_rom_type(rom_name):
    rom_type = ''
    for i in xrange(len(Rom_Type)):
        info = Rom_Type[i]
        sub = info[0]
        if sub in rom_name:
            rom_type = info[1]
            break
    return rom_type


def walk_dir(folder_name, topdown=True):
    miui = 'miui_'
    images = '_images_'
    rom_info = list()
    for root, dirs, files in os.walk(folder_name, topdown):
        for name in files:
            if miui in name or images in name:
                index = get_rom_detail(name)
                print os.path.abspath(os.path.join(root, name))
                print(index)
                if index > 0:
                    info = [index, name]
                    rom_type = get_rom_type(name)
                    info.append(rom_type)
                    size = get_rom_size(os.path.join(root, name))
                    info.append(size)
                    md5 = get_file_md5(os.path.join(root, name))
                    info.append(md5)
                    rom_info.append(info)
    return rom_info


class Generate:
    m_folder = ''
    version = ''
    print_format = ''

    def __init__(self):
        if len(sys.argv) >= 2:
            self.m_folder = sys.argv[1]
            self.version = get_version()
            print('Folder:' + self.m_folder)
            print('Version:' + self.version)
        else:
            print('No argv given.')
            return

    def get_print_format(self):
        wrap = '\r\n'
        print_format = '' + wrap
        tab = '     '
        sub_url = 'http://bigota.d.miui.com/'
        if self.m_folder != '':
            if os.path.exists(self.m_folder):
                rom_info = walk_dir(self.m_folder)
                for i in xrange(len(rom_info)):
                    info = rom_info[i]
                    index = info[0] - 1
                    name = info[1]
                    rom_type = info[2]
                    size = info[3]
                    md5 = info[4]
                    rom_property = Rom_Properties[index]
                    c_name = rom_property[0]
                    dev_type = rom_property[1]
                    url = sub_url + self.version + '/' + name
                    print_format = "%s%s %s %s %s%s%s%s%s%s%s%s%s" % (
                        print_format, c_name, dev_type, self.version, rom_type, wrap, url, wrap, size, tab, md5,
                        wrap, wrap)
                self.print_format = print_format
            else:
                print('Folder not found.')
                sys.exit()
        else:
            print('Folder not given.')
            sys.exit()

    def write_print_format(self):
        read_mode = 'w'
        file_name = self.version + '.txt'
        file_obj = open(file_name, read_mode)
        file_obj.write(self.print_format)
        file_obj.close()


if __name__ == '__main__':
    print('.........Begin to work.........')
    begin = time.time()
    ge = Generate()
    ge.get_print_format()
    end = time.time()
    cost = int(end - begin)
    print('.........Work done.........')
    print(".........Cost time : %d seconds........." % cost)
    print(ge.print_format)
    #ge.write_print_format()

