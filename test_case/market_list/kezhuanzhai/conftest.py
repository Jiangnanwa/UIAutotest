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
from airtest.core.api import sleep

from common.app_operation import stop_app_open_app
from common.function import homePageFindElements

import time


@pytest.fixture(scope="module", autouse=True)
def enter_main_inflow_kzz(poco):
    # 重启app
    stop_app_open_app("com.hexin.plat.android")
    sleep(8.0)
    if not poco(text="转债排行").exists():
        print("当前页面不再可转债页面")
        # 新手开户弹窗
        if poco(name="android.widget.Image").exists():
            poco(nameMatches="android.widget.Image")[0].click()
        homePageFindElements(poco(text="行情"), 1, poco)
        if poco("行情").exists():
            poco("行情").click()
        elif poco(text="行情").exists():
            poco(text="行情").click()


        sleep(3.0)
        # 初始化第一个引导
        if poco("com.hexin.plat.android:id/tv_guide_pop_title").exists():
            poco("com.hexin.plat.android:id/tv_guide_pop_title").click()

        poco("可转债").wait(15).click()
    else:
        print("当前页面在可转债页面")
