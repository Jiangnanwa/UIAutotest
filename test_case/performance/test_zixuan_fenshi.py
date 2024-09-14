#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_performance
   Description :
   Author : chenqiyue
   CreateDate：2023/11/27  用例id:
-------------------------------------------------
"""

import pytest
from airtest.core.api import start_app, touch
from common.app_operation import back_findelement
from common.function import Template
from common.function import homePageFindElements
import requests
from airtest.core.api import keyevent, sleep
from common.app_operation import stop_app_open_app


# @pytest.mark.repeat(10)
def test_zixuan_fenshi(poco, phone_udid):
# def test_zixuan_fenshi(poco):
    start_app("com.hexin.plat.android", activity="LogoEmptyActivity")
    print("查找自选tab")
    # app启动有等待时间保证可以在首页
    try:
        poco(text="自选", name="com.hexin.plat.android:id/title").wait_for_appearance()
    except Exception as e:
        print(e, "没找到自选")
    # 处理首页弹窗
    homePageFindElements(poco(text="自选", name="com.hexin.plat.android:id/title"), 1, poco)
    # 保证自选是存在的状态
    sleep(5.0)
    try:
        poco(text="自选", name="com.hexin.plat.android:id/title").wait_for_appearance()
    except Exception as e:
        print(e, "没找到自选")
    # 自选元素有很多中定位
    if poco(text="自选", name="com.hexin.plat.android:id/title").exists():
        poco(text="自选", name="com.hexin.plat.android:id/title").click()
        print("text=自选点击成功")
    elif poco("自选").exists():
        poco("自选").click()
        print("name=自选点击成功")
    else:
        print("图像识别点击")
        touch(Template(r"tpl1726106257583.png", record_pos=(-0.08, 0.712), resolution=(1080, 1920)))
    # 进入到自选的弹窗处理
    if poco(text="我知道了").exists():
        poco(text="我知道了").click()
    if poco("com.hexin.plat.android:id/closeBt").exists():
        poco("com.hexin.plat.android:id/closeBt").click()
    if poco("com.hexin.plat.android:id/next_step").exists():
        poco("com.hexin.plat.android:id/next_step").click()
    if poco("com.hexin.plat.android:id/next_step").exists():
        poco("com.hexin.plat.android:id/next_step").click()
    # 自选-分时,游客账号-自选 - 点击【贵州茅台】股票
    # zixuan = poco(text="自选", name="com.hexin.plat.android:id/title")
    sleep(2.0)
    # 先用元素定位点击  没有找到用图像识别
    try:
        poco("com.hexin.plat.android:id/new_title_search").click()
    except Exception as e:
        touch(Template(r"tpl1726105504388.png", record_pos=(0.42, -0.755), resolution=(1080, 1920)))

    try:
        print("点击输入框")
        search_input = poco("com.hexin.plat.android:id/search_input")
        search_input.wait_for_appearance()
        search_input.click()
    except Exception as e:
        print(e, "没找到输入框")
        poco(name="com.hexin.plat.android:id/search_input", type="android.widget.EditText").refresh()
        poco(name="com.hexin.plat.android:id/search_input", type="android.widget.EditText").click()
    sleep(2.0)
    poco("com.hexin.plat.android:id/search_input").set_text("600519")
    sleep(8.0)
    poco("com.hexin.plat.android:id/add_delete_op")[0].click()
    # 回到自选
    if not poco(text="自选", name="com.hexin.plat.android:id/title").exists() or poco("自选").exists():
        back_findelement(poco(text="自选", name="com.hexin.plat.android:id/title"))
    try:
        poco(text="自选", name="com.hexin.plat.android:id/title").wait_for_appearance()
    except Exception as e:
        print(e)
    # 点击自选
    if poco(text="自选", name="com.hexin.plat.android:id/title").exists():
        poco(text="自选", name="com.hexin.plat.android:id/title").click()
    elif poco("自选").exists():
        poco("自选").click()
    else:
        print("图像识别点击")
        touch(Template(r"zixuantab.png"))
    try:
        poco("同花顺自选").wait_for_appearance()
    except Exception as e:
        print(e, "没找到同花顺自选标题")
    sleep(5.0)
    # 茅台股票元素可能存在两种，要求找到元素才进行开始录制
    maotai_button = poco(nameMatches="贵州茅台.*|XD贵州茅.*")
    maotai_button2 = poco(desc="贵州茅台#600519")
    if maotai_button.exists():
        print("贵州茅台.*|XD贵州茅.*存在，开启录制")
        requests.get(f"http://localhost:9998/start/scrcpy?serial={phone_udid}")
        maotai_button.click()
    elif maotai_button2.exists():
        print("贵州茅台#600519存在，开启录制")
        requests.get(f"http://localhost:9998/start/scrcpy?serial={phone_udid}")
        maotai_button2.click()
    else:
        raise AssertionError("没有找到贵州茅台，无法开启录屏")
    # 进入分时页面当贵州茅台股票导航栏出现股票名称进行停止录制
    if poco(name="com.hexin.plat.android:id/navi_title_text", text="贵州茅台").exists():
        print("进入到茅台分时，调用结束录屏的接口")
        requests.get(f"http://localhost:9998/stop/scrcpyfromscript?serial={phone_udid}")
    else:
        raise AssertionError("没有进入到茅台分时，没有调用调用结束录屏的接口,进行重跑")
