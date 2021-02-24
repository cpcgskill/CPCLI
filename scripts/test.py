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
from CPCLI.overall_processing_function import group
from CPCLI.file_filtering_functions import noTypes
from CPCLI.processing_function import deleteBlankLines, deleteUselessStrings


class Config(object):
    # 文件过滤函数
    file_filtering_functions = [
        noTypes(['pyc'])
    ]
    # 整体处理函数
    overall_processing_function = [
        group(
            name=u"TOOLS_2021_2_24",
            exec_script=u'''\
import main
from main import main
main()'''
        )
    ]
    # 处理函数
    processing_function = [
        deleteBlankLines,
        deleteUselessStrings
    ]
    debug = True

    class Path(object):
        root = r"D:\Development\CPCLI\test"
        src = root + r"\src"
        scripts = root + r"\scripts"
        build = root + r"\build"


cli_core.build(Config)
