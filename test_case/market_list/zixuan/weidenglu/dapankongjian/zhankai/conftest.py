#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：conftest.py
   Description :
   Author : chenqiyue
   CreateDate：2023/04/03
   用例id:
------------------------------------------------
"""
import pytest
from airtest.core.android import Android
from airtest.core.api import *

from common.app_operation import stop_app_open_app, back_findelement
from common.function import myFindElements, homePageFindElements


@pytest.fixture(scope="function", autouse=True)
def test_dapankongjian_setup(poco):
    print("scope=function, autouse=True")
    # start_app("com.hexin.plat.android", activity="LogoEmptyActivity")
    if poco("同花顺自选").exists():
        if poco("com.hexin.plat.android:id/qrfx_name").exists():
            print("大盘是展开的状态")
        else:
            print("大盘不是展开的状态,需要点击展开按钮")
            poco("com.hexin.plat.android:id/selfstock_arrow").click()
    else:
        back_findelement(poco(text="自选"))
        if poco("自选").exists():
            print("当前页面没有同花顺自选,进行返回操作,直到有自选元素")
            poco("自选").click()
        elif poco(text="自选").exists():
            poco(text="自选").click()
        poco("com.hexin.plat.android:id/selfstock_arrow").click()


