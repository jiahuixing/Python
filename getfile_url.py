# -*- coding: utf-8 -*-

from my_libs import *


class Generate:
    m_folder = ''

    def __init__(self):
        self.get_folder()

    def get_folder(self):
        block = '.'
        argv_len = len(sys.argv)
        if argv_len >= 2:
            m_folder = sys.argv[1]
        else:
            year, mon, day = time.strftime('%Y'), time.strftime('%m'), time.strftime('%d')
            year = year[-1]
            mon = str(int(mon))
            day = str(int(day))
            m_folder = year + block + mon + block + day
        self.m_folder = m_folder

    def get_download_url(self):

        m_folder = self.m_folder
        info = walk_dir(m_folder)
        version = get_version()
        m_url = ''
        body = ''
        head = '【升级提醒】\n—————————————————————————————————————————————————— \n\n'
        end = ' '
        url_head = 'http://ota.n.miui.com/ota/' + version + '/'
        if {} != info:
            for key in info.keys():
                if key != '':
                    #print('key:%s'%key)
                    length = len(info[key])
                    #print('length:%s'%length)
                    idx = info[key][0][0]
                    c_name = Rom_Properties[idx][1]
                    body += "%s %s\n\n" % (c_name, version)
                    for i in xrange(length):
                        #print('i:%d'%i)
                        tmp = info[key][i]
                        size = tmp[1]
                        md5 = tmp[2]
                        name = tmp[3]
                        rom_type = get_rom_type(name)
                        body = '%s%s %s MD5: %s\n%s%s \n\n' % (body, rom_type, size, md5, url_head, name)
                    body += '—————————————————————————————————————————————————— \n\n'
            m_url = head + body + end
        return m_url


if __name__ == '__main__':
    print('total=%s' % len(Rom_Properties))
    generate = Generate()
    url = generate.get_download_url()
    print url
