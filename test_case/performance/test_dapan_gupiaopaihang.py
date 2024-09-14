#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapan_gupiaopaihang
   Description :
   Author : chenqiyue
   CreateDate：2023/12/06  用例id:
-------------------------------------------------
"""
import pytest
import requests
from airtest.core.api import sleep, start_app, touch, swipe
from airtest.core.cv import Template

from common.app_operation import back_findelement
from common.function import homePageFindElements, find_element_within_timeout

# @pytest.mark.repeat(10)
def test_dapan_gupiaopaihang(poco, phone_udid):
# def test_dapan_gupiaopaihang(poco):
    """
    大盘 - 股票排行 - 点击右侧【更多】- 点击【最新】表头 - 点击【贵州茅台】股票（计算从点击至分时页加载完成的耗时）
    """
    start_app("com.hexin.plat.android", activity="LogoEmptyActivity")

    hangqing = poco(text="行情", name="com.hexin.plat.android:id/title")
    # 手机app重启后有一个加载时间，用这个函数去等待
    try:
        hangqing.wait_for_appearance()
    except Exception as e:
        print(e)
    print("处理关闭按钮")
    if poco("com.hexin.plat.android:id/close_button").exists():
        poco("com.hexin.plat.android:id/close_button").click()
    homePageFindElements(hangqing, 1, poco)
    if not hangqing.exists() or poco("行情").exists():
        back_findelement(hangqing)
    if hangqing.exists():
        hangqing.click()
    elif poco("行情").exists():
        poco("行情").click()
    else:
        print("图像识别点击")
        touch(Template(r"tpl1719400341808.png", record_pos=(-0.24, 1.01), resolution=(1440, 3200)))
    sleep(5.0)
    # 初始化第一个引导
    if poco("com.hexin.plat.android:id/tv_guide_pop_title").exists():
        poco("com.hexin.plat.android:id/tv_guide_pop_title").click()
    # 在超时时间内寻找“更多”元素
    # sleep(5.0)
    # poco(text="昨日涨停表现").swipe([0.0397, -0.3864])
    print("滑动页面查找更多")
    try:
        # # find_element_within_timeout(poco(text="展开分析"), timeout=2000)
        # dp_flipper = poco("com.hexin.plat.android:id/dp_flipper")
        # dp_flipper.wait_for_appearance()
        # dp_flipper.swipe([-0.0872, -0.4549])
        swipe(556, 1399, 556, 585, duration=1.0)
    except Exception as e:
        print("dp_flipper没有找到，换其他元素滑动")
        try:
            poco("com.hexin.plat.android:id/amount_change_describe_text").swipe([-0.0121, -0.444])
        except Exception as e:
            print("大盘点评没有找到，拖拽同花顺热榜滑动")
            poco(text="同花顺热榜").swipe([0.0024, -0.5189])
    print("滑动后点击更多")
    if poco(text="更多").exists():
        poco(text="更多").click()
    else:
        touch(Template(r"tpl1724326917531.png", record_pos=(0.4, 0.137), resolution=(1080, 1920)))
    print("点击“最新”按钮")
    zuixin = poco(text="最新")
    try:
        zuixin.wait_for_appearance()
    except Exception as e:
        print(e)
    zuixin.click()
    sleep(5)
    # 等待并点击列表中的第一个元素
    maotai1 = poco(text="贵州茅台")
    maotai2 = poco(nameMatches="贵州茅台.*")
    if maotai1.exists():
        requests.get(f"http://localhost:9998/start/scrcpy?serial={phone_udid}")
        print("贵州茅台点击")
        maotai1.click()
    elif maotai2.exists():
        requests.get(f"http://localhost:9998/start/scrcpy?serial={phone_udid}")
        print("贵州茅台.*被点击")
        maotai2.click()
    else:
        raise AssertionError("没有找到贵州茅台，无法开启录屏")
    if poco(name="com.hexin.plat.android:id/navi_title_text", text="贵州茅台").exists():
        print("进入到茅台分时，调用结束录屏的接口")
        requests.get(f"http://localhost:9998/stop/scrcpyfromscript?serial={phone_udid}")
    else:
        raise AssertionError("没有进入到茅台分时，没有调用调用结束录屏的接口,进行重跑")
