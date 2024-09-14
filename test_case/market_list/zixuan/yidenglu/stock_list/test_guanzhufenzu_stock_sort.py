#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_guanzhufenzu_stock_sort 
   Description :
   Author : chenqiyue
   CreateDate：2024/07/27  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.assertions import assert_exists
from airtest.core.cv import Template


@pytest.mark.parametrize("final_teardown_yidenglu", [{}], indirect=True)
def test_guanzhufenzu_stock_sort(poco):
    """
用例名称
TC_我的关注分组_竖屏列表排序状态下跳转分时
用例id
1968816
    """

    poco("com.hexin.plat.android:id/slidingmenu_menu").click()
    if not poco(text="自动化").exists():
        poco("com.hexin.plat.android:id/collapse_btn").click()
    poco(text="自动化").click()
    poco(text="最新").click()
    # 获取所有fixed_column元素
    fixed_columns = poco("com.hexin.plat.android:id/fixed_column")
    i = 0
    stock_list = []
    for stock in fixed_columns:
        if i < 3:
            stock_name = stock.attr('desc')
            stock_name = stock_name.split("#")[0]
            stock_list.append(stock_name)
            i = i + 1
        else:
            break
    print(f"列表数据{stock_list}")
    # 获取前三个元素
    # first_three_elements = fixed_columns[:3]
    # print(f"列表前三个股票{first_three_elements}")
    # 获取每个元素的desc值
    # desc_values = [element.attr('desc') for element in first_three_elements]

    # 用#分割
    # joined_desc_values = '#'.join(desc_values)

    # 将结果存到列表中
    # desc_values_list = [joined_desc_values]

    # 打印结果
    # print("Desc values list:", desc_values_list)

    poco("com.hexin.plat.android:id/fixed_column").click()
    elements = [(poco("com.hexin.plat.android:id/navi_left_icon"), "向做切换按钮"),
                (poco("com.hexin.plat.android:id/navi_right_icon"), "向右切换按钮")]
    for ele, element_name in elements:
        if not ele.exists():
            raise AssertionError(f"{element_name}不存在")
        else:
            ele.click()
    navi_title_text = poco("com.hexin.plat.android:id/navi_title_text").get_text()
    assert navi_title_text == stock_list[0]
    poco("com.hexin.plat.android:id/navi_right_icon").click()
    if poco("com.hexin.plat.android:id/i_know").exists():
        poco("com.hexin.plat.android:id/i_know").click()
    navi_title_text = poco("com.hexin.plat.android:id/navi_title_text").get_text()
    assert navi_title_text == stock_list[1], "第一次点击右切换"
    poco("com.hexin.plat.android:id/navi_right_icon").click()
    navi_title_text = poco("com.hexin.plat.android:id/navi_title_text").get_text()
    if poco("com.hexin.plat.android:id/i_know").exists():
        poco("com.hexin.plat.android:id/i_know").click()
    assert navi_title_text == stock_list[2], "第二次点击右切换"
    poco("com.hexin.plat.android:id/backButton").click()
    assert_exists(Template(r"降序按钮.png", record_pos=(-0.072, -0.331), resolution=(1080, 2376)), "降序按钮")
    assert_exists(Template(r"取消排序按钮.png", record_pos=(-0.37, -0.306), resolution=(1080, 2340)), "取消按钮")
    first_stock_name = poco("com.hexin.plat.android:id/fixed_column").attr("desc")
    print(first_stock_name, stock_list[0])
    assert stock_list[0] in first_stock_name
