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

from common.app_operation import stop_app_open_app, back_findelement
from common.function import homePageFindElements


@pytest.fixture(scope="function", autouse=True)
def enter_main_inflow_sousuo(poco):
    # 重启app
    stop_app_open_app("com.hexin.plat.android")
    sleep(3.0)
    homePageFindElements(poco(text="行情"), 1, poco)
    # 点击搜索框
    poco("com.hexin.plat.android:id/text_switcher").click()
    sleep(1.0)
