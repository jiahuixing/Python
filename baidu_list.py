__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

import os
import sys
import thread

DEVICES = []


def getDeviceList():
    """
    获取device list
    """
    adb_cmd_devices = 'adb devices'
    po = os.popen(adb_cmd_devices)
    i = 0
    for line in po.readlines():
        line = line.strip('\r').strip('\n')
        if line != '':
            line = line.split()
            if len(line) == 2:
#                i += 1
#                print('i=%d'%i)
#                print(line)
                DEVICES.append(line[0])
    print(DEVICES)

def log(device_id):
    """
    读取logcat
    """
    adb_cmd_clear_log = 'adb -s ' + device_id + ' logcat -c'
    adb_cmd_logcat = 'adb -s ' + device_id + ' logcat -v time | grep -E "SyncPlaylist|BaiduSdkManager|SyncDBManager|XiaomiConstants|CacheDBHelper|LogUtil|HttpHelper"'
    print(device_id)


def testThread():
    """

        """
    num = len(DEVICES)
    if num > 0:
        for i in xrange(num):
            device_id = DEVICES[i]
            print('i=%d,device_id=%s'%(i,device_id))
            thread.start_new_thread(log,(device_id,i))

getDeviceList()
testThread()




