#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/2/24 6:39
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import re


def addhead(re_check, head):
    re_check_o = re.compile(re_check)

    def _(file, code, config):
        if not re_check_o.match(file) is None:
            return file, head + code
        return file, code

    return _
