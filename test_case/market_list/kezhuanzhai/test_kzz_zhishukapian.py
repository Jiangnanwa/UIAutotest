#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_kzz_zhishukapian
   Description：  TC_指数卡片_数据格式展示
   Author：       duanxufei
   CreateDate：   2024/3/14 16:41
   CaseID：       2025513
-------------------------------------------------
"""
from common.image import get_color, get_screenshot_by_element

import re


def count_decimal_places(num_str):
    pattern = r'^[+-]?\d+(\.\d+)?$'
    if re.match(pattern, num_str):
        decimal_places = len(num_str.split('.')[1])
        return decimal_places
    else:
        return 0


def test_setup(poco):
    """
    前提
        行情-可转债，点击指数卡片
    """
    poco("行情").click()
    poco("com.hexin.plat.android:id/tool_bar").offspring("可转债").click()
    poco(text="可转债指数").click()


def test_check_data(poco):
    """
    数据格式展示
        1：校验指数、涨跌幅、涨跌值数据格式展示
    """
    kapian_ele = poco(text="可转债指数").parent()
    textview_list = kapian_ele.offspring("android.widget.TextView")
    zhishu_text = textview_list[1].get_text()
    zhangdie = textview_list[2].get_text()
    zhangdiefu = textview_list[3].get_text()
    assert 3 == count_decimal_places(zhishu_text)
    assert 3 == count_decimal_places(zhangdie)
    assert 2 == count_decimal_places(zhangdiefu[0:-1])


def test_check_color_1(poco):
    """
    颜色展示
        1：校验指数数据颜色展示
    """
    kapian_ele = poco(text="可转债指数").parent()
    textview_list = kapian_ele.offspring("android.widget.TextView")
    color = get_color(get_screenshot_by_element(textview_list[1]), shield_list=["white"])
    assert "green" == color or "red" == color or "red2" == color


def test_check_color_2(poco):
    """
    颜色展示
        1：校验涨跌幅数据颜色展示
    """
    kapian_ele = poco(text="可转债指数").parent()
    textview_list = kapian_ele.offspring("android.widget.TextView")
    color = get_color(get_screenshot_by_element(textview_list[2]), shield_list=["white"])
    assert "green" == color or "red" == color or "red2" == color


def test_check_color_3(poco):
    """
    颜色展示
        1：校验涨跌值数据颜色展示
    """
    kapian_ele = poco(text="可转债指数").parent()
    textview_list = kapian_ele.offspring("android.widget.TextView")
    color = get_color(get_screenshot_by_element(textview_list[3]), shield_list=["white"])
    assert "green" == color or "red" == color or "red2" == color
