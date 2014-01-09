__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

import sys
import urllib
import time

MAIN_PAGE = 'http://ota.n.miui.com/ota/'

CHOOSE_T_SYS = 'sys.argv'
CHOOSE_T_IN = 'input'

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


def getDate():
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


def downTar():
    '''
    open url
    '''
    version = getDate()
    web = urllib.urlopen(MAIN_PAGE).read()

    if version in web:
        choose_num = judgeInput(CHOOSE_T_SYS)
        print('choose_num=%s' % choose_num)
        if choose_num:
            print('222222222222222222')
    else:
        print('Version not found.')


def judgeInput(choose_type=CHOOSE_T_IN):
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
                print('m_input=%s' % m_input)
                return m_input
            else:
                print('not valid')
                judgeInput()
        else:
            print('not num')
            judgeInput()
    except KeyboardInterrupt:
        print('Interrupt')


downTar()