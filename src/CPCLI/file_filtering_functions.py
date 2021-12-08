#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/2/25 3:59
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import re


def types(types):
    u"""
    文件类型过滤器
    * 例子
        file_filtering_functions = [
            types(['py', 'pyz', 'pyd', 'pyo', 'dll', 'exe', 'png', 'jpg', 'json'])
        ]


    :param types:
    :type types: list
    :return:
    """
    re_o = re.compile(r".*\.({})$".format("|".join(types)), flags=re.IGNORECASE)

    def _(file, config):
        if re_o.match(file) is None:
            return False
        return True

    return _


def noTypes(*args):
    v = types(*args)
    return lambda *args: not v(*args)
