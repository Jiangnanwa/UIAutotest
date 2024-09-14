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


@pytest.fixture(scope="function", autouse=True)
def enter_main_inflow_qihuo(poco):
    # 重启app
    stop_app_open_app("com.hexin.plat.android")
    sleep(8.0)

    homePageFindElements(poco(text="行情"), 1, poco)
    if poco("行情").exists():
        poco("行情").click()
    elif poco(text="行情").exists():
        poco(text="行情").click()


    sleep(3.0)
    # 初始化第一个引导
    if poco("com.hexin.plat.android:id/tv_guide_pop_title").exists():
        poco("com.hexin.plat.android:id/tv_guide_pop_title").click()

    poco("期货").wait(15).click()
    poco("com.hexin.plat.android:id/futures_external").wait(15).click()
