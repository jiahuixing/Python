# !/usr/local/bin/python -u
# -*- coding: utf-8 -*-

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
            argv = str.rstrip(sys.argv[1], '/')
            count = str.count(argv, '/')
            if count >= 3:
                split_list = str.split(argv, '/')
                m_version = split_list[-1]
                self.m_version = m_version
                m_folder = split_list[-2]
                self.m_folder = m_folder
                work_path = str.replace(argv, m_version, '', 1)
                self.work_path = work_path
                debug_msg(color_msg(
                    'argv = %s\ncount = %s\nsplit_list = %s\nm_version = %s\nm_folder = %s\nwork_path = %s\n' % (
                        argv, count, split_list, m_version, m_folder, work_path)))
            else:
                debug_msg(color_msg('请输入含有版本号的文件夹 例: /data/ota/4.6.11/'))
                sys.exit()
        else:
            debug_msg(color_msg('请输入含有版本号的文件夹 例: /data/ota/4.6.11/'))
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


