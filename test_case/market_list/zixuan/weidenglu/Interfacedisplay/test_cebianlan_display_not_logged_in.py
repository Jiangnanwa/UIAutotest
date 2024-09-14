#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_cebianlan_display_not_logged_in 
   Description :
   Author : chenqiyue
   CreateDate：2024/05/10  用例id:
-------------------------------------------------
"""
import os

import pytest
from airtest.core.api import touch, exists
from airtest.core.cv import Template
from airtest.core.helper import G
import os

from poco.exceptions import PocoNoSuchNodeException

from common.image import get_screenshot_by_element2


def test_cebianlan_display_not_logged_in(poco):
    """
    用例id    用例名称
    731366  TC_自选侧边栏_未登录的界面显示
    操作步骤:
    荣耀v40
    """
    #current_file = os.path.dirname(__file__)
    #print(current_file)
    try:
        #get_screenshot_by_element2(poco("com.hexin.plat.android:id/slidingmenu_menu"), "cebianlan",current_file)

        poco("com.hexin.plat.android:id/slidingmenu_menu").click()
        if poco(text="我知道了").exists():
            poco(text="我知道了").click()
    except PocoNoSuchNodeException:
        G.BASEDIR.append(os.path.dirname(os.path.abspath(__file__)))

        touch(Template(r"cebianlanmenu.png"))  # 截图定位

    

    #校验选股、持仓股、基金（iOS ）
    #我的关注分组（0）快叫朋友分享吧
    #我的分组（0）
    #自选分组
    #动态分组
    #文案显示“还不会用？查看自选分组使用技巧
