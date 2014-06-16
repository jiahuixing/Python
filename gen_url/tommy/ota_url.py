# !/usr/local/bin/python -u
# -*- coding: utf-8 -*-

__author__ = 'jiahuixing'

from ota_url_lib import *


class Generate:
    main_url = ''
    m_sub_address = ''
    m_folder = ''
    m_version = ''
    work_path = ''
    m_who = 0

    def __init__(self, m_options, m_who):
        self.m_options = m_options
        self.m_who = m_who
        self.get_version_and_folder()

    def get_version_and_folder(self):
        if self.m_who == 1:
            folder = self.m_options.tommy_ota_folder
            main_url = 'http://ota.n.miui.com'
        else:
            folder = self.m_options.dj_ota_folder
            main_url = 'http://bigota.d.miui.com'
        version = self.m_options.ota_version
        folder = str.rstrip(folder, '/')
        version = str.rstrip(version, '/')
        count = str.count(folder, '/')
        if count >= 3:
            self.main_url = main_url
            split_list = str.split(folder, '/')
            m_folder = split_list[-1]
            self.m_folder = m_folder
            m_sub_address = split_list[-2]
            self.m_sub_address = m_sub_address
            work_path = str.replace(folder, m_folder, '', 1)
            self.work_path = work_path
            m_version = version
            self.m_version = m_version
            debug_msg(color_msg(
                'folder = %s\nversion=%s\n'
                'count = %s\nsplit_list = %s\n'
                'm_folder = %s\nm_sub_address = %s\nwork_path = %s\n'
                'm_version = %s\n' % (
                    folder, version, count, split_list, m_folder, m_sub_address, work_path, m_version)))
        else:
            exp_msg = '正确的用法:\n1. python ota_url.py -t /data/eng/4.6.11-internal -v 4.6.11\n' \
                      '2. python ota_url.py -d /data/eng/4.6.11-internal -v 4.6.11'
            debug_msg(color_msg(exp_msg, RED))
            sys.exit()


if __name__ == '__main__':
    start_time = time.time()
    try:
        options = init_options()
        who = judge_options(options)
        if who != 0:
            generate = Generate(options, who)
            for i in xrange(len(Rom_Properties)):
                model_type = Model_Types[i]
                debug_msg(color_msg('i:%s\n机型:%s\n数量:%s' % (i, model_type, len(Rom_Properties[i]))))
            xiaomi_url, redmi_url, pad_url = get_download_url(generate)
            print_url(xiaomi_url)
            print_url(redmi_url)
            print_url(pad_url)
            write_url(xiaomi_url, redmi_url, pad_url, generate)
    except NameError:
        print('NameError')
        print(NameError)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        print(KeyboardInterrupt)
    except TypeError:
        print('TypeError')
        print(TypeError)
    finally:
        end_time = time.time()
        cost_time = int(end_time - start_time)
        debug_msg(color_msg('cost_time = %s seconds.' % cost_time))


