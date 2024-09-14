#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：test_gerenzhongxin
   Description :
   Author : wangsutong
   CreateDate：2024/06/19
   用例id:
------------------------------------------------
"""
from airtest.core.api import touch, sleep, keyevent
from airtest.core.cv import Template

import pytest


@pytest.mark.parametrize("final_teardown_gerenzhongxin", [{}], indirect=True)
def test_gerenzhuye(final_teardown_gerenzhongxin,poco):
    """
    用例名称
    TC_个人主页
    用例id
    1100977
    """
    print("TC_个人主页")
    if poco("com.hexin.plat.android:id/iconPersonalRightImage").exists():
        poco("com.hexin.plat.android:id/iconPersonalRightImage").click()
    else:
        touch(Template(r"个人中心跳转按钮.png", record_pos=(0.45, -0.796), resolution=(1080, 2340)))
    sleep(3.0)
    elements = [poco(text="全部"), poco(text="模拟")]
    for i in elements:
        if not i.exists():
            raise AssertionError(f"{i}元素缺失")
    #poco("android.widget.LinearLayout").offspring("android.widget.RelativeLayout").child("android.webkit.WebView").offspring("app").offspring("userInfo").child("android.view.View")[0].child("android.widget.TextView")[0].click()
    keyevent('BACK')
    assert poco("com.hexin.plat.android:id/iv_personal_setting").exists(), "未返回到上一级页面"



