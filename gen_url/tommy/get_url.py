# !/usr/local/bin/python -u
# -*- coding: utf-8 -*-
import sys

__author__ = 'jiahuixing'

from get_url_lib import *


class Generate:
    m_folder = ''
    m_version = ''
    work_path = ''

    def __init__(self):
        self.get_version_and_folder()

    def get_version_and_folder(self):
        if len(sys.argv) >= 2:
            arg = str.rstrip(sys.argv[1], '/')
            count = str.count(arg, '/')
            if count == 3:
                tmp_list = str.split(arg, '/')
                m_version = tmp_list[-1]
                self.m_version = m_version
                m_folder = tmp_list[-2]
                self.m_folder = m_folder
                work_path = str.replace(arg, m_version, '', 1)
                self.work_path = work_path
                debug_msg(color_msg('arg=%s\ncount=%s\ntmp_list=%s\nm_version=%s\nm_folder=%s\nwork_path=%s\n' % (
                    arg, count, tmp_list, m_version, m_folder, work_path)))
            else:
                debug_msg(color_msg('请输入含有版本号的文件夹 例: /data/ota/4.6.11/'))
                sys.exit()
        else:
            debug_msg(color_msg('请输入含有版本号的文件夹 例: /data/ota/4.6.11/'))
            sys.exit()


if __name__ == '__main__':
    start_time = time.time()
    for i in xrange(len(Rom_Properties)):
        model_type = Model_Types[i]
        debug_msg('i:%s,机型:%s,数量:%s' % (i, model_type, len(Rom_Properties[i])))
    generate = Generate()
    xiaomi_url, redmi_url, pad_url = get_download_url(generate)

    print_url(xiaomi_url)
    print_url(redmi_url)
    print_url(pad_url)

    write_url(xiaomi_url, redmi_url, pad_url, generate)

    end_time = time.time()
    cost_time = int(end_time - start_time)
    debug_msg('cost_time = %s seconds.' % cost_time)


