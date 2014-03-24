# -*- coding: utf-8 -*-

from my_libs import *


class Generate:
    m_folder = ''
    m_version = ''

    def __init__(self):
        self.get_folder()
        self.get_version()

    def get_folder(self):
        argv_len = len(sys.argv)
        if argv_len >= 2:
            m_folder = sys.argv[1]
        else:
            m_folder = get_date()
        self.m_folder = m_folder

    def get_version(self):
        if len(sys.argv) >= 3:
            version = sys.argv[2]
        else:
            version = get_date()
        self.m_version = version


if __name__ == '__main__':
    start_time = time.time()
    for i in xrange(len(Rom_Properties)):
        debug_msg('i=%s,i_length=%s' % (i, len(Rom_Properties[i])))
    generate = Generate()
    xiaomi_url, redmi_url, pad_url = get_download_url(generate.m_folder, generate.m_version)
    if xiaomi_url != '':
        print(xiaomi_url)
    if redmi_url != '':
        print(redmi_url)
    if pad_url != '':
        print(pad_url)
    end_time = time.time()
    cost_time = int(end_time - start_time)
    debug_msg('start_time=%s,end_time=%s,cost_time=%s' % (start_time, end_time, cost_time))