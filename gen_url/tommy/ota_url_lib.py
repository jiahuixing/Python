# !/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

import os
import sys
import hashlib
import re
import time
import optparse

Model_Types = [
    '小米手机',
    '红米手机',
    '小米平板',
]

Rom_Properties = [

    [
        # 小米手机机型 new named
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

        # 小米手机机型 old named
        ['cancro_my_', 'MI3WMY_', '小米手机3-CDMA/WCDMA'],
        ['cancro_sg_', 'MI3WSG_', '小米手机3-CDMA/WCDMA'],
        ['cancro_tw_', 'MI3WTW_', '小米手机3-CDMA/WCDMA'],
        ['cancro_hk_', 'MI3WHK_', '小米手机3-CDMA/WCDMA'],

    ],
    [
        # 红米手机机型 new named
        ['wt93007_', 'HM2_', '红米手机-TD'],
        ['wt98007_', 'HM2W_', '红米手机-WCDMA'],
        ['wt98007_global_', 'HM2WGlobal_', '红米手机-WCDMA'],
        ['armani_', 'H2A_', '红米手机1S'],
        ['armani_global', 'H2AGlobal_', '红米手机1S'],
        ['wt93807_', 'H2S82TD_', 'H2S-TD'],
        ['wt98807_', 'H2S82W_', 'H2S-WCDMA'],
        ['wt98807_global', 'H2S82W_Global', 'H2S-WCDMA'],
        ['dior_', 'H3LTE_', '红米Note-LTE'],
        ['lcsh92_wet_tdd_', 'H3TD_', '红米Note-TD'],
        ['lcsh92_wet_jb9_', 'H3W_', '红米Note-WCDMA'],
        ['lcsh92_wet_jb9_global_', 'H3WGlobal_', '红米Note-WCDMA'],
        ['wt96007_', 'WT96007_', 'WT96007-TD'],

        # 红米手机机型 old named
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
        # 小米Pad机型 new named
        ['MOCHA_', 'mocha_', '小米平板X6'],

    ],

]

Rom_Types = [

    # rom的类型 线刷包 | 卡刷包

    ['.zip', '系统升级卡刷包'],
    ['.tgz', 'Fastboot线刷包'],
    ['.tar', 'Fastboot线刷包'],
]

Ops_Types = [

    # 运营商种类

    # 中国移动   0
    ['chinamobile', '中国移动定制'],
    # 中国联通   1
    ['chinaunicom', '中国联通定制'],
    # 中国电信   2
    ['chinatelecom', '中国电信定制'],

]

Dev_Types = [

    # 版本类型

    '体验版',
    '开发版',
    '稳定版',

]

Area_Types = [

    # [flag1, flag2', Area],

    ['HK_', 'hk_', '香港'],
    ['ID_', 'id_', '印度尼西亚'],
    ['IN_', 'in_', '印度'],
    ['MY_', 'my_', '马来西亚'],
    ['PH_', 'ph_', '菲律宾'],
    ['SG_', 'sg_', '新加坡'],
    ['TH_', 'th_', '泰国'],
    ['TW_', 'tw_', '台湾'],

]


# noinspection PyClassHasNoInit
class DefaultFolder:
    PYTHON_FILE_PATH = '/data/files'
    USER_OTA_PATH = '/data/ota/'
    ENG_PATH = '/data/eng/'


# noinspection PyClassHasNoInit
class Sign:
    IGNORE_OTA = 'ota'
    GLOBAL_SIGN = 'global'


def init_options():
    usage_msg = 'usage: %prog [options] arg'
    parser = optparse.OptionParser(usage=usage_msg)
    parser.add_option('-d', '--dj', dest='dj_ota_folder')
    parser.add_option('-t', '--tommy', dest='tommy_ota_folder')
    parser.add_option('-v', '--version', dest='ota_version')
    (options, args) = parser.parse_args()
    # print(len(sys.argv))
    # print(options)
    # print(options.dj_ota_folder)
    # print(options.tommy_ota_folder)
    # print(options.ota_version)
    return options


def judge_options(options):
    who = 0
    argv_length = len(sys.argv[1:])
    exp_msg = '正确的用法:\n1. python ota_url.py -t /data/eng/4.6.11-internal -v 4.6.11\n' \
              '2. python ota_url.py -d /data/eng/4.6.11-internal -v 4.6.11'
    if argv_length == 4:
        if options.ota_version is not None:
            if options.tommy_ota_folder is not None:
                who = 1
            elif options.dj_ota_folder is not None:
                who = 2
            else:
                debug_msg(color_msg('错误的参数', RED))
                debug_msg(color_msg(exp_msg, RED))
        else:
            debug_msg(color_msg('没有输入版本号', RED))
            debug_msg(color_msg(exp_msg, RED))
    else:
        debug_msg(color_msg('错误的参数个数', RED))
        debug_msg(color_msg(exp_msg, RED))
    return who


COLOR_START = '\033[0;'
COLOR_END = '\033[0m'
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def color_msg(msg, fg=GREEN, bg=None):
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
    if Sign.IGNORE_OTA not in file_name:
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
    rom_type_idx = -1
    rom_type = ''
    op_type = get_op_type(file_name)
    area_type = get_area_type(file_name)
    for i in xrange(len(Rom_Types)):
        if Rom_Types[i][0] in file_name:
            rom_type_idx = i
            rom_type = Rom_Types[i][1]
            if rom_type_idx != 0:
                if op_type == -1 and area_type == '':
                    rom_type = '标准%s' % rom_type
                else:
                    if op_type != -1:
                        op_name = Ops_Types[op_type][1]
                        rom_type = '%s%s' % (op_name, rom_type)
                    if area_type != '':
                        rom_type = '%s%s' % (area_type, rom_type)
            break
    return rom_type_idx, rom_type


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
    if Sign.GLOBAL_SIGN in name:
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


def search_dev(file_name):
    dev = 0
    dev_version = r'[0-9]{1}\.[0-9]{1,2}\.[0-9]{1,2}\_'
    stable_version = r'[a-z]{3,7}[0-9]{1,2}\.[0-9]{1,2}\_'
    pattern_dev = re.compile(dev_version)
    pattern_stable = re.compile(stable_version)
    dev_search_result = re.findall(pattern_dev, file_name)
    stable_search_result = re.findall(pattern_stable, file_name)
    if dev_search_result:
        dev = 1
    elif stable_search_result:
        dev = 2
    return dev


def get_dev_type(file_name):
    dev_type = ''
    name = str.lower(file_name)
    dev = search_dev(name)
    if dev == 1:
        if 'alpha' in name:
            dev_type = Dev_Types[0]
        else:
            dev_type = Dev_Types[1]
    elif dev == 2:
        dev_type = Dev_Types[2]
    area_type = get_area_type(file_name)
    if area_type != '':
        dev_type = '国际' + dev_type
    return dev_type


def sort_file_names(file_names):
    zip_files = list()
    fast_boot_files = list()
    if isinstance(file_names, list):
        for file_name in file_names:
            if 'zip' in file_name:
                zip_files.append(file_name)
            else:
                if 'tgz' in file_name or 'tar' in file_name:
                    fast_boot_files.append(file_name)
    new_file_names = list()
    if len(fast_boot_files) > 0:
        for fast_boot_file in fast_boot_files:
            new_file_names.append(fast_boot_file)
    if len(zip_files) > 0:
        for zip_file in zip_files:
            new_file_names.append(zip_file)
    return new_file_names


def walk_dir(generate):
    debug_msg(color_msg('------walk_dir------'))
    os.chdir(generate.work_path)
    info_xiaomi = dict()
    info_redmi = dict()
    info_pad = dict()
    if os.path.exists(generate.m_folder):
        file_names = os.listdir(generate.m_folder)
        file_names = sort_file_names(file_names)
        file_path = '%s/%s' % (generate.work_path, generate.m_folder)
        os.chdir(file_path)
        for file_name in file_names:
            valid = is_valid_file(file_name)
            if valid == 1:
                tmp_info = list()
                model_idx, idx, str_idx = get_rom_idx(file_name)
                min_idx = 0
                if str_idx != min_idx:
                    rom_type_idx, rom_type = get_rom_type(file_name)
                    dev_type = get_dev_type(file_name)
                    name = '%s-%s' % (Rom_Properties[model_idx][idx][2], dev_type)
                    md5 = get_file_md5(file_name)
                    size = get_rom_size(file_name)
                    tmp_info.append(model_idx)
                    tmp_info.append(idx)
                    tmp_info.append(md5)
                    tmp_info.append(size)
                    tmp_info.append(rom_type)
                    tmp_info.append(file_name)
                    tmp_info.append(name)
                    # noinspection PyPep8
                    debug_msg(color_msg(
                        'model_idx = %s,idx = %s\nfile_name = %s\nname = %s\n'
                        'md5 = %s\nsize = %s\nrom_type_idx = %s rom_type = %s') % (
                                  model_idx, idx, file_name, name, md5, size, rom_type_idx, rom_type))
                    if model_idx == 0:
                        keys = info_xiaomi.keys()
                        if name not in keys:
                            info_xiaomi[name] = list()
                        info_xiaomi[name].append(tmp_info)
                    elif model_idx == 1:
                        keys = info_redmi.keys()
                        if name not in keys:
                            info_redmi[name] = list()
                        info_redmi[name].append(tmp_info)
                    elif model_idx == 2:
                        keys = info_pad.keys()
                        if name not in keys:
                            info_pad[name] = list()
                        info_pad[name].append(tmp_info)
        return info_xiaomi, info_redmi, info_pad
    else:
        debug_msg(color_msg('folder:%s not exist.' % generate.m_folder, RED))
        sys.exit()


def get_download_url(generate):
    debug_msg(color_msg('------get_download_url------'))
    info_xiaomi, info_redmi, info_pad = walk_dir(generate)
    xiaomi_url = make_url(info_xiaomi, generate)
    redmi_url = make_url(info_redmi, generate)
    pad_url = make_url(info_pad, generate)
    return xiaomi_url, redmi_url, pad_url


def make_url(info, generate):
    head = '\n【升级提醒】\n—————————————————————————————————————————————————— \n\n'
    body = ''
    end = ' '
    m_url = ''
    if generate.m_who == 1:
        domain = '%s/%s/%s/' % (generate.main_url, generate.m_sub_address, generate.m_folder)
    else:
        domain = '%s/%s/' % (generate.main_url, generate.m_folder)
    if isinstance(info, dict):
        if len(info) > 0:
            keys = sorted(info.keys())
            for key in keys:
                if key != '':
                    body = "%s%s %s\n\n" % (body, key, generate.m_version)
                    length = len(info[key])
                    for i in xrange(length):
                        tmp = info[key][i]
                        md5 = tmp[2]
                        size = tmp[3]
                        rom_type = tmp[4]
                        file_name = tmp[5]
                        body = '%s\n%s %s MD5: %s\n%s%s\n\n' % (
                            body, rom_type, size, md5, domain, file_name)
                    body += '—————————————————————————————————————————————————— \n\n'
            m_url = head + body + end
        return m_url
    else:
        debug_msg('Wrong info.')


def print_url(url):
    if url != '':
        print(url)


def write_url(xiaomi_url, redmi_url, pad_url, generate, flag=0):
    if flag == 1:
        os.chdir(generate.work_path)
        doc_name = 'url.txt'
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