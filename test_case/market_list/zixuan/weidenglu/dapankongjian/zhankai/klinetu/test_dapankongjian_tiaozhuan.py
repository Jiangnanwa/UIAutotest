#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapankongjian_tiaozhuan 
   Description :
   Author : chenqiyue
   CreateDate：2024/02/28  用例id:
-------------------------------------------------
"""
from airtest.core.api import swipe, keyevent

from common.function import calculate_coordinate


def test_dapankongjian_tiaozhaun_kxian(poco):
    """
    用例名称
    TC_大盘控件_展开状态点击K线跳转
    用例id
    1238633
    操作步骤:
    """
    # 获取股票名称元素
    # stockname_txt = poco(nameMatches="com.hexin.plat.android:id/stockname_txt")
    # # 获取文本值
    # stock_name = stockname_txt.get_text()
    #
    # # 根据文本值设置 zhishu_name 的值
    # if "深" in stock_name:
    #     zhishu_name = "深证成指"
    # elif "沪" in stock_name:
    #     zhishu_name = "上证指数"
    # elif "创" in stock_name:
    #     zhishu_name = "创业板指"
    # elif "京" in stock_name:
    #     zhishu_name = "北证50"
    # else:
    #     # 如果股票名称既不包含“深”也不包含“沪”，也不包含“创”，可以根据实际情况进行处理
    #     zhishu_name = "未知"
    poco(text="沪").click()

    #print("指数名称:", zhishu_name)
    poco("com.hexin.plat.android:id/curveview").swipe([-1, -0.0249])
    poco("com.hexin.plat.android:id/curveview").click()
    if not poco("com.hexin.plat.android:id/navi_title_text").exists():
        keyevent('BACK')
    if not poco("com.hexin.plat.android:id/navi_title_text").get_text()=="上证指数":
        raise  AssertionError("自选-点击大盘控件k线图-跳转的页面非上证指数")
    poco("com.hexin.plat.android:id/backButton").click()
    if not poco(text="上证指数").exists():
        raise  AssertionError("自选-点击大盘控件k线图-按钮返回,没有返回到自选页面,没有找到沪")
    poco("com.hexin.plat.android:id/selfstock_arrow").click()
    poco("com.hexin.plat.android:id/curveview").swipe([-1, -0.0249])
    poco("com.hexin.plat.android:id/curveview").click()
    keyevent('BACK')
    if not poco("同花顺自选").exists():
        raise  AssertionError("自选-点击大盘控件k线图-侧滑返回,没有返回到自选页面")

def test_dapankongjian_tiaozhaun_fenshi(poco):
    """
    用例名称

    TC_大盘控件_展开状态点击分时跳转
    用例id
    1238635
    操作步骤:
    """
    # # 获取股票名称元素
    # stockname_txt = poco("com.hexin.plat.android:id/stockname_txt")
    # # 获取文本值
    # stock_name = stockname_txt.get_text()
    #
    # # 根据文本值设置 zhishu_name 的值
    # if "深" in stock_name:
    #     zhishu_name = "深证成指"
    # elif "沪" in stock_name:
    #     zhishu_name = "上证指数"
    # elif "创" in stock_name:
    #     zhishu_name = "创业板指"
    # elif "京" in stock_name:
    #     zhishu_name = "北证50"
    # else:
    #     # 如果股票名称既不包含“深”也不包含“沪”，也不包含“创”，可以根据实际情况进行处理
    #     zhishu_name = "未知"
    #
    # print("指数名称:", zhishu_name)
    poco(text="沪").click()
    poco("com.hexin.plat.android:id/curveview").click()

    if not poco("com.hexin.plat.android:id/navi_title_text").get_text()=="上证指数":
        raise  AssertionError(f"自选-点击大盘控件k线图-跳转的页面非上证指数")
    poco("com.hexin.plat.android:id/backButton").click()
    if not poco("同花顺自选").exists():
        raise  AssertionError("自选-点击大盘控件k线图-按钮返回,没有返回到自选页面,没有找到同花顺自选")
    poco("com.hexin.plat.android:id/selfstock_arrow").click()

    poco("com.hexin.plat.android:id/curveview").click()
    keyevent('BACK')
    # x,y = calculate_coordinate(0.5, 0.5)
    # swipe( (0, y), (x, y))
    if not poco("同花顺自选").exists():
        raise  AssertionError("自选-点击大盘控件k线图-侧滑返回,没有返回到自选页面")