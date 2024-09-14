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


@pytest.fixture(scope="module", autouse=True)
def enter_main_inflow_dapan(poco):
    # 重启app
    stop_app_open_app("com.hexin.plat.android")
    sleep(8.0)
    try:
        homePageFindElements(poco(text="行情"), 1, poco).click()
    except Exception as e:
        print(e)
        if poco("行情").exists():
            poco("行情").click()
        elif poco(text="行情").exists():
            poco(text="行情").click()
    finally:
        sleep(3.0)
    poco("com.hexin.plat.android:id/tool_bar").offspring("A股").click()
    poco("com.hexin.plat.android:id/hs")

