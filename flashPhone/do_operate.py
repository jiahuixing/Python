# -*- coding: utf-8 -*-
__author__ = 'jiahuixing'

from Operate import *


def opr():
    try:
        op = Operate()
        op.root_and_remount()
        info = '''
Input num:
1.push_file:%s to path:%s
2.delete_file:%s from path:%s
3.push apk to path:%s
4.pull db from phone to path:%s
        '''
        local_file_name = 'account_preview'
        push_termini_path = '/data/system/'
        rm_from_path = '/data/system/'
        apk_termini_path = '/system/app/Music.apk'
        db_termini_path = '/home/jiahuixing/music/'
        input_num = input(
            info % (
                local_file_name, push_termini_path, local_file_name, rm_from_path, apk_termini_path, db_termini_path))
        if isinstance(input_num, int):
            if input_num == 1:
                op.push_file(local_file_name, push_termini_path)
            elif input_num == 2:
                op.delete_file(local_file_name, rm_from_path)
            elif input_num == 3:
                op.push_apk(apk_termini_path)
            elif input_num == 4:
                op.pull_apk_db()
            else:
                print('Input wrong num:%s.' % input_num)
        else:
            print('Not a num:%s.' % input_num)
    except KeyboardInterrupt:
        print('KeyboardInterrupt.')
    except IOError:
        print('IOError.')
    except NameError:
        print('NameError.')


opr()