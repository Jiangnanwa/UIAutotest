#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_search_fenshi
   Description :
   Author : chenqiyue
   CreateDate：2023/12/06  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import sleep, touch, exists

from common.function import Template
import requests

# @pytest.mark.repeat(10)
def test_search_fenshi(poco, phone_udid):
# def test_search_fenshi(poco):
# 搜索分时
    sleep(3.0)
    sousuokuang = exists(Template(r"tpl1723465262931.png", record_pos=(-0.042, -0.757), resolution=(1080, 1920)))
    print("如果搜索框图片存在则点击")
    if sousuokuang:
        print("搜索框图片存在点击")
        touch(Template(r"tpl1723465262931.png", record_pos=(-0.042, -0.757), resolution=(1080, 1920)))
        print("搜索框图片存在点击成功")
    elif poco(text="搜索").exists():
        print("搜索框搜索按钮元素存在")
        poco(text="搜索").click()
        print("搜索框搜索按钮元素点击成功")
    print("等待5s")
    # sleep(8.0)
    try:
        print("点击输入框")
        search_input = poco("com.hexin.plat.android:id/search_input")
        search_input.wait_for_appearance()
        search_input.click()
    except Exception as e:
        print(e, "没找到输入框")
        poco(name="com.hexin.plat.android:id/search_input", type="android.widget.EditText").refresh()
        poco(name="com.hexin.plat.android:id/search_input", type="android.widget.EditText").click()
    print("点击输入框成功")
    sleep(2.0)
    print("在输入框输入600519")
    search_input.set_text("600519")
    print("在输入框输入600519成功")
    #sleep(2.0)
    print("在输入框输入600519后点击搜索")
    #poco(name="com.hexin.plat.android:id/search_action").click()
    sleep(5.0)
    print("点击搜索出来的茅台")
    try:
        poco(textMatches="贵州茅台|XD贵州茅").wait_for_appearance()
    except Exception as e:
        print(e, "贵州茅台|XD贵州茅")
    gzmt = poco(textMatches="贵州茅台|XD贵州茅")
    if gzmt.exists():
        print("贵州茅台存在，开启录制")
        requests.get(f"http://localhost:9998/start/scrcpy?serial={phone_udid}")
        gzmt.click()
    else:
        raise AssertionError("没有找到贵州茅台，无法开启录屏")
    if poco(name="com.hexin.plat.android:id/navi_title_text", text="贵州茅台").exists():
        print("进入到茅台分时，调用结束录屏的接口")
        requests.get(f"http://localhost:9998/stop/scrcpyfromscript?serial={phone_udid}")

    else:
        raise AssertionError("没有进入到茅台分时，没有调用调用结束录屏的接口,进行重跑")
