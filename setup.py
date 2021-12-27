#!/usr/bin/python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function
import setuptools

with open("README.md", "rb") as f:
    long_description = f.read().decode(encoding="utf-8")

setuptools.setup(
    name="CP_CLI",
    version="1.0.3",
    author="cpcgskill",
    author_email="cpcgskill@outlook.com",
    description="python 打包编译工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cpcgskill/CPCLI",
    project_urls={
        "Bug Tracker": "https://github.com/cpcgskill/CPCLI/issues",
    },
    license="Apache Software License (Apache 2.0)",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    package_dir={"": "src"},
    # 不使用自动搜索
    # packages=setuptools.find_packages(where="src"),
    packages=["CPCLI", "CPCLI.decorator", "CPCLI.overall_processing_function", "CPCLI.processing_function"],
    python_requires="==2.*,",
    # 指定依赖
    install_requires=[
        'astunparse==1.6.3',
    ]
)
