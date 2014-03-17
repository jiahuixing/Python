# -*- coding: utf-8 -*-

from my_libs import *


BLOCK = ' '
PYTHON_FILE_PATH = '/data/files'
USER_OTA_PATH = '/data/ota/'
ENG_PATH = '/data/eng/'

DEV_MIUI = 'miui_'
ZIP = 'zip'
DEV_IMAGES = '_images_'
TAR = 'tgz'
STABLE_MIUI = 'J'
ORIGIN = 'N'


def walk_dir(m_folder, topdown=True):
    info = dict()
    for root, dirs, files in os.walk(m_folder, topdown):
        for file_name in files:
            tmp = []
            print os.path.abspath(file_name)
            if Rom_Types[0][0] in file_name or Rom_Types[1][0] in file_name or Rom_Types[2][0] in file_name:
                idx, str_idx = get_rom_idx(file_name)
                print('idx=%s' % idx)
                if str_idx != "0":
                    size = get_rom_size(os.path.join(root, file_name))
                    md5 = get_file_md5(os.path.join(root, file_name))
                    tmp.append(idx)
                    tmp.append(size)
                    tmp.append(md5)
                    tmp.append(file_name)
                    # print(tmp)
                    keys = info.keys()
                    # print(keys)
                    if str_idx not in keys:
                        info[str_idx] = []
                        info[str_idx].append(tmp)
                    else:
                        info[str_idx].append(tmp)
                else:
                    print('Not in Rom_Types list.')
            else:
                print('Not valid "zip,tar,tgz" files.')

    return info


def get_version_type():
    num_letter = 0
    input_type = 0
    if len(sys.argv) < 2:
        num_letter = 1
        input_type = 0
    else:
        version = str(sys.argv[1])
        nums = '0123456789'
        letters = 'abcdefghijklmnopqrstuvwxyz'
        num_length = len(nums)
        letter_length = len(letters)
        # print('num_length=%d'%num_length)
        # print('letter_length=%d'%letter_length)
        if num_letter == 0:
            for i in xrange(num_length):
                num = nums[i]
                # print('num=%s'%num)
                if version.startswith(num):
                    num_letter = 1
                    input_type = 0
                    break
                else:
                    continue
        if num_letter == 0:
            for j in xrange(letter_length):
                letter = letters[j].upper()
                # print('letter=%s'%letter)
                if version.startswith(letter):
                    num_letter = 1
                    input_type = 1
                    break
                else:
                    continue
    if num_letter == 1:
        # print('input_type=%d'%input_type)
        return input_type
    else:
        get_version_type()


def get_path_names():
    length = len(sys.argv)
    if length >= 2:
        # print('argvs >= 2')
        version = sys.argv[1]
    else:
        # print('argvs < 2')
        version = get_date()
    internal_version = version + '-internal'
    return version, internal_version


def create_path():
    cwd = str(os.getcwd()).strip('\n').strip('\r')
    version, internal_version = get_path_names()
    version_type = get_version_type()
    if cwd == PYTHON_FILE_PATH:
        print('File path correct,begin to create path.')
        if not os.path.exists(version):
            print('Path %s is not exist' % version)
            os.mkdir(version)
        else:
            print('Path %s is already exist' % version)
        if version_type == 0:
            if not os.path.exists(internal_version):
                print('Path %s is not exist' % internal_version)
                os.mkdir(internal_version)
            else:
                print('Path %s is already exist' % internal_version)
    else:
        print('Pls move this python file to path:%s.' % PYTHON_FILE_PATH)


def move_files_paths():
    cwd = str(os.getcwd()).strip('\n').strip('\r')
    version, internal_version = get_path_names()
    version_type = get_version_type()
    if cwd == PYTHON_FILE_PATH:
        move_internal = 'mv *internal* ' + internal_version
        move_other = 'mv *' + version + '*.zip* *' + version + '*.tgz* ' + version
        if version_type == 0:
            print('Move internal files to path:%s.' % internal_version)
            os.system(move_internal)
            print('Move xml files to path:%s.' % internal_version)
            mv_xml = 'mv *' + version + '*.xml ' + internal_version
            os.system(mv_xml)
        elif version_type == 1:
            mv_xml = 'mv *' + version + '*.xml ' + version
            os.system(mv_xml)
        print('Move zip and tgz files to path:%s.' % version)
        os.system(move_other)
        move_user_ota = 'mv ' + version + BLOCK + USER_OTA_PATH
        print('Move ota path to path:%s.' % USER_OTA_PATH)
        os.system(move_user_ota)
        if version_type == 0:
            move_eng = 'mv ' + internal_version + BLOCK + ENG_PATH
            print('Move internal path to path:%s.' % ENG_PATH)
            os.system(move_eng)
    else:
        print('Pls move this python file to path:%s.' % PYTHON_FILE_PATH)


def write_print_format(version, msg):
    read_mode = 'w'
    file_name = version + '-url.txt'
    file_obj = open(file_name, read_mode)
    file_obj.write(msg)
    file_obj.close()


class Generate:
    m_folder = ''
    m_version = ''

    def __init__(self):
        self.get_version()
        self.get_folder()

    def get_folder(self):
        argv_len = len(sys.argv)
        if argv_len >= 2:
            m_folder = sys.argv[1]
        else:
            m_folder = get_date()
        self.m_folder = USER_OTA_PATH + m_folder

    def get_version(self):
        if len(sys.argv) >= 2:
            version = sys.argv[1]
        else:
            version = get_date()
        self.m_version = version

    def get_download_url(self):

        m_folder = self.m_folder
        info = walk_dir(m_folder)
        version = self.m_version
        m_url = ''
        body = ''
        head = '【升级提醒】\n—————————————————————————————————————————————————— \n\n'
        end = ' '
        url_head = 'http://ota.n.miui.com/ota/' + version + '/'
        if info:
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
    create_path()
    move_files_paths()
    generate = Generate()
    url = generate.get_download_url()
    print url
    #write_print_format(generate.mVersion,url)

