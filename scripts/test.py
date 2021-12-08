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
from __future__ import unicode_literals, print_function
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
            name=u"TOOL_NAME",
            exec_script=u'''\
# 以下是启动脚本
import main
from main import main
main()'''
        )
    ]
    # 处理函数
    processing_function = [
        # 清除空行
        deleteBlankLines,
        # 清除无用字符串
        deleteUselessStrings
    ]
    # 可真可假影响不大
    debug = True

    class Path(object):
        root = r"项目根目录"
        src = root + r"\src"
        scripts = root + r"\scripts"
        build = root + r"\build"


cli_core.build(Config)