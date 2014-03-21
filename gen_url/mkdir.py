# -*- coding: utf-8 -*-

from gen_url.my_libs import *

BLOCK = ' '
PYTHON_FILE_PATH = '/data/files'
USER_OTA_PATH = '/data/ota/'
ENG_PATH = '/data/eng/'


def get_version_type():
    """


    @return:
    @summary 获取版本类型
    """
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


def create_path():
    """

    @summary 创建目录
    """
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
    """

    @summary 移动文件到目录
    """
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


if __name__ == '__main__':
    for i in xrange(len(Rom_Properties)):
        print('i=%s,i_length=%s' % (i, len(Rom_Properties[i])))
    create_path()
    move_files_paths()
    generate = Generate()
    xiaomi_url, redmi_url, pad_url = get_download_url(generate.m_folder, generate.m_version)
    print('###################################################################\n')
    if xiaomi_url != '':
        print(xiaomi_url)
    if redmi_url != '':
        print(redmi_url)
    if pad_url != '':
        print(pad_url)
    print('###################################################################\n')
