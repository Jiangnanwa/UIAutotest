#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapan_gupiaopaihanggengduo
   Description：  TC_大盘_股票排行_一级列表_更多 需要使用debug包
   Author：       duanxufei
   CreateDate：   2024/3/13 11:19
   CaseID：       1753036
-------------------------------------------------
"""

import pytest


@pytest.mark.skip(reason="服务器未调试通过")
def test_tiaozhuanerjiliebiao(poco):
    """
    跳转二级列表
        1、任意选择一个榜单列表，点击列表下方查看更多按钮
    """
    poco("行情").click()

    while not (poco("ranking").exists() and poco("ranking").children() and poco(text="查看更多").exists()):
        if poco(text="意见反馈").exists():
            raise Exception("股票排行不存在")
        tmp_ele = poco("lazy_scroll").children()[1]
        tmp_ele.swipe([0, -tmp_ele.get_size()[1]], duration=1)

    poco(text="查看更多").click()
    assert "股票排行" == poco("com.hexin.plat.android:id/title_bar_middle_container").child(
        "android.widget.TextView").get_text()
    assert poco("com.hexin.plat.android:id/new_title_search").exists()


@pytest.mark.skip(reason="服务器未调试通过")
def test_fanhui(poco):
    """
    返回
        1、点击返回按钮/物理返回/手势返回
    """

    poco("com.hexin.plat.android:id/title_bar_img").click()
    assert poco("ranking").exists()


@pytest.mark.skip(reason="服务器未调试通过")
def test_tiaozhuanzijin(poco):
    """
    跳转资金页面
        1、选中大单净量榜单，点击列表下方查看更多按钮
    """

    if poco(text="大单净量").get_bounds()[1] > 1:
        poco(text="涨幅榜").swipe([-0.5, 0])
    poco(text="大单净量").click()

    poco(text="查看更多").click()
    assert "股票排行" == poco("com.hexin.plat.android:id/title_bar_middle_container").child(
        "android.widget.TextView").get_text()
    assert poco("com.hexin.plat.android:id/new_title_search").exists()
    poco("com.hexin.plat.android:id/title_bar_img").click()
    assert poco("ranking").exists()


@pytest.mark.skip(reason="服务器未调试通过")
def test_tiaozhuanzhulijingliuru(poco):
    """
    跳转资金页面
        1、选中主力净流入榜单，点击列表下方查看更多按钮
    """

    if poco(text="主力净流入").get_bounds()[1] > 1:
        poco(text="大单净量").swipe([-0.5, 0])
    poco(text="主力净流入").click()

    poco(text="查看更多").click()
    assert "股票排行" == poco("com.hexin.plat.android:id/title_bar_middle_container").child(
        "android.widget.TextView").get_text()
    assert poco("com.hexin.plat.android:id/new_title_search").exists()
    poco("com.hexin.plat.android:id/title_bar_img").click()
    assert poco("ranking").exists()
