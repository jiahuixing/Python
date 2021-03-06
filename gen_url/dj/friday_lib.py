# !/usr/local/bin/python -u
# -*- coding: utf-8 -*-
import hashlib
import re
import time

__author__ = 'jiahuixing'

import os

# WORK_PATH = '/home/jiahuixing/Python/gen_url'
WORK_PATH = '/data/ota'

IGNORE_OTA = 'ota'
GLOBAL_SIGN = 'global'

MAIN_URL = 'http://bigota.d.miui.com'

Rom_Properties = [

    [
        #小米手机机型 new named
        ['mione_plus_', 'Mioneplus_', '小米手机1/1S'],
        ['aries_', 'MI2_', '小米手机2/2S'],
        ['aries_alpha_', 'MI2Alpha_', '小米手机2/2S'],
        ['aries_', 'MI2TW_', '小米手机2/2S'],
        ['aries_', 'MI2HK_', '小米手机2/2S'],
        ['taurus_', 'MI2A_', '小米手机2A-WCDMA'],
        ['taurus_alpha_', 'MI2AAlpha_', '小米手机2A-WCDMA'],
        ['pisces_', 'MI3_', '小米手机3-TD'],
        ['cancro_', 'MI3W_', '小米手机3-CDMA/WCDMA'],
        ['cancro_alpha_', 'MI3WAlpha_', '小米手机3-CDMA/WCDMA'],
        ['cancro_global_', 'MI3WGlobal_', '小米手机3-CDMA/WCDMA'],

        #小米手机机型 old named
        ['cancro_my_', 'MI3WMY_', '小米手机3-CDMA/WCDMA'],
        ['cancro_sg_', 'MI3WSG_', '小米手机3-CDMA/WCDMA'],
        ['cancro_tw_', 'MI3WTW_', '小米手机3-CDMA/WCDMA'],
        ['cancro_hk_', 'MI3WHK_', '小米手机3-CDMA/WCDMA'],

    ],
    [
        #红米手机机型 new named
        ['wt93007_', 'HM2_', '红米手机-TD'],
        ['wt98007_', 'HM2W_', '红米手机-WCDMA'],
        ['wt98007_global_', 'HM2WGlobal_', '红米手机-WCDMA'],
        ['armani_', 'H2A_', '红米手机1S'],
        ['wt93807_', 'H2S82TD_', 'H2S-TD'],
        ['wt98807_', 'H2S82W_', 'H2S-WCDMA'],
        ['dior_', 'H3LTE_', '红米Note-LTE'],
        ['lcsh92_wet_tdd_', 'H3TD_', '红米Note-TD'],
        ['lcsh92_wet_jb9_', 'H3W_', '红米Note-WCDMA'],
        ['lcsh92_wet_jb9_global_', 'H3WGlobal_', '红米Note-WCDMA'],

        #红米手机机型 old named
        ['HM2013023_tw_', 'HM2WTW_', '红米手机-WCDMA'],
        ['HM2013023_sg_', 'HM2WSG_', '红米手机-WCDMA'],
        ['HM2013023_my_', 'HM2WMY_', '红米手机-WCDMA'],
        ['HM2013023_hk_', 'HM2WHK_', '红米手机-WCDMA'],

        ['armani_tw_', 'H2ATW_', '红米手机1S'],
        ['armani_hk_', 'H2AHK_', '红米手机1S'],
        ['armani_my_', 'H2AMY_', '红米手机1S'],
        ['armani_sg_', 'H2ASG_', '红米手机1S'],

        ['lcsh92_wet_jb9_sg_', 'H3WSG_', '红米Note-WCDMA'],
        ['lcsh92_wet_jb9_my_', 'H3WMY_', '红米Note-WCDMA'],
        ['lcsh92_wet_jb9_hk_', 'H3WHK_', '红米Note-WCDMA'],
        ['lcsh92_wet_jb9_tw_', 'H3WTW_', '红米Note-WCDMA'],

    ],

    [
        #小米Pad机型 new named
        ['MOCHA_', 'mocha_', '小米平板X6'],

    ],

]

Rom_Types = [

    #rom的类型 线刷包 | 卡刷包

    ['.zip', '系统升级卡刷包'],
    ['.tgz', 'Fastboot线刷包'],
    ['.tar', 'Fastboot线刷包'],
]

Ops_Types = [

    #运营商种类

    #中国移动   0
    ['chinamobile', '-移动定制版'],
    #中国联通   1
    ['chinaunicom', '-联通定制版'],
    #中国电信   2
    ['chinatelecom', '-电信定制版'],

]

Dev_Types = [

    # 版本类型

    '-体验版',
    '-开发版',
    '-稳定版',

]

Area_Types = [

    # [flag1, flag2', Area],

    ['HK_', 'hk_', '-香港'],
    ['ID_', 'id_', '-印度'],
    ['IN_', 'in_', '-印度尼西亚'],
    ['MY_', 'my_', '-马来西亚'],
    ['PH_', 'ph_', '-菲律宾'],
    ['SG_', 'sg_', '-新加坡'],
    ['TH_', 'th_', '-泰国'],
    ['TW_', 'tw_', '-台湾'],

]

COLOR_START = '\033[0;'
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
        color.append(color_fg)
    if bg is not None:
        color_bg = '4%d' % bg
        color.append(color_bg)
    if len(color) > 0:
        color_str = ';'.join(color)
        msg = '%s%sm%s%s' % (COLOR_START, color_str, msg, COLOR_END)
    return msg


def debug_msg(msg, flag=1):
    if flag == 1:
        print('----------------------------------------------------')
        print(msg)


def get_file_md5(file_name):
    if not os.path.isfile(file_name):
        return
    my_hash = hashlib.md5()
    f = file(file_name, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        my_hash.update(b)
    f.close()
    return my_hash.hexdigest().lower()


def get_rom_size(file_name):
    size = os.path.getsize(file_name) / 1024 / 1024
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


def is_valid_file(file_name):
    valid = 0
    if IGNORE_OTA not in file_name:
        for i in xrange(len(Rom_Types)):
            rom_type = Rom_Types[i][0]
            if str.endswith(file_name, rom_type):
                valid = 1
                break
    return valid


def get_rom_idx(file_name):
    model_idx = -1
    idx = -1
    name = str.lower(file_name)
    for i in xrange(len(Rom_Properties)):
        models = Rom_Properties[i]
        if isinstance(models, list):
            for j in xrange(len(models)):
                model = models[j]
                mask_1 = str.lower(model[0])
                mask_2 = str.lower(model[1])
                if mask_1 in name or mask_2 in name:
                    model_idx = i
                    idx = j
                    break
    str_idx = idx + 1
    return model_idx, idx, str_idx


def get_rom_type(file_name):
    rom_type = ''
    for i in xrange(len(Rom_Types)):
        if Rom_Types[i][0] in file_name:
            rom_type = Rom_Types[i][1]
            break
    return rom_type


def get_op_type(file_name):
    op_type = -1
    name = str.lower(file_name)
    for i in xrange(len(Ops_Types)):
        op = Ops_Types[i][0]
        if op in name:
            op_type = i
            break
        else:
            continue
    return op_type


def get_area_type(file_name):
    area_type = ''
    name = str.lower(file_name)
    if GLOBAL_SIGN in name:
        area_type = '国际'
    for i in xrange(len(Area_Types)):
        flag1 = Area_Types[i][0]
        flag2 = Area_Types[i][1]
        if flag1 in file_name or flag2 in file_name:
            area_type = Area_Types[i][2]
            break
        else:
            continue
    return area_type


def get_dev_type(file_name):
    dev_type = ''
    op_type = get_op_type(file_name)
    if op_type != -1:
        op_name = Ops_Types[op_type][1]
        dev_type = op_name
    else:
        dev_version = r'[0-9]{1}\.[0-9]{1,2}\.[0-9]{1,2}\_'
        stable_version = r'[A-Z]{3,7}[0-9]{1,2}\.[0-9]{1,2}\_'
        pattern_dev = re.compile(dev_version)
        pattern_stable = re.compile(stable_version)
        dev_search_result = re.findall(pattern_dev, file_name)
        stable_search_result = re.findall(pattern_stable, file_name)
        if dev_search_result:
            name = str.lower(file_name)
            if 'alpha' in name:
                dev_type = Dev_Types[0]
            else:
                dev_type = Dev_Types[1]
        elif stable_search_result:
            dev_type = Dev_Types[2]
        area_type = get_area_type(file_name)
        if area_type != '':
            dev_type = area_type + dev_type
    return dev_type


def walk_dir(folder_name):
    debug_msg(color_msg('------walk_dir------'))
    info_xiaomi = dict()
    info_redmi = dict()
    info_pad = dict()
    os.chdir(WORK_PATH)
    if os.path.exists(folder_name):
        file_names = os.listdir(folder_name)
        file_path = '%s/%s' % (WORK_PATH, folder_name)
        os.chdir(file_path)
        for file_name in file_names:
            valid = is_valid_file(file_name)
            if valid == 1:
                tmp = list()
                model_idx, idx, str_idx = get_rom_idx(file_name)
                min_idx = 0
                if str_idx != min_idx:
                    dev_type = get_dev_type(file_name)
                    name = '%s%s' % (Rom_Properties[model_idx][idx][2], dev_type)
                    md5 = get_file_md5(file_name)
                    size = get_rom_size(file_name)
                    rom_type = get_rom_type(file_name)
                    tmp.append(model_idx)
                    tmp.append(idx)
                    tmp.append(md5)
                    tmp.append(size)
                    tmp.append(rom_type)
                    tmp.append(file_name)
                    tmp.append(name)
                    # noinspection PyPep8
                    debug_msg(color_msg(
                        'model_idx = %s,idx = %s\nfile_name = %s\nname = %s\nmd5 = %s\nsize = %s\nrom_type = %s') % (
                                  model_idx, idx, file_name, name, md5, size, rom_type))
                    if model_idx == 0:
                        keys = info_xiaomi.keys()
                        if name not in keys:
                            info_xiaomi[name] = list()
                        info_xiaomi[name].append(tmp)
                    elif model_idx == 1:
                        keys = info_redmi.keys()
                        if name not in keys:
                            info_redmi[name] = list()
                        info_redmi[name].append(tmp)
                    elif model_idx == 2:
                        keys = info_pad.keys()
                        if name not in keys:
                            info_pad[name] = list()
                        info_pad[name].append(tmp)
        return info_xiaomi, info_redmi, info_pad
    else:
        print('folder:%s not exist.' % folder_name)


def get_download_url(version):
    debug_msg(color_msg('------get_download_url------'))
    xiaomi_url, redmi_url, pad_url = '', '', ''
    try:
        info_xiaomi, info_redmi, info_pad = walk_dir(version)
        # info = walk_dir(folder))
        xiaomi_url = make_url(info_xiaomi, version)
        redmi_url = make_url(info_redmi, version)
        pad_url = make_url(info_pad, version)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        return xiaomi_url, redmi_url, pad_url


def make_url(info, version):
    head = '\n【升级提醒】\n—————————————————————————————————————————————————— \n\n'
    body = ''
    end = ' '
    m_url = ''
    domain = '%s/%s/' % (MAIN_URL, version)
    if isinstance(info, dict):
        if len(info) > 0:
            keys = sorted(info.keys())
            for key in keys:
                if key != '':
                    # body += "%s %s\n\n" % (key, version)
                    for i in xrange(len(info[key])):
                        tmp = info[key][i]
                        md5 = tmp[2]
                        size = tmp[3]
                        rom_type = tmp[4]
                        file_name = tmp[5]
                        name = tmp[6]
                        body = '%s%s MIUI %s %s \n%s%s\nsize:%s    md5:%s\n\n' % (
                            body, name, version, rom_type, domain, file_name, size, md5)
                    body += '—————————————————————————————————————————————————— \n\n'
            m_url = head + body + end
        return m_url
    else:
        print('Wrong info.')


def print_url(url):
    if url != '':
        print(url)


def write_url(xiaomi_url, redmi_url, pad_url, flag=0):
    if flag == 1:
        doc_name = 'url.txt'
        os.chdir(WORK_PATH)
        mode = 'a+'
        if os.path.exists(doc_name):
            os.remove(doc_name)
        write_to_file(xiaomi_url, doc_name, mode)
        write_to_file(redmi_url, doc_name, mode)
        write_to_file(pad_url, doc_name, mode)


def write_to_file(url, doc_name, mode='a+'):
    if url != '':
        file_open = open(doc_name, mode)
        file_open.writelines(url)
        file_open.close()