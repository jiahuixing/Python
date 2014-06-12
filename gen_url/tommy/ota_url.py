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

    def __init__(self):
        self.get_version_and_folder()

    def get_version_and_folder(self):
        if len(sys.argv) >= 3:
            argv_2 = str.rstrip(sys.argv[1], '/')
            argv_3 = str.rstrip(sys.argv[2], '/')
            count = str.count(argv_2, '/')
            if count >= 3:
                main_url = 'http://ota.n.miui.com'
                self.main_url = main_url
                split_list = str.split(argv_2, '/')
                m_folder = split_list[-1]
                self.m_folder = m_folder
                m_sub_address = split_list[-2]
                self.m_sub_address = m_sub_address
                work_path = str.replace(argv_2, m_folder, '', 1)
                self.work_path = work_path
                m_version = argv_3
                self.m_version = m_version
                debug_msg(color_msg(
                    'argv_2 = %s\nargv_3=\n'
                    'count = %s\nsplit_list = %s\n'
                    'm_folder = %s\nm_sub_address = %s\nwork_path = %s\n'
                    'm_version = %s\n' % (
                        argv_2, count, split_list, m_folder, m_sub_address, work_path, m_version)))
            else:
                debug_msg(color_msg('请使用正确的参数\n例:python ota_url.py /data/eng/4.6.11-internal 4.6.11'))
                sys.exit()
        else:
            debug_msg(color_msg('请使用正确的参数\n例:python ota_url.py /data/eng/4.6.11-internal 4.6.11'))
            sys.exit()


if __name__ == '__main__':
    start_time = time.time()
    try:
        for i in xrange(len(Rom_Properties)):
            model_type = Model_Types[i]
            debug_msg(color_msg('i:%s\n机型:%s\n数量:%s' % (i, model_type, len(Rom_Properties[i]))))
        generate = Generate()
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


