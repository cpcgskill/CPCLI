#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/2/25 6:04
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import ast
import astunparse
import re

re_check = re.compile(r".*\.py$")

block_node_types = [ast.Module, ast.If, ast.FunctionDef, ast.ClassDef, ast.For]


def checkNode(node):
    if isinstance(node, ast.Expr):
        if isinstance(node.value, ast.Str):
            return False
    return True


def buildBlock(node):
    node.body = [i for i in node.body if checkNode(i)]
    for i in node.body:
        for t in block_node_types:
            if isinstance(i, t):
                buildBlock(i)
    if len(node.body) < 1:
        node.body.append(ast.Pass())


def deleteUselessStrings(file, code, config):
    if not re_check.match(file) is None:
        nodes = ast.parse(code)
        buildBlock(nodes)
        code = astunparse.unparse(nodes)
    return file, code
