# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from libs import *
from data import *

CONST = {
    'block': ' ',
    'work_path': '/home/jiahuixing/music',
}


class Operate:
    adb_device_list = []

    def __init__(self):
        debug('init')
        while len(self.adb_device_list) == 0:
            self.adb_device_list = get_adb_device_list()
            if len(self.adb_device_list) == 0:
                debug('wait for 3 seconds.')
                time.sleep(3)

    def root_and_remount(self):
        """

        @summary 获取root remount权限
        """
        device_list = self.adb_device_list
        root_devices(device_list)
        remount_devices(device_list)

    def push_file(self, file_name, push_path):
        """

        @param file_name:
        @param push_path:
        @summary adb push文件file_name到目录push_path
        """
        device_list = self.adb_device_list
        work_path = CONST['work_path']
        block = CONST['block']
        os.chdir(work_path)
        push_command = 'adb -s %s push '
        reboot_command = 'adb -s %s reboot'
        for device in device_list:
            if os.path.exists(file_name):
                debug('file exists.')
                push_cmd = (push_command % device) + file_name + block + push_path
                reboot_cmd = reboot_command % device
                debug('%s\n%s\n' % (push_cmd, reboot_cmd))
                os.system(push_cmd)
                os.system(reboot_cmd)

    def delete_file(self, file_name, file_path):
        """

        @param file_name:
        @param file_path:
        @summary 从file_path删除文件file_name
        """
        delete_command = 'adb -s %s shell rm '
        reboot_command = 'adb -s %s reboot'
        device_list = self.adb_device_list
        for device in device_list:
            delete_cmd = (delete_command % device) + file_path + file_name
            reboot_cmd = reboot_command % device
            debug('%s\n%s\n' % (delete_cmd, reboot_cmd))
            os.system(delete_cmd)
            os.system(reboot_cmd)

    def push_apk(self, termini_path):
        """

        @param termini_path:
        @summary push Music apk到termini_path
        """
        rm_command = 'adb -s %s shell rm /system/app/Music.*'
        push_command = 'adb -s %s push'
        reboot_command = 'adb -s %s reboot'
        apk = ''
        work_path = CONST['work_path']
        block = CONST['block']
        os.chdir(work_path)
        path_files = os.listdir(work_path)
        for path_file in path_files:
            if path_file.endswith('.apk') and path_file.startswith('Music'):
                apk = path_file
                break
        if apk != '':
            debug(apk)
            device_list = self.adb_device_list
            for device in device_list:
                rm_cmd = rm_command % device
                push_cmd = (push_command % device) + block + apk + block + termini_path
                reboot_cmd = reboot_command % device
                debug('%s\n%s\n%s\n' % (rm_cmd, push_cmd, reboot_cmd))
                os.system(rm_cmd)
                os.system(push_cmd)
                os.system(reboot_cmd)

    def test_push(self, tag, attr):
        work_path = CONST['work_path']
        block = CONST['block']
        device_list = self.adb_device_list
        commands = read_xml_file(Tmp_File_Path, tag, attr)
        for device in device_list:
            debug(device)

    def flash_phone(self):
        device_list = self.adb_device_list
        debug(device_list)

    # noinspection PyMethodMayBeStatic
    def pull_apk_db(self):
        work_path = CONST['work_path']
        block = CONST['block']
        pull_command = 'adb -s %s pull /data/data/com.miui.player/databases/com_miui_player.db'
        to_path = '/home/jiahuixing/music/%s_com_miui_player.db'
        device_list = get_adb_device_list()
        for device in device_list:
            pull_cmd = (pull_command % device) + block + (to_path % device)
            debug(pull_cmd)
            os.system(pull_cmd)

