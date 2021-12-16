# CPCLI

苍之幻灵-脚手架

## 目录

- [快速开始](#快速开始)
- [版权说明](#版权说明)

### 快速开始

1. 打开C:\Users\PC\Documents\maya文件夹
2. 进入scripts文件夹，如果没有就创建它
3. 下载完整的CPCLI代码
4. 解压并进入解压完成的文件夹
5. 将src目录中的CPCLI文件夹复制到scripts
6. 打开maya2018，如果已经打开了就重启它
7. 创建test.python并添加以下代码

```python
#!/usr/bin/python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function

# 因为是将库放在C:\Users\PC\Documents\maya\scripts下的所以需要初始化maya
try:
    import maya.standalone

    maya.standalone.initialize()
except:
    pass

import CPCLI.core as cli_core
from CPCLI.overall_processing_function import group
from CPCLI.file_filtering_functions import noTypes
from CPCLI.processing_function import deleteBlankLines, deleteUselessStrings


class Config(object):
    # 文件过滤函数
    file_filtering_functions = [
        noTypes(['pyc'])
    ]
    # 整体处理函数
    overall_processing_function = [
        group(
            name=u"TOOL_NAME",
            exec_script=u'''\
# 以下是启动脚本
import main
from main import main
main()'''
        )
    ]
    # 处理函数
    processing_function = [
        # 清除空行
        deleteBlankLines,
        # 清除无用字符串
        deleteUselessStrings
    ]
    # 可真可假影响不大
    debug = True

    class Path(object):
        root = r"项目根目录"
        src = root + r"\src"
        scripts = root + r"\scripts"
        build = root + r"\build"


cli_core.build(Config)
```

### 版权说明

该项目签署了Apache-2.0 授权许可，详情请参阅 LICENSE