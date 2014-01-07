__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

import os
import time
import sys
import urllib
import re

MAIN_PAGE = 'http://ota.n.miui.com/ota/'

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

CHOOSE = [X1,X2,X2_ALPHA,X2A,X2A_ALPHA,X3_TD,X3_W,HM2_TD,HM2_W]

IMAGES_SUF = r'_4.[0-9]{1}_[a-zA-Z0-9]{10}.tar'

def debug(msg):
    print('******%s******'%msg)

def getDate():
    if len(sys.argv) > 1:
        version = sys.argv[1]
    else:
        block = '.'
        year,mon,day= time.strftime('%Y'),time.strftime('%m'),time.strftime('%d')
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
        debug('Find version.')
        page = MAIN_PAGE + version
        web = urllib.urlopen(page).readlines()
        for line in web:
            if '.tar' in line:
                tar = findTar1(2,line)
                if tar:
                    print('tar=%s'%tar)
                    break
    else:
        debug('Version not found.')

def findTar():
    info = '''Pls choose the num to down the tar:
1.mione
2.aries
3.aries_alpha
4.taurus
5.taurus_alpha
6.pisces
7.cancro
8.wt93007
9.HM2013023
    '''
    print(info)
    m_input = sys.stdin.read(1)
    if m_input.isdigit():
        m_input = int(m_input)
        if m_input in range(1,9):
            choose = CHOOSE[m_input-1]
            version = getDate()
            tar_name = choose + MID + version + IMAGES_SUF
            print(tar_name)
            pat = re.compile(tar_name)
            print('pat=%s'%pat)
            tmp = 'aries_images_'+ version + '_4.1_eb18afb0ac.tar'
            print('tmp=%s'%tmp)
            if re.findall(pat,tmp):
                print(1)
            else:
                print(2)
        else:
            print('******wrong num******')
            findTar()
    else:
        print('******input wrong******')
        findTar()


def findTar1(num,line):
    choose = CHOOSE[num-1]
    version = getDate()
    tar_name = choose + MID + version + IMAGES_SUF
#    print(tar_name)
    pat = re.compile(tar_name)
#    print('pat=%s'%pat)
#    print('line=%s'%line)
    #result = re.findall(pat,line)
    result = re.search(pat,line)
    if result:
        print('******find it******')
        tar = result.group()
    else:
        print('******cant find it******')
        tar = ''
    return  tar


downTar()



