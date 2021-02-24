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

"""
import os
from CPCLI.utils import formattedPath, readFile, writeFile
import logging

logging.basicConfig(
    format="[CPCLI %(levelname)s]: %(message)s",
    level=logging.DEBUG)


def build(config):
    config.Path.src = formattedPath(config.Path.src)
    config.Path.build = formattedPath(config.Path.build)

    src = config.Path.src
    build = config.Path.build

    file_filtering_functions = config.file_filtering_functions
    overall_processing_function = config.overall_processing_function
    processing_function = config.processing_function

    src_size = len(src)

    walk = [(root, dirs, files) for root, dirs, files in os.walk(src)]
    files = [formattedPath(u"%s/%s" % (root, file)) for root, dirs, files in walk for file in files]
    files = [i[src_size:] for i in files]
    for fn in file_filtering_functions:
        files = [file for file in files if fn(file, config)]

    file_k_v = {i: readFile(src + i) for i in files}

    for fn in overall_processing_function:
        file_k_v = fn(file_k_v, config)

    for fn in processing_function:
        file_k_v = dict([fn(k, v, config) for k, v in file_k_v.items()])

    [writeFile(build + k, v) for k, v in file_k_v.items()]
