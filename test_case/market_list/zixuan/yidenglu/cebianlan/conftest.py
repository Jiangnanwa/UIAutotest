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

from airtest.core.api import *

from common.app_operation import stop_app_open_app, back_findelement
from common.function import homePageFindElements

import pytest

from common.login import login_by_password, login_out


@pytest.fixture(scope="function", autouse=True)
def cebianlan_zhankai(poco):

    if poco(text="我知道了").exists():
        poco(text="我知道了").click()
    poco("com.hexin.plat.android:id/slidingmenu_menu").click()
    if poco(text="我知道了").exists():
        poco(text="我知道了").click()