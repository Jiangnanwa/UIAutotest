#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_hot_stock_navigation 
   Description :
   Author : chenqiyue
   CreateDate：2024/07/17  用例id:
-------------------------------------------------
"""
from airtest.core.api import keyevent, sleep

from common.app_operation import back_findelement


def test_hot_stock_navigation(poco):
    """
用例名称
TC_推荐页_热股榜_页面跳转
用例id
1482969
    """
    # 1. 依次选中热股榜单中条目，获取text值，查看页面跳转情况
    stock_items = poco("com.hexin.plat.android:id/stock_name")

    stock_name = stock_items.get_text()
    stock_items.click()
    print(f"跳转前股票{stock_name}")
    stock_name2 = poco("com.hexin.plat.android:id/navi_title_text").get_text()
    print(f"跳转后股票{stock_name2}")

    # 校验页面跳转成功，股票名称一致
    assert stock_name2 == stock_name, "股票详情页名称与点击的股票名称不一致"

    # 返回上一级
    back_findelement(poco(text="综合"))
    assert poco(text="综合").exists(), "未返回到热点榜推荐页"

    # 2. 收起系统键盘
    keyevent("BACK")
    if  poco("com.hexin.plat.android:id/text_switcher").exists():
        poco("com.hexin.plat.android:id/text_switcher").click()
    sleep(1.0)
    # 横滑热股榜，点击【查看更多】
    poco(text="热股榜").swipe([-0.8995, 0.0012])
    poco(text="查看更多").click()

    # 校验跳转至详情页成功，页面布局合理，展示完整
    assert poco(text="同花顺用户都关注的股票").exists(), "详情页布局不合理或未展示完整"

    # 返回上一级，返回推荐页
    back_findelement(poco(text="综合"))
    sleep(1.0)
    assert poco(text="综合").exists(), "未返回到热点榜推荐页"