#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/2/21 6:39
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

* 一个例子
import re
import CPCLI.core as cli_core
from CPCLI.utils import decode
from CPCLI.overall_processing_function import group
from CPCLI.processing_function import addhead

class Config(object):
    # 文件过滤函数
    file_filtering_functions = [
        lambda file, config: re.match(r".*pyc$", file) is None
    ]
    # 整体处理函数
    overall_processing_function = [
        group(
            name="TOOLS_2021_2_24",
            exec_script=u'''\
import main
from main import main
main()'''
        )
    ]
    # 处理函数
    processing_function = [
        addhead(r".*\.py$", "# window\n")
    ]
    debug = True

    class Path(object):
        root = r"你的根路径"
        src = root + r"\src"
        scripts = root + r"\scripts"
        build = root + r"\build"


cli_core.build(Config)

"""
