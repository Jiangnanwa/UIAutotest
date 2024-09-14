#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_tuxiangshibie
   Description :
   Author : chenqiyue
   CreateDate：2024/03/14  用例id:
-------------------------------------------------
"""

from airtest.core.api import touch
from airtest.core.cv import Template
from airtest.core.helper import G
import os


def test_tuxiangshibie(poco):
    """
    用例id    用例名称
    1300912  TC_全部板块_排序状态列表滑动
    操作步骤:
    """
    print("图像识别")
    # sleep(5.0)
    # if poco("com.hexin.plat.android:id/tv_skip").exists():
    #     poco("com.hexin.plat.android:id/tv_skip").click()
    print(G.BASEDIR)

    touch(Template(r"tpl1710408236141.png", record_pos=(0.376, -0.081), resolution=(1224, 2700)))
