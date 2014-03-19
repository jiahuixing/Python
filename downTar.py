__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

import time
import sys
import urllib
import re

MAIN_PAGE = 'http://ota.n.miui.com/ota/'

CHOOSE_T_SYS = 'sys.argv'
CHOOSE_T_IN = 'input'

DOWNLOAD = 'wget '

X1 = 'mione_plus_'
X2 = 'aries_'
X2_ALPHA = 'aries_alpha_'
X2A = 'taurus_'
X2A_ALPHA = 'taurus_alpha_'
X3_TD = 'pisces_'
X3_W = 'cancro_'
HM2_TD = 'wt93007_'
HM2_W = 'HM2013023_'

MID = 'images_'

CHOOSE = [X1, X2, X2_ALPHA, X2A, X2A_ALPHA, X3_TD, X3_W, HM2_TD, HM2_W]

IMAGES_SUF = r'_4\.[0-9]{1}_[a-zA-Z0-9]{10}'

SUFFIX = '.tgz'


def debug(msg):
    print('******%s******' % msg)


def get_date():
    if len(sys.argv) > 1:
        version = sys.argv[1]
    else:
        block = '.'
        year, mon, day = time.strftime('%Y'), time.strftime('%m'), time.strftime('%d')
        year = year[-1]
        mon = str(int(mon))
        day = str(int(day))
        version = year + block + mon + block + day
    return version


def down_tgz():
    """

    @summary 下载tgz
    """
    version = get_date()
    web = urllib.urlopen(MAIN_PAGE).read()

    if version in web:
        debug('Find version.')
        judge_input(CHOOSE_T_SYS)
        num = choose_num
        debug('num=%s' % num)
        if num:
            page = MAIN_PAGE + version
            debug(page)
            web = urllib.urlopen(page).readlines()
            for line in web:
                if '.tgz' in line:
                    # debug(line)
                    tar = find_tar(num, line)
                    if tar:
                        print('tar=%s' % tar)
                        break
    else:
        debug('Version not found.')


def find_tar(num, line):
    choose = CHOOSE[num - 1]
    version = get_date()
    tar_name = choose + MID + version + IMAGES_SUF + SUFFIX
    # debug('tar_name=%s' % tar_name)
    pat = re.compile(tar_name)
    result = re.search(pat, line)
    if result:
        debug('find it')
        tar = result.group()
    else:
        #debug('cant find it')
        tar = ''
    return tar


def judge_input(choose_type=CHOOSE_T_IN):
    debug(choose_type)
    try:
        if len(CHOOSE) > 9:
            read_len = 2
        else:
            read_len = 1
        if len(sys.argv) > 2 and choose_type == CHOOSE_T_SYS:
            m_input = sys.argv[2][:read_len]
        else:
            info = (
                '''Pls choose the num to down the tar:
1.mione
2.aries
3.aries_alpha
4.taurus
5.taurus_alpha
6.pisces
7.cancro
8.wt93007
9.HM2013023
        ''')
            print(info)
            m_input = sys.stdin.read(read_len)
        if m_input.isdigit():
            m_input = int(m_input)
            if m_input in range(1, len(CHOOSE) + 1):
                debug('m_input=%s' % m_input)
                set_num(m_input)
            else:
                debug('Pls input num in %s--%s.' % (1, len(CHOOSE)))
                judge_input()
        else:
            debug('Not a valid num,pls re input')
            judge_input()
    except KeyboardInterrupt:
        debug('Interrupt')


def get_num():
    return choose_num


def set_num(num):
    global choose_num
    choose_num = num


down_tgz()
