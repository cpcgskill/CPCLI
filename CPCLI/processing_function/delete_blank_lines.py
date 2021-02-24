#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/2/25 5:59
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import re

re_check = re.compile(r".*\.py$")


def deleteBlankLines(file, code, config):
    if not re_check.match(file) is None:
        code = code.replace("\r", "")
        code = "\r\n".join([i for i in code.split("\n") if len(i.replace(" ", "").replace("  ", "")) != 0])
    return file, code
