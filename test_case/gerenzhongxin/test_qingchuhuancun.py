#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_qingchuhuancun 
   Description :
   Author : chenqiyue
   CreateDate：2024/07/29  用例id:
-------------------------------------------------
"""
import threading

import pytest
from airtest.core.api import snapshot, sleep

from common.function import myFindElements
from common.image import image_to_base64, ths_ocr


@pytest.mark.parametrize("final_teardown_gerenzhongxin", [{}], indirect=True)
def test_qingchuhuancun(poco):
    """
    用例名称
    TC_清除缓存
    用例id
    1100997
    """
    print("test_qingchuhuancun")
    myFindElements("com.hexin.plat.android:id/iv_personal_setting", 2, poco)
    if poco("返回").exists():
        poco("返回").click()
    poco("com.hexin.plat.android:id/iv_personal_setting").click()

    def click_element():
        poco(text="清除缓存").click()

    def take_screenshot():
        snapshot(filename="screenshot.png")

    # 创建线程来并行执行点击和截屏操作
    click_thread = threading.Thread(target=click_element)
    screenshot_thread = threading.Thread(target=take_screenshot)
    # 启动线程
    click_thread.start()
    screenshot_thread.start()
    # 等待线程完成
    click_thread.join()
    screenshot_thread.join()
    print("Click and screenshot completed.")
    Temp_str = ths_ocr(image_to_base64("screenshot.png"))
    toast = Temp_str["text"]
    toast = f"{toast}"
    print(toast)
    if "清除缓存成功" not in toast:
        snapshot(filename="screenshot.png")
        Temp_str = ths_ocr(image_to_base64("screenshot.png"))
        toast = Temp_str["text"]
        toast = f"{toast}"
        print(toast)
        if "当前已是最新版本" not in toast:
            raise AssertionError(f"点击清除缓存提示信息为{toast}")

    else:
        print(f"点击清除缓存提示信息为{toast}")
