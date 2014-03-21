# -*- coding: utf-8 -*-

import hashlib
import os
import sys
import time
import re

# IMAGES_SUF = r'_4.[0-9]{1}_[a-zA-Z0-9]{10}.tar'

Rom_Properties = [

    [
        ##############################################小米手机##############################################

        # 小米手机1/1S

        ['_Mioneplus_4', 'M1/M1S-开发版', ],
        ['mione_plus_images_4', 'M1/M1S-开发版', ],
        ['_Mioneplus_J', 'M1/M1S-稳定版', ],
        ['mione_plus_images_J', 'M1/M1S-稳定版', ],
        ['_NativeMioneplus_', 'M1/M1S-Android-原生版', ],
        ['mione_android', 'M1/M1S-Android-原生版', ],

        # 小米手机2/2S

        ['_MI2_4', 'M2/M2S-开发版', ],
        ['aries_images_4', 'M2/M2S-开发版', ],
        ['_MI2_J', 'M2/M2S-稳定版', ],
        ['aries_images_J', 'M2/M2S-稳定版', ],
        ['aries_chinaunicom_images', 'M2/M2S-CU-联通稳定版', ],
        ['aries_chinatelecom_images', 'M2/M2S-CT-电信稳定版', ],
        ['_MI2Alpha_', 'M2/M2S-体验版', ],
        ['aries_alpha_', 'M2/M2S-体验版', ],
        ['_MI2TW_', 'M2/M2S-台湾稳定版', ],
        ['aries_tw_', 'M2/M2S-台湾稳定版', ],
        ['_MI2HK_', 'M2/M2S-香港稳定版', ],
        ['aries_hk_', 'M2/M2S-香港稳定版', ],
        ['_NativeMI2_', 'M2/M2S-Android-原生版', ],
        ['aries_images_', 'M2/M2S-Android-原生版', ],

        # 小米手机2A TD

        ['_MI2ATD_', 'M2A-TD-开发版', ],
        ['taurus_td_images', 'M2A-TD-开发版', ],

        # 小米手机2A WCDMA

        ['_MI2A_4', 'M2A-WCDMA-开发版', ],
        ['taurus_images_4', 'M2A-WCDMA-开发版', ],
        ['_MI2A_J', 'M2A-WCDMA-稳定版', ],
        ['taurus_images_J', 'M2A-WCDMA-稳定版', ],
        ['taurus_chinaunicom_images', 'M2A-WCDMA-CU-联通稳定版', ],
        ['_MI2AAlpha_', 'M2A-WCDMA-体验版', ],
        ['taurus_alpha_images', 'M2A-WCDMA-体验版', ],

        # 小米手机3 TD

        ['_MI3_4', 'X3-TD-开发版', ],
        ['pisces_images_4', 'X3-TD-开发版', ],
        ['_MI3_J', 'X3-TD-稳定版', ],
        ['pisces_images_J', 'X3-TD-稳定版', ],
        ['pisces_chinamobile_images', 'X3-TD-移动定制版', ],
        ['_NativeMI3_N', 'X3-TD-Android-原生版', ],
        ['pisces_images_N', 'X3-TD-Android-原生版', ],

        # 小米手机3 WCDMA

        ['_MI3W_4', 'X3-WCDMA-开发版', ],
        ['cancro_images_4', 'X3-WCDMA-开发版', ],
        ['_MI3W_J', 'X3-WCDMA-稳定版', ],
        ['cancro_images_J', 'X3-WCDMA-稳定版', ],
        ['_MI3WTW_4', 'X3-WCDMA-TW-台湾开发版', ],
        ['cancro_tw_images_4', 'X3-WCDMA-TW-台湾开发版', ],
        ['_MI3WTW_J', 'X3-WCDMA-TW-台湾稳定版', ],
        ['cancro_tw_images_J', 'X3-WCDMA-TW-台湾稳定版', ],
        ['_MI3WHK_4', 'X3-WCDMA-HK-香港开发版', ],
        ['cancro_hk_images_4', 'X3-WCDMA-HK-香港开发版', ],
        ['_MI3WHK_J', 'X3-WCDMA-HK-香港稳定版', ],
        ['cancro_hk_images_J', 'X3-WCDMA-SG-香港稳定版', ],
        ['_MI3WSG_4', 'X3-WCDMA-SG-新加坡开发版', ],
        ['cancro_sg_images_4', 'X3-WCDMA-SG-新加坡开发版', ],
        ['_MI3WSG_J', 'X3-WCDMA-SG-新加坡稳定版', ],
        ['cancro_sg_images_J', 'X3-WCDMA-SG-新加坡稳定版', ],
        ['_MI3WMY_4', 'X3-WCDMA-MY-马来西亚开发版', ],
        ['cancro_my_images_4', 'X3-WCDMA-MY-马来西亚开发版', ],
        ['_MI3WMY_J', 'X3-WCDMA-MY-马来西亚稳定版', ],
        ['cancro_my_images_J', 'X3-WCDMA-MY-马来西亚稳定版', ],
        ['cancro_chinaunicom_images', 'X3-WCDMA-CU-联通定制版', ],
        ['cancro_chinatelecom_images', 'X3-WCDMA-CT-电信定制版', ],
        ['_NativeMI3W_Q', 'X3-WCDMA-Android-原生版', ],
        ['cancro_images_Q', 'X3-WCDMA-Android-原生版', ],

    ],
    [
        ##############################################红米手机##############################################

        # 红米手机2 TD

        ['_HM2_4', 'H2-TD-不稳定版', ],
        ['wt93007_images_4', 'H2-TD-不稳定版', ],
        ['_HM2_J', 'H2-TD-稳定版', ],
        ['wt93007_images_J', 'H2-TD-稳定版', ],
        ['wt93007_chinamobile_images', 'H2-TD-移动稳定版', ],

        # 红米手机2 WCDMA

        ['_HM2W_4', 'H2-WCDMA-不稳定版', ],
        ['HM2013023_images_4', 'H2-WCDMA-不稳定版', ],
        ['_HM2W_J', 'H2-WCDMA-稳定版', ],
        ['HM2013023_images_J', 'H2-WCDMA-稳定版', ],
        ['HM2013023_chinaunicom_images', 'H2-WCDMA-CU-联通稳定版', ],
        ['_HM2WHK_4', 'H2-WCDMA-HK-香港开发版', ],
        ['HM2013023_hk_images_4', 'H2-WCDMA-HK-香港开发版', ],
        ['_HM2WHK_J', 'H2-WCDMA-HK-香港稳定版', ],
        ['HM2013023_hk_images_J', 'H2-WCDMA-HK-香港稳定版', ],
        ['_HM2WTW_4', 'H2-WCDMA-TW-台湾开发版', ],
        ['HM2013023_tw_images_4', 'H2-WCDMA-TW-台湾开发版', ],
        ['_HM2WTW_J', 'H2-WCDMA-TW-台湾稳定版', ],
        ['HM2013023_tw_images_J', 'H2-WCDMA-TW-台湾稳定版', ],
        ['_HM2WSG_4', 'H2-WCDMA-SG-新加坡开发版', ],
        ['HM2013023_sg_images_4', 'H2-WCDMA-SG-新加坡开发版', ],
        ['_HM2WSG_J', 'H2-WCDMA-SG-新加坡稳定版', ],
        ['HM2013023_sg_images_J', 'H2-WCDMA-SG-新加坡稳定版', ],
        ['_HM2WMY_4', 'H2-WCDMA-MY-马来西亚开发版', ],
        ['HM2013023_my_images_4', 'H2-WCDMA-MY-马来西亚开发版', ],
        ['_HM2WMY_J', 'H2-WCDMA-MY-马来西亚稳定版', ],
        ['HM2013023_my_images_J', 'H2-WCDMA-MY-马来西亚稳定版', ],

        # 红米手机2S TD

        ['_H2S82TD_4', 'H2S-TD-不稳定版', ],
        ['HM2014011_images_4', 'H2S-TD-不稳定版', ],
        ['_H2S82TD_J', 'H2S-TD-稳定版', ],
        ['HM2014011_images_J', 'H2S-TD-稳定版', ],
        ['HM2014011_chinamobile_images', 'H2S-TD-CM-移动稳定版', ],

        # 红米手机2S WCDMA

        ['_H2S82W_4', 'H2S-WCDMA-不稳定版', ],
        ['HM2014012_images_4', 'H2S-WCDMA-不稳定版', ],
        ['_H2S82W_J', 'H2S-WCDMA-稳定版', ],
        ['HM2014012_images_J', 'H2S-WCDMA-稳定版', ],
        ['HM2014012_chinaunicom_images', 'H2S-WCDMA-CU-联通稳定版', ],

        # 红米手机2S Plus TD

        ['_H2S91TD_4', 'H2S-Plus-TD-不稳定版', ],
        ['HM2014013_images_4', 'H2S-Plus-TD-不稳定版', ],
        ['_H2S91TD_J', 'H2S-Plus-TD-稳定版', ],
        ['HM2014013_images_J', 'H2S-Plus-TD-稳定版', ],
        ['HM2014013_chinamobile_images', 'H2S-Plus-TD-CM-移动稳定版', ],

        # 红米手机2S Plus WCDMA

        ['_H2S91W_4', 'H2S-Plus-WCDMA-不稳定版', ],
        ['HM2014014_images_4', 'H2S-Plus-WCDMA-不稳定版', ],
        ['_H2S91W_J', 'H2S-Plus-WCDMA-稳定版', ],
        ['HM2014014_images_J', 'H2S-Plus-WCDMA-稳定版', ],
        ['HM2014014_chinaunicom_images', 'H2S-Plus-WCDMA-CU-联通稳定版', ],

        # 红米手机1S

        ['_H2A_4', 'HM1S-不稳定版', ],
        ['armani_images_4', 'HM1S-不稳定版', ],
        ['_H2A_J', 'HM1S-稳定版', ],
        ['armani_images_J', 'HM1S-稳定版', ],

        # 红米手机1S CDMA

        ['armani_chinatelecom_images', 'HM1S-电信稳定版', ],
        ['_NativeH2A', 'HM1S-Android-原生版', ],
        ['armani_images_Q', 'HM1S-Android-原生版', ],

        # 红米手机3

        ['_H3TD_4', 'H3-TD-不稳定版', ],
        ['lcsh92_wet_tdd_images_4', 'H3-TD-不稳定版', ],
        ['_H3TD_J', 'H3-TD-稳定版', ],
        ['lcsh92_wet_tdd_images_J', 'H3-TD-稳定版', ],
        ['lcsh92_wet_tdd_chinamobile_images', 'H3-TD-移动定制版', ],

        # 红米手机3 WCDMA

        ['_H3W_4', 'H3-WCDMA-不稳定版', ],
        ['lcsh92_wet_jb9_images_4', 'H3-WCDMA-不稳定版', ],
        ['_H3W_J', 'H3-WCDMA-稳定版', ],
        ['lcsh92_wet_jb9_images_J', 'H3-WCDMA-稳定版', ],

    ],
    [
        ##############################################小米Pad##############################################

        # 小米平板X6

        ['_MOCHA_4', 'X6-开发版', ],
        ['mocha_images_4', 'X6-开发版', ],

    ],

]

Rom_Types = [

    #rom的类型 线刷包 | 卡刷包

    ['zip', '系统升级卡刷包'],
    ['tgz', 'Fastboot线刷包'],
    ['tar', 'Fastboot线刷包'],
]

Ops_Types = [

    #运营商种类

    #中国移动   0
    ['chinamobile', '-CM-移动稳定版'],
    #中国联通   1
    ['chinaunicom', '-CU-联通定制版'],
    #中国电信   2
    ['chinatelecom', '-CT-电信定制版'],

]

Dev_Types = [

    # 版本类型

    '-体验版',
    '-开发版',
    '-稳定版',
    '-Android-原生版',

]

Area_Types = [

    # 香港版 台湾版 新加坡版 马来西亚版
    # [flag1, flag2', Area],

    ['HK_', '_hk_', '-HK-香港'],
    ['TW_', '_tw_', '-TW-台湾'],
    ['SG_', '_sg_', '-SG-新加坡'],
    ['MY_', '_my_', '-MY-马来西亚'],

]


def get_file_md5(filename):
    """

    @param filename:
    @return md5:
    @summary 获取rom的md5
    """
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


def get_rom_type(name):
    """

    @param name:
    @return rom_type:
    @summary 获取rom的类型
    """
    rom_type = ''
    for i in xrange(len(Rom_Types)):
        if Rom_Types[i][0] in name:
            rom_type = Rom_Types[i][1]
            break
    return rom_type


def get_rom_idx(name):
    """

    @param name:
    @return :
    @summary 获取rom name 在Rom_Properties中的idx
    """
    model_idx = -1
    idx = -1
    name = str.lower(name)
    rom_type_num = len(Rom_Properties)
    for i in xrange(rom_type_num):
        model = Rom_Properties[i]
        model_type_num = len(model)
        for j in xrange(model_type_num):
            mask = str.lower(model[j][0])
            if mask in name:
                model_idx = i
                idx = j
                break
            else:
                continue
    str_idx = str(idx + 1)
    return model_idx, idx, str_idx


def get_rom_size(filename):
    """

    @param filename:
    @return size:
    @summary 获得rom的size
    """
    size = os.path.getsize(filename) / 1024 / 1024
    size = str(size) + 'M'
    return size


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


def write_print_format(version, msg):
    read_mode = 'w'
    file_name = version + '-url.txt'
    file_obj = open(file_name, read_mode)
    file_obj.write(msg)
    file_obj.close()


def get_path_names():
    length = len(sys.argv)
    if length >= 2:
        # print('argvs >= 2')
        version = sys.argv[1]
    else:
        # print('argvs < 2')
        version = get_date()
    internal_version = version + '-internal'
    return version, internal_version


def walk_dir(m_folder, topdown=True):
    """

    @param m_folder:
    @param topdown:
    @return info:
    @summary 遍历目录m_folder
    """
    info_xiaomi = dict()
    info_redmi = dict()
    info_pad = dict()
    for root, dirs, files in os.walk(m_folder, topdown):
        for file_name in files:
            tmp = []
            print os.path.abspath(file_name)
            if Rom_Types[0][0] in file_name or Rom_Types[1][0] in file_name or Rom_Types[2][0] in file_name:
                if 'ota' not in file_name:
                    model_idx, idx, str_idx = get_rom_idx(file_name)
                    # print('idx==%s str_idx=%s' % (idx, str_idx))
                    print('model_idx==%s,idx==%s' % (model_idx, idx))
                    # print(Rom_Properties[idx])
                    min_idx = '0'
                    if str_idx != min_idx:
                        size = get_rom_size(os.path.join(root, file_name))
                        md5 = get_file_md5(os.path.join(root, file_name))
                        c_name = Rom_Properties[model_idx][idx][1]
                        tmp.append(model_idx)
                        tmp.append(idx)
                        tmp.append(size)
                        tmp.append(md5)
                        tmp.append(file_name)
                        # print(tmp)
                        if model_idx == 0:
                            keys = info_xiaomi.keys()
                            # print(keys)
                            if c_name not in keys:
                                info_xiaomi[c_name] = []
                            info_xiaomi[c_name].append(tmp)
                        if model_idx == 1:
                            keys = info_redmi.keys()
                            # print(keys)
                            if c_name not in keys:
                                info_redmi[c_name] = []
                            info_redmi[c_name].append(tmp)
                        if model_idx == 2:
                            keys = info_pad.keys()
                            # print(keys)
                            if c_name not in keys:
                                info_pad[c_name] = []
                            info_pad[c_name].append(tmp)
                    else:
                        print('Not in Rom_Types list.')
                else:
                    print('Ota files.')
            else:
                print('Not valid "zip,tar,tgz" files.')

    return info_xiaomi, info_redmi, info_pad


def to_get_url(info, version):
    """

    @param info:
    @param version:
    @return m_url:
    @summary 组合url
    """
    m_url = ''
    body = ''
    head = '【升级提醒】\n—————————————————————————————————————————————————— \n\n'
    end = ' '
    url_head = 'http://ota.n.miui.com/ota/' + version + '/'
    if {} != info:
        keys = info.keys()
        # print('pre_sort')
        # print(keys)
        # for key in keys:
        #     print(key)
        # print('after_sort')
        keys = sorted(keys)
        # print(keys)
        # for key in keys:
        #     print(key)
        for key in keys:
            if key != '':
                #print('key:%s'%key)
                length = len(info[key])
                #print('length:%s'%length)
                body += "%s %s\n\n" % (key, version)
                for i in xrange(length):
                    #print('i:%d'%i)
                    tmp = info[key][i]
                    size = tmp[2]
                    md5 = tmp[3]
                    name = tmp[4]
                    rom_type = get_rom_type(name)
                    body = '%s%s %s MD5: %s\n%s%s \n\n' % (body, rom_type, size, md5, url_head, name)
                body += '—————————————————————————————————————————————————— \n\n'
        m_url = head + body + end
    return m_url


def get_download_url(m_folder, version):
    """

    @param m_folder:
    @param version:
    @return xiaomi_url, redmi_url, pad_url:
    @summary 获得to_get_url 中组合得到的url
    """
    info_xiaomi, info_redmi, info_pad = walk_dir(m_folder)
    # info = walk_dir(m_folder))
    xiaomi_url = to_get_url(info_xiaomi, version)
    redmi_url = to_get_url(info_redmi, version)
    pad_url = to_get_url(info_pad, version)
    return xiaomi_url, redmi_url, pad_url


def get_op_idx(file_name):
    """

    @param file_name:
    @return op_idx:
    @summary 获取运营商类型的idx
    """
    op_idx = -1
    name = str.lower(file_name)
    for i in xrange(len(Ops_Types)):
        op = Ops_Types[i][0]
        if op in name:
            op_idx = i
            break
        else:
            continue
    return op_idx


def get_area_type(file_name):
    """

    @param file_name:
    @return area:
    @summary 返回区域
    """
    area = ''
    for i in xrange(len(Area_Types)):
        flag1 = Area_Types[i][0]
        flag2 = Area_Types[i][1]
        if flag1 in file_name or flag2 in file_name:
            area = Area_Types[i][2]
            break
        else:
            continue
    return area


def get_dev_type(file_name):
    """

    @param file_name:
    """
    dev_type = ''
    dev_version = r'[0-9]{1}\.[0-9]{1,2}\.[0-9]{1,2}\_'
    stable_version = r'[A-Z]{3,7}[0-9]{1,2}\.[0-9]{1,2}\_'
    origin_version = r'[A-Z]{3}[0-9]{2}\_'
    pattern_dev = re.compile(dev_version)
    pattern_stable = re.compile(stable_version)
    pattern_origin = re.compile(origin_version)

    op_idx = get_op_idx(file_name)
    op_name = ''
    if op_idx != -1:
        op_name = Ops_Types[op_idx][1]
    if op_name != '':
        print('op_name=%s' % op_name)

    dev_search_result = re.findall(pattern_dev, file_name)
    stable_search_result = re.findall(pattern_stable, file_name)
    origin_search_result = re.findall(pattern_origin, file_name)
    find_type = False
    result = False
    if dev_search_result:
        find_type = 'dev.'
        result = dev_search_result
        if 'alpha' in file_name:
            dev_type = Dev_Types[0]
        else:
            dev_type = Dev_Types[1]
    elif stable_search_result:
        find_type = 'stable.'
        result = stable_search_result
        dev_type = Dev_Types[2]
    elif origin_search_result:
        find_type = 'origin.'
        result = origin_search_result
        dev_type = Dev_Types[3]
    else:
        print('Not find.')

    if result and find_type:
        print(find_type)
        print(result)

    area = get_area_type(file_name)
    if area != '':
        dev_type = area + dev_type

    if op_name != '':
        dev_type = op_name

    return dev_type