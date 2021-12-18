# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/19 4:12
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import re

build_file_check = re.compile(r".*\.py$")

import ast
import astunparse


def filter_node(nodes, key):
    """

    :param key:
    :type nodes: ast.AST
    """
    for b in ast.walk(nodes):
        if hasattr(b, "body"):
            b.body = [i for i in b.body if key(i)]


def future_top(f_dict):
    """ 过滤所有文件中的__future__将其置顶"""
    for path, code in f_dict.items():
        if not build_file_check.match(path) is None:
            futures = []
            nodes = ast.parse(code)

            def filter_fn(i):
                """
                :type i: ast.AST
                """
                if isinstance(i, ast.ImportFrom):
                    if i.module == "__future__":
                        for f in i.names:
                            futures.append(f)
                        return False
                return True

            filter_node(nodes, key=filter_fn)
            if len(futures) > 0:
                from_imp_futures = ast.ImportFrom()
                from_imp_futures.module = "__future__"
                from_imp_futures.level = 0
                from_imp_futures.names = futures
                nodes.body.insert(0, from_imp_futures)
            code = astunparse.unparse(nodes)
            f_dict[path] = code
    return f_dict
