#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：
   Description :
   Author : zengwenxin
   CreateDate：2024/05/27  用例id:
-------------------------------------------------
"""
import os

from PIL import Image

from airtest.core.api import sleep, swipe, snapshot

from airtest.aircv.cal_confidence import *
import cv2
from common.image import get_screenshot_by_element2
from common.network_operations import disable_wifi, enable_wifi,  lockunlock_screen
from common.function import check_attr_updated


def test_01_refresh(poco):
    """
    用例名称
    TC_大盘控件_展开状态盘中分时数据刷新/k线图数据更新
    用例id
    1238626、1238631
    """

    check_attr_updated(poco("com.hexin.plat.android:id/price"), "text", second=60)
    # print(poco("com.hexin.plat.android:id/price").get_text())



def test_02_wlan(poco):
    # 断网重连

    disable_wifi(poco)
    sleep(10)#等待一段时间，确保 Wi-Fi 已经完全关闭
    enable_wifi(poco)
    sleep(10)
    if not poco("com.hexin.plat.android:id/price").exists():
        poco("com.hexin.plat.android:id/selfstock_arrow").click()
    check_attr_updated(poco("com.hexin.plat.android:id/price"), "text", second=60)

def test_03_lock(poco):

    lockunlock_screen(poco)
    if not poco("com.hexin.plat.android:id/price").exists():
        poco("com.hexin.plat.android:id/selfstock_arrow").click()
    check_attr_updated(poco("com.hexin.plat.android:id/price"), "text", second=60)
def test_04_screen_shot(poco):
    # Example usage
    poco_element = poco("com.hexin.plat.android:id/curveview")
    destination_directory = "image"
    screenshot_path1 = get_screenshot_by_element2(poco_element, "fenshi1", destination_directory)
    sleep(60)
    screenshot_path2 = get_screenshot_by_element2(poco_element, "fenshi2", destination_directory)

    print(f"分时图保存在: {screenshot_path1}")
    im_source = Image.open(screenshot_path1)
    im_search = Image.open(screenshot_path2)
    im_source_cv = cv2.cvtColor(np.array(im_source), cv2.COLOR_RGB2BGR)
    im_search_cv = cv2.cvtColor(np.array(im_search), cv2.COLOR_RGB2BGR)

    confidence = cal_ccoeff_confidence(im_source_cv, im_search_cv)

    print("----------------")
    print(confidence)
    if confidence < 0.99:
        print("分时图刷新")
    else:
        raise AssertionError("相似度高于99%,可能未刷新！")
def test_05_screen_shot(poco):
    if not poco("com.hexin.plat.android:id/price").exists():
        poco("com.hexin.plat.android:id/selfstock_arrow").click()
    poco("com.hexin.plat.android:id/curveview").swipe([-1, 0])

    # Example usage
    poco_element = poco("com.hexin.plat.android:id/curveview")
    destination_directory = "image"
    os.makedirs(destination_directory, exist_ok=True)

    screenshot_path1 = get_screenshot_by_element2(poco_element, "k1", destination_directory)
    sleep(60)
    screenshot_path2 = get_screenshot_by_element2(poco_element, "k2", destination_directory)

    print(f"k线图保存在: {screenshot_path1}")
    im_source = Image.open(screenshot_path1)
    im_search = Image.open(screenshot_path2)
    im_source_cv = cv2.cvtColor(np.array(im_source), cv2.COLOR_RGB2BGR)
    im_search_cv = cv2.cvtColor(np.array(im_search), cv2.COLOR_RGB2BGR)

    confidence = cal_ccoeff_confidence(im_source_cv, im_search_cv)

    print("----------------")
    print(confidence)
    if confidence < 0.99:
        print("k线图刷新")
    else:
        raise AssertionError("相似度高于99%,可能未刷新！")
