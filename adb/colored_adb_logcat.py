# !/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

import os
import sys


class COLOR:
    WHITE = '\033[37m'
    GRAY = '\033[30m'
    BLUE = '\033[34m'
    GREEN = '\033[92m'
    YELLOW = '\033[33m'
    RED = '\033[91m'
    ENDC = '\033[1;m'


adb_args = ' '.join(sys.argv[1:])

if os.isatty(sys.stdin.fileno()):
    input_source = os.popen("adb logcat %s" % adb_args)
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
        if line[0] == 'E':
            out_color = COLOR.RED
        elif line[0] == 'D':
            out_color = COLOR.BLUE
        elif line[0] == 'V':
            out_color = COLOR.WHITE
        elif line[0] == 'W':
            out_color = COLOR.YELLOW
        elif line[0] == 'I':
            out_color = COLOR.GREEN
        line = line.strip()
        print out_color + line + COLOR.ENDC