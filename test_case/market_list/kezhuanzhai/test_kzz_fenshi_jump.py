#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_kzz_jump_fenshi 
   Description :
   Author : chenqiyue
   CreateDate：2024/01/03  用例id:
-------------------------------------------------
"""
from airtest.core.api import sleep, keyevent

from common.function import check_time_range, check_attr_updated


def test_kzz_jump_fenshi(poco):
    """
    用例id    用例名称
    1752757  TC_转债列表股票跳转
    操作步骤:
    """
    # 点击第一个元素，记录位置和text值
    first_element = poco("com.hexin.plat.android:id/tv_value")[0]
    second_element = poco("com.hexin.plat.android:id/tv_value")[4]
    first_element_text = first_element.get_text()
    second_element_text = second_element.get_text()
    first_element_pos = first_element.get_position()

    first_element.click()
    # 如果弹出 i_know 弹窗，则点击
    if poco("com.hexin.plat.android:id/i_know").exists():
        poco("com.hexin.plat.android:id/i_know").click()
        sleep(2)  # 等待页面加载完成
    # 获取poco("com.hexin.plat.android:id/navi_title_text")的text属性值
    navi_title_text = poco("com.hexin.plat.android:id/navi_title_text").get_text()

    # 校验两个text值是否一致
    if first_element_text != navi_title_text:
        raise AssertionError(f"行情-可转债-点击第一个可转债股票跳转后的报价头股票名称不一致,跳转前{first_element_text},跳转后{navi_title_text}")
    else:
        print(f"行情-可转债-点击第一个可转债股票跳转后的报价头股票名称一致,跳转前{first_element_text},跳转后{navi_title_text}")
    # 校验盘中报价头是否刷新
    if check_time_range():
        check_attr_updated(poco("com.hexin.plat.android:id/fenshi_headline_view"), "desc")
    else:
        print("当前时间不在允许的时间段内，不执行代码。")
    # 点击切换按钮,校验下一个股票是否和股票列表一致
    poco("com.hexin.plat.android:id/navi_right_icon").click()
    navi_title_text2 = poco("com.hexin.plat.android:id/navi_title_text").get_text()
    # 校验两个text值是否一致
    if second_element_text != navi_title_text2:
        raise AssertionError(f"行情-可转债-点击第2个可转债股票跳转后的报价头股票名称不一致,跳转前{second_element_text},跳转后{navi_title_text2}")
    else:
        print(f"行情-可转债-点击第2个可转债股票跳转后的报价头股票名称一致,跳转前{second_element_text},跳转后{navi_title_text2}")
    # 点击返回按钮
    poco("com.hexin.plat.android:id/backButton").click()

    # 校验位置是否变化
    current_pos = first_element.get_position()
    if current_pos != first_element_pos:
        raise AssertionError("Element position has changed.")
    # 再次点击校验按键返回
    first_element.click()

    # 获取poco("com.hexin.plat.android:id/navi_title_text")的text属性值
    navi_title_text = poco("com.hexin.plat.android:id/navi_title_text").get_text()

    # 校验两个text值是否一致
    if first_element_text != navi_title_text:
        raise AssertionError(f"行情-可转债-点击第一个可转债股票跳转后的报价头股票名称不一致,跳转前{first_element_text},跳转后{navi_title_text}")
    else:
        print(f"行情-可转债-点击第一个可转债股票跳转后的报价头股票名称一致,跳转前{first_element_text},跳转后{navi_title_text}")
    # 点击返回按钮
    keyevent("BACK")
    # 校验位置是否变化
    current_pos = first_element.get_position()
    if current_pos != first_element_pos:
        raise AssertionError("Element position has changed.")
    # 再次点击校验按键返回





