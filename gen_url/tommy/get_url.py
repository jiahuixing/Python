# !/usr/local/bin/python -u
# -*- coding: utf-8 -*-
import sys

__author__ = 'jiahuixing'

from gen_url.tommy.get_url_lib import *


class Generate:
    m_version = ''

    def __init__(self):
        self.get_version()

    def get_version(self):
        if len(sys.argv) >= 2:
            version = str.replace(sys.argv[1], '/', '')
        else:
            version = get_date()
        self.m_version = version


if __name__ == '__main__':
    start_time = time.time()
    for i in xrange(len(Rom_Properties)):
        model_type = Model_Types[i]
        debug_msg('i:%s,机型:%s,数量:%s' % (i, model_type, len(Rom_Properties[i])))
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


