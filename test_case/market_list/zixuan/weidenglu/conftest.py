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

from airtest.core.api import *

from common.app_operation import back_findelement
from common.function import homePageFindElements



@pytest.fixture(scope="package", autouse=True)
def weidenglu_enter_main_inflow(poco):
    start_app("com.hexin.plat.android", activity="LogoEmptyActivity")
    G.BASEDIR.append(os.path.dirname(os.path.abspath(__file__)))
    zixuan = poco(text="自选", name="com.hexin.plat.android:id/title")
    homePageFindElements(zixuan, 1, poco)

    if not zixuan.exists() or poco("自选").exists():
        back_findelement(zixuan)
    if zixuan.exists():
        zixuan.click()
    elif poco("自选").exists():
        poco("自选").click()
    else:

        print("图像识别点击")

        touch(Template(r"zixuantab.png"))
    tab_list = [poco("不用了"), poco(text="不用了")]
    [i.click() for i in tab_list if i.exists()]