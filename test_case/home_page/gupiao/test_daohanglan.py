#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_daohanglan 
   Description :
   Author : chenqiyue
   CreateDate：2024/08/07  用例id:
-------------------------------------------------
"""
from airtest.core.api import exists, sleep
from airtest.core.cv import Template


def test_daohanglan(poco):
    """
用例名称
TC_导航栏
用例id
587366
    """
    # 校验标题栏存在
    exists(Template(r"tpl1723015100178.png", record_pos=(0.011, -0.931), resolution=(1080, 2376)))
    # 标题
    title_bar_middle = poco("com.hexin.plat.android:id/title_bar_middle")
    # 标题名称
    assert title_bar_middle.get_text() == "股票"
    # 语音助手点击
    poco("com.hexin.plat.android:id/voice_assistant").click()
    sleep(3.0)
    # 跳转后可能存在的提示
    if poco("com.hexin.plat.android:id/close_img").exists():
        poco("com.hexin.plat.android:id/close_img").click()
    if poco("com.hexin.plat.android:id/ok_btn").exists():
        poco("com.hexin.plat.android:id/ok_btn").click()
    # 点击标题栏的搜索
    poco("com.hexin.plat.android:id/new_title_search").click()
    # 校验搜索框存在
    assert poco("com.hexin.plat.android:id/search_input").exists()
    #返回到股票
    poco("com.hexin.plat.android:id/back_up").click()
    # 返回首页按钮
    poco("com.hexin.plat.android:id/title_bar_img").click()
    assert poco(text="行情").exists()
