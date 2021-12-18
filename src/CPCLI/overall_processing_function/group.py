#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/2/23 6:41
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""

import logging
import ast
import astunparse
from CPCLI.utils import uidname, formattedPath
import re

py_check = re.compile(r".*\.py[cdowz]?$")
build_file_check = re.compile(r".*\.py$")
py_path_get = re.compile(r"(.*)\.py[cdowz]?$")


def build(code, import_fn, from_import_fn):
    u"""


    :param code: str
    :param modules: list
    :param import_fn: func
    :param from_import_fn: func
    :return: str
    """
    nodes = ast.parse(code)
    for i in ast.walk(nodes):
        if isinstance(i, ast.Import):
            import_fn(i)
        elif isinstance(i, ast.ImportFrom):
            from_import_fn(i)
    code = astunparse.unparse(nodes)
    return code


def filePathToModuleName(file_path):
    path = py_path_get.findall(file_path)
    path = path[0]
    return u".".join([i for i in path.split(u"/") if i != u""])


head_template = u"""\
from sys import modules as __CPCLI_GROUP_SYS_MODULES
__import__("<<group>>").<<name>> = __CPCLI_GROUP_SYS_MODULES.get(__name__)
"""


def _main(group_name, exec_script, f_dict, config):
    u"""
    :type f_dict: dict
    :param f_dict:
    :type config: object
    :param config:
    :return:
    """
    _head_template = head_template.replace(u"<<group>>", group_name)

    files = [i for i in f_dict.keys() if not py_check.match(i) is None]
    module_dict = {filePathToModuleName(i): i for i in files}
    package_dict = {u".".join(k.split(u".")[:-1]): v for k, v in module_dict.items()
                    if k.split(u".")[-1] == u"__init__"}
    package_dict = {k: v for k, v in package_dict.items() if k != u""}

    def importFn(this_name, node):
        u"""

        :param this_name: str
        :param node: ast.Import
        :return:
        """
        this_package = u".".join(this_name.split(u".")[:-1])
        for ID in range(len(node.names)):
            alias = node.names[ID]
            alias_list = list()
            node.names[ID] = alias_list
            name = alias.name
            asname = alias.asname

            re_ed_name = u"%s.%s" % (this_package, name)
            if not (re_ed_name in module_dict or re_ed_name in package_dict):
                if name in module_dict or name in package_dict:
                    con_ed_name = u"%s.%s" % (group_name, name)
                    alias.name = con_ed_name
                    if asname is None:
                        head = ast.alias()
                        head.asname = name.split(u".")[0]
                        head.name = u"%s.%s" % (group_name, head.asname)
                        alias.asname = u"_"
                        alias_list.append(head)
            alias_list.append(alias)
        node.names = [t for i in node.names for t in i]

    def importFromFn(this_name, node):
        u"""

        :param this_name: str
        :param node: ast.ImportFrom
        :return:
        """
        if node.level < 1:
            this_package = u".".join(this_name.split(u".")[:-1])
            name = node.module
            re_ed_name = u"%s.%s" % (this_package, name)
            if not (re_ed_name in module_dict or re_ed_name in package_dict):
                if name in module_dict or name in package_dict:
                    node.module = u"%s.%s" % (group_name, name)

    for name, path in module_dict.items():
        if not build_file_check.match(path) is None:
            print(u"build %s" % path)
            f_dict[path] = build(f_dict[path], lambda i: importFn(name, i), lambda i: importFromFn(name, i))

    for name, path in module_dict.items() + package_dict.items():
        if len(name.split(u".")) == 1:
            print(u"add head %s" % path)
            f_dict[path] = u"{}\nexec({})".format(_head_template.replace(u"<<name>>", name), repr(f_dict[path]))

    if not u"/__init__.py" in f_dict:
        logging.info(u"add __init__.py")
        f_dict[u"/__init__.py"] = "# plug group head"

    path_head_str = u"/" + group_name
    f_dict = {path_head_str + k: v for k, v in f_dict.items()}

    f_dict[u"/exec.py"] = build(exec_script, lambda i: importFn(u"-@", i), lambda i: importFromFn(u"-@", i))
    return f_dict


def group(name, exec_script):
    return lambda f_dict, config: _main(name, exec_script, f_dict, config)
