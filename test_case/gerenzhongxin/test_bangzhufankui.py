#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：test_gerenzhongxin
   Description :TC_（已自动化）帮助与反馈
   Author : wangsutong
   CreateDate：2024/06/19
   用例id:1101006
------------------------------------------------
"""

from airtest.core.api import touch, sleep, keyevent
from airtest.core.assertions import assert_exists
from airtest.core.cv import Template
import pytest


@pytest.mark.parametrize("final_teardown_gerenzhongxin", [{}], indirect=True)
def test_bangzhufankui(final_teardown_gerenzhongxin, poco):
    poco("com.hexin.plat.android:id/iv_personal_setting").click()
    poco("com.hexin.plat.android:id/scroll").swipe([-0.0313, -0.763])
    poco(text="帮助和反馈").click()

    assert_exists(Template(r"tpl1721634426140.png", record_pos=(-0.025, -0.958), resolution=(1080, 2340)), "问财导航栏是否存在")
    keyevent('BACK')
    assert poco(text="系统设置").exists(), "未返回到上一级页面"


