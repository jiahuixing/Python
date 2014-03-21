__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

from my_libs import *


def test1():
    m_folder = sys.argv[1]
    for root, dirs, files in os.walk(m_folder):
        for file_name in files:
            print(file_name)
            dev_type = get_dev_type(file_name)
            print(dev_type)


def test2():
    dev_version = r'[0-9]{1}\.[0-9]{1,2}\.[0-9]{1,2}\_'
    dev_pattern = re.compile(dev_version)
    string = 'dasdadadsasd4.5.12_dasdasdweqweqw5.6.7222_dasdadsdasdad7.2.3_dasdasdasdas1.3.3_asdasdasdas'
    dev_search_result = re.findall(dev_pattern, string)
    if dev_search_result:
        print(dev_search_result)


test1()
print('#########################################################')
test2()


