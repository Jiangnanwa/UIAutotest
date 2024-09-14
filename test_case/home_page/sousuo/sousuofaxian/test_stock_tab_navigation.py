#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_stock_tab_navigation 
   Description :
   Author : chenqiyue
   CreateDate：2024/07/17  用例id:
-------------------------------------------------
"""
from airtest.core.api import keyevent, sleep


def test_stock_tab_navigation(poco):
    """
用例名称
TC_搜索_股票Tab_热门股票点击跳转
用例id
1368834
    """
    # 1. 选择股票Tab
    poco(text="股票").click()
    sleep(1.0)
    # 依次点击热门搜索下的股票，校验跳转至分时界面
    hot_search_items = poco("com.hexin.plat.android:id/title")[0]

    stock_name = hot_search_items.get_text()
    hot_search_items.click()
    # 校验跳转至对应股票的分时界面
    assert poco("com.hexin.plat.android:id/navi_title_text").get_text() == stock_name, f"未跳转至股票 {stock_name} 的分时界面"

    # 点击分时界面左上角的返回
    poco("com.hexin.plat.android:id/backButton").click()

    # 校验页面保持在股票Tab
    assert poco(text="股票").attr('selected') == True, "返回后股票Tab未被选中"

    # 2. 再次选择股票Tab
    poco(text="股票").click()
    hot_search_items = poco("com.hexin.plat.android:id/title")[1]
    # 点击一个热门搜索下的股票
    stock_name = hot_search_items.get_text()
    hot_search_items.click()

    # 校验跳转至对应股票的分时界面
    assert poco("com.hexin.plat.android:id/navi_title_text").get_text() == stock_name, f"未跳转至股票 {stock_name} 的分时界面"

    # 按键返回
    keyevent("BACK")

    # 校验页面保持在股票Tab
    assert poco(text="股票").attr('selected') == True, "返回后股票Tab未被选中"
