#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/2/21 7:59
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import re
import CPCLI.core as cli_core
from CPCLI.utils import decode
from CPCLI.processing.group import group

class Config(object):
    # 文件过滤函数
    file_filtering_functions = [
        lambda file, config: not re.match(r".*", file) is None
    ]
    # 整体处理函数
    overall_processing_function = [
        group
    ]
    # 处理函数
    processing_function = [
    ]
    debug = True

    class Path(object):
        src = r"D:\Development\CPCLI\test\src"
        scripts = r"D:\Development\CPCLI\test\scripts"
        build = r"D:\Development\CPCLI\test\build"

    class Group(object):
        name = "TTTT"
        exec_script = u'''\
import main
from main import main
main()'''


cli_core.build(Config)
