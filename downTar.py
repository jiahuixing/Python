__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

import os
import time
import sys
import urllib
import urllib2

MAIN_PAGE = 'http://ota.n.miui.com/ota/'

def debug(msg):
    print('******%s******'%msg)

def getDate():
    block = '.'
    year,mon,day= time.strftime('%Y'),time.strftime('%m'),time.strftime('%d')
    year = year[-1]
    mon = str(int(mon))
    day = str(int(day))
    mDate = year + block + mon + block + day
    return mDate

def downTar():
    '''
    open url
    '''
    if len(sys.argv) > 1:
        version = sys.argv[1]
    else:
        version = getDate()

    web = urllib.urlopen(MAIN_PAGE).read()

    if version in web:
        debug('Find version.')
        page = MAIN_PAGE + version
        web = urllib.urlopen(page).read()

    else:
        debug('Version not found.')

downTar()



