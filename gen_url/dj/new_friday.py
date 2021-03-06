# !/usr/local/bin/python -u
# -*- coding: utf-8 -*-
import sys

__author__ = 'jiahuixing'

from friday_lib import *


class Generate:
    # m_folder = ''
    m_version = ''

    def __init__(self):
        # self.get_folder()
        self.get_version()

    # def get_folder(self):
    #     length = len(sys.argv)
    #     if length >= 2:
    #         m_folder = sys.argv[1]
    #     else:
    #         m_folder = get_date()
    #     self.m_folder = m_folder

    def get_version(self):
        if len(sys.argv) >= 2:
            # if len(sys.argv) >= 3:
            # version = sys.argv[1]
            version = str.replace(sys.argv[1], '/', '')
        else:
            version = get_date()
        self.m_version = version


if __name__ == '__main__':
    start_time = time.time()

    for i in xrange(len(Rom_Properties)):
        print('i=%s,i_length=%s' % (i, len(Rom_Properties[i])))
    generate = Generate()
    debug_msg('m_version=%s' % generate.m_version)
    xiaomi_url, redmi_url, pad_url = get_download_url(generate.m_version)

    print_url(xiaomi_url)
    print_url(redmi_url)
    print_url(pad_url)

    write_url(xiaomi_url, redmi_url, pad_url)

    end_time = time.time()
    cost_time = int(end_time - start_time)
    debug_msg('cost_time = %s seconds.' % cost_time)


