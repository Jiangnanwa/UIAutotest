#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_kzz_jiagezhoushi
   Description：  TC_切换价格走势图表
   Author：       duanxufei
   CreateDate：   2024/3/15 10:26
   CaseID：       2025544
-------------------------------------------------
"""
from common.image import get_screenshot_by_element, ths_ocr, image_to_base64, get_device_full_screenshot


def test_setup(poco):
    """
    前提
        行情-可转债，点击可转债均价卡片
    """
    poco("行情").click()
    poco("com.hexin.plat.android:id/tool_bar").offspring("可转债").click()
    poco(text="可转债均价").click()
    poco(text="价格走势").click()


def test_qiehuanyinian(poco):
    """
    切换近一年图表
        1：点击近一年按钮
    """
    # 获取“近一年”所在的坐标并点击
    r = ths_ocr(image_to_base64(get_device_full_screenshot()))
    p = get_text_pos(r, "近一年")
    poco.click(p)

    # 先获取到图表所在的元素
    chart = poco("android.widget.ScrollView").offspring("android.widget.RelativeLayout")[0].child("android.view.View")

    tmp_path = get_screenshot_by_element(chart)

    r = ths_ocr(image_to_base64(tmp_path))
    target_text = r["text"].split("\n")[-1]
    from datetime import datetime, timedelta
    # 获取当前日期
    current_date = datetime.now()
    yesterday_date = current_date - timedelta(days=1)
    # 获取一年前的日期
    one_year_ago = yesterday_date - timedelta(days=365)
    # 格式化日期为字符串
    current_date_str = current_date.strftime("%Y-%m-%d")
    yesterday_date_str = yesterday_date.strftime("%Y-%m-%d")
    one_year_ago_str = one_year_ago.strftime("%Y-%m-%d")
    # 拼接日期字符串
    # TODO 近一年的图表日期更新逻辑待确认
    source_text = f"{one_year_ago_str} {current_date_str}"
    # assert source_text == target_text
    print(f"图表x轴日期实际为:{target_text}")
    print(f"图表x轴左侧日期预期为:{one_year_ago_str}")
    print(f"图表x轴右侧日期预期为:{current_date_str}")


def test_qiehuanfenshi(poco):
    """
    切换分时图表
        1：点击分时按钮
    """
    # 获取“近一年”所在的坐标并点击
    r = ths_ocr(image_to_base64(get_device_full_screenshot()))
    p = get_text_pos(r, "分时")
    poco.click(p)

    # 先获取到图表所在的元素
    chart = poco("android.widget.ScrollView").offspring("android.widget.RelativeLayout")[0].child("android.view.View")

    tmp_path = get_screenshot_by_element(chart)

    r = ths_ocr(image_to_base64(tmp_path))
    target_text = r["text"].split("\n")[-1]

    assert "09:30 11:30/13:00 15:00" == target_text


def get_text_pos(full_input, target_str):
    data = full_input["data"]
    target_str_bound = []
    for index in range(len(data)):
        if target_str == data[index][0]:
            target_str_bound = data[index][1]
    x = (target_str_bound[0][0] + target_str_bound[1][0]) / 2
    y = (target_str_bound[0][1] + target_str_bound[3][1]) / 2
    x_delta = x / full_input['weight']
    y_delta = y / full_input['height']
    return [x_delta, y_delta]
