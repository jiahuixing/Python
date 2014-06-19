# !/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

import os
import sys
from optparse import OptionParser


def init_options():
    usage_msg = 'usage: %prog [options] arg'
    parser = OptionParser(usage=usage_msg)
    parser.add_option('-s', '--serial', dest='device_serial_num', help='device serial num')
    parser.add_option('-a', '--adb_args', dest='adb_args', help='adb args')
    (options, args) = parser.parse_args()
    return options


# noinspection PyClassHasNoInit
class COLOR:
    WHITE = '\033[37m'
    GRAY = '\033[30m'
    BLUE = '\033[34m'
    GREEN = '\033[92m'
    YELLOW = '\033[33m'
    RED = '\033[91m'
    ENDC = '\033[1;m'


m_options = init_options()

serial, adb_args = None, None
adb = 'adb logcat'
if m_options.device_serial_num is not None:
    serial = m_options.device_serial_num
if m_options.adb_args is not None:
    adb_args = m_options.adb_args
if serial is not None:
    if adb_args is not None:
        adb = 'adb -s %s logcat %s' % (serial, adb_args)
    else:
        adb = 'adb -s %s logcat' % serial
else:
    if adb_args is not None:
        adb = 'adb logcat %s' % adb_args
    else:
        adb = 'adb logcat'

# adb_args = ' '.join(sys.argv[1:])

if os.isatty(sys.stdin.fileno()):
    input_source = os.popen(adb)
else:
    input_source = sys.stdin

while True:
    try:
        line = input_source.readline()
    except KeyboardInterrupt:
        break

    if len(line) == 0:
        break
    else:
        out_color = COLOR.WHITE
        # if line[0] == 'E':
        if 'E/' in line:
            out_color = COLOR.RED
        # elif line[0] == 'D':
        elif 'D/' in line:
            out_color = COLOR.BLUE
        # elif line[0] == 'V':
        elif 'V/' in line:
            out_color = COLOR.WHITE
        # elif line[0] == 'W':
        elif 'W/' in line:
            out_color = COLOR.YELLOW
        # elif line[0] == 'I':
        elif 'I/' in line:
            out_color = COLOR.GREEN
        line = line.strip()
        print out_color + line + COLOR.ENDC