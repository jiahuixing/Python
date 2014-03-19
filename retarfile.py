__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

import os
import sys
import re


TAR_XVF = 'tar xvf '
TAR_CVF = 'tar cvf '
RM = 'rm -r '

ARIES = 'aries'
TAURUS = 'taurus'

CP_ARIES = 'cp home/builder/jb-aries-operator-bak/'
CP_TAURUS = 'cp home/builder/jb-taurus-operator-bak/'

USER_DATA_PRE = [
    'aries_chinatelecom_images_',
    'aries_chinaunicom_images_',
    'taurus_chinaunicom_images_',
]
USER_DATA_SUF = '_4.1.tar'

IMAGES_PRE = [
    'aries_images_',
    'taurus_images_',
]
IMAGES_SUF = r'_4.1_[a-zA-Z0-9]{10}.tar'

OP_CT = 'chinatelecom'
OP_CU = 'chinaunicom'


def debug(msg):
    print('******%s******' % msg)


def get_version():
    if len(sys.argv) > 1:
        folder = sys.argv[1]
        folder = str.split(folder, '/')
        version = folder[3]
        return version
    else:
        debug('请输入版本号(如：“/data/ota/JLB25.0/ ”)')


def find_image(version, device_type):
    image = ''
    image_pre = ''
    if device_type == ARIES:
        image_pre = IMAGES_PRE[0]
    elif device_type == TAURUS:
        image_pre = IMAGES_PRE[1]
    full = image_pre + version + IMAGES_SUF
    debug('full=%s' % full)
    ls_read = os.popen('ls').readlines()
    pat = re.compile(full)
    for i in xrange(len(ls_read)):
        line = ls_read[i].strip('\r').strip('\n')
        if 'tar' in line and device_type in line and version in line:
            m = pat.search(line)
            if m:
                image = line
                break
    if image:
        debug('image=%s' % image)
    return image


def extract_tar(file_name):
    extract = TAR_XVF + file_name
    debug('extract=%s' % extract)
    os.system(extract)


def compress_tar(version, device_type, operator):
    compress = ''
    if device_type == TAURUS:
        compress = TAR_CVF + 'taurus_' + operator + '_images_' + version + '_4.1.tar ' + 'taurus_' + operator + '_images_' + version + '_4.1'
    elif device_type == ARIES:
        compress = TAR_CVF + 'aries_' + operator + '_images_' + version + '_4.1.tar ' + 'aries_' + operator + '_images_' + version + '_4.1'
    debug('compress=%s' % compress)
    if compress:
        os.system(compress)


def cp_user_date(version, device_type):
    cp = ''
    if device_type == TAURUS:
        cp = CP_TAURUS + version + '/userdata.img taurus_images_' + version + '_4.1/images/'
    elif device_type == ARIES:
        cp = CP_ARIES + version + '/userdata.img  aries_images_' + version + '_4.1/images/'
    debug('cp=%s' % cp)
    if cp:
        os.system(cp)


def rename_folder(version, device_type, operator):
    rename = ''
    if device_type == TAURUS:
        rename = 'mv taurus_images_' + version + '_4.1 ' + 'taurus_' + operator + '_images_' + version + '_4.1'
    elif device_type == ARIES:
        rename = 'mv aries_images_' + version + '_4.1 ' + 'aries_' + operator + '_images_' + version + '_4.1'
    if rename:
        debug('rename=%s' % rename)
        os.system(rename)


def rm_folder(version, device_type, operator):
    rm_data = RM + 'home/'
    rm_image = RM
    debug('rm_data=%s' % rm_data)
    os.system(rm_data)
    if device_type == TAURUS:
        rm_image = RM + 'taurus_' + operator + '_images_' + version + '_4.1/'
    elif device_type == ARIES:
        rm_image = RM + 'aries_' + operator + '_images_' + version + '_4.1/'
    if rm_image != RM:
        debug('rm_image=%s' % rm_image)
        os.system(rm_image)


def run_script():
    version = get_version()
    if version:
        for i in xrange(len(USER_DATA_PRE)):
            debug('i=%d' % i)
            user_data_pre = USER_DATA_PRE[i]
            user_data = user_data_pre + version + USER_DATA_SUF
            debug('user_data=%s' % user_data)
            #机型
            device_type = ''
            if ARIES in user_data:
                device_type = ARIES
            elif TAURUS in user_data:
                device_type = TAURUS
            debug('device_type=%s' % device_type)
            #运营商
            operator = ''
            if OP_CT in user_data:
                operator = OP_CT
            elif OP_CU in user_data:
                operator = OP_CU
            debug('operator=%s' % operator)
            image = find_image(version, device_type)
            if image:
                extract_tar(user_data)
                extract_tar(image)
                cp_user_date(version, device_type)
                rename_folder(version, device_type, operator)
                compress_tar(version, device_type, operator)
                rm_folder(version, device_type, operator)
            else:
                debug('未找到image.')


run_script()
