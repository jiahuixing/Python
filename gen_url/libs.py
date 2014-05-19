#!/usr/local/bin/python -u
# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

COLOR_START = '\033[0;'
COLOR_END = '\033[0m'
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def color_msg(msg, fg=GREEN, bg=None):
    """

    @param msg:
    @param fg:
    @param bg:
    @return:
    """
    color = list()
    if fg is not None:
        color_fg = '3%d' % fg
        # debug_msg('color_fg=%s' % color_fg)
        color.append(color_fg)
    if bg is not None:
        color_bg = '4%d' % bg
        # debug_msg('color_bg=%s' % color_bg)
        color.append(color_bg)
    if len(color) > 0:
        color_str = ';'.join(color)
        # debug_msg(color)
        # debug_msg(color_str)
        msg = '%s%sm%s%s' % (COLOR_START, color_str, msg, COLOR_END)
    # if color == 2:
    #     return '%s%s%s%s%s' % (COLOR_START, color_fg, color_bg, msg, COLOR_END)
    return msg


def debug_msg(msg, flag=1):
    if flag == 1:
        print('---------------------------------')
        print(msg)