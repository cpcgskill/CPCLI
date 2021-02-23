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
    format="%(asctime)s [CPCLI] %(levelname)s: %(message)s",
    level=logging.DEBUG)


class Files(object):
    def __init__(self):
        self._file_filtering_functions = list()
        self._file_load_function = list()
        self._file_ass = dict()

    def addFileFilteringFunction(self, fn):
        u"""
        添加文件过滤器函数

        :param fn:
        :return:
        """
        self._file_filtering_functions.append(fn)

    def addFileLoadFunction(self, fn):
        u"""
        添加文件加载函数

        :param fn:
        :return:
        """
        self._file_load_function.append(fn)

    def _print(self):
        print (u"{")
        for k, v in self._file_ass.items():
            print(u"    {}: {}".format(repr(k), repr(v)))
        print (u"}")

    def load(self, dir):
        u"""

        :type dir: unicode
        :return:
        """
        dir = formattedPath(dir)
        dir_size = len(dir)

        walk = [(root, dirs, files) for root, dirs, files in os.walk(dir)]
        files = [formattedPath(u"%s/%s" % (root, file)) for root, dirs, files in walk for file in files]
        files = [i[dir_size:] for i in files]
        for fn in self._file_filtering_functions:
            files = [file for file in files if fn(file)]
        file_ass = dict()
        for i in files:
            file = dir + i
            v = None
            for fn in self._file_load_function:
                if v is None:
                    v = fn(file)
                    continue
                break
            if v is None:
                v = readFile(file)
            file_ass[i] = v
        self._file_ass = file_ass

    def dump(self, dir):
        u"""

        :type dir: unicode
        :return:
        """
        dir = formattedPath(dir)
        dir_size = len(dir)
        [writeFile(dir + k, v) for k, v in self._file_ass.items()]


class BuilderObject(object):
    def __init__(self):
        self._file_filtering_functions = list()
        self._overall_processing_function = list()
        self._processing_function = list()
        self._config = dict()

    def setConfig(self, k, v):
        self._config[str(k)] = v

    def addFileFilteringFunction(self, fn):
        u"""
        添加文件过滤器函数

        :param fn:
        :return:
        """
        self._file_filtering_functions.append(fn)

    def addOverallProcessingFunction(self, fn):
        u"""
        添加整体预处理器函数

        :param fn:
        :return:
        """
        self._overall_processing_function.append(fn)

    def addProcessingFunction(self, fn):
        u"""
        添加预处理器函数

        :param fn:
        :return:
        """
        self._processing_function.append(fn)

    def build(self, path, out_dir):
        u"""

        :param path:
        :return:
        """
        path = formattedPath(path)
        path_size = len(path)
        out_dir = formattedPath(out_dir)

        walk = [(root, dirs, files) for root, dirs, files in os.walk(path)]
        files = [formattedPath(u"%s/%s" % (root, file)) for root, dirs, files in walk for file in files]
        files = [i[path_size:] for i in files]
        for fn in self._file_filtering_functions:
            files = [file for file in files if fn(file, self._config)]

        file_k_v = {i: readFile(path + i) for i in files}

        for fn in self._overall_processing_function:
            file_k_v = fn(file_k_v, self._config)

        for fn in self._processing_function:
            file_k_v = {k: fn(v, self._config) for k, v in file_k_v.items()}

        [writeFile(out_dir + k, v) for k, v in file_k_v.items()]


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
        file_k_v = {k: fn(v, config) for k, v in file_k_v.items()}

    [writeFile(build + k, v) for k, v in file_k_v.items()]
