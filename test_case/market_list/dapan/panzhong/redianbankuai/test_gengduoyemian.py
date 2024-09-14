#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_gengduoyemian
   Description：  TC_大盘_异动_热点板块_更多页面跳转   需要使用debug包
   Author：       duanxufei
   CreateDate：   2024/3/13 10:59
   CaseID：       1753993
-------------------------------------------------
"""

import pytest


@pytest.mark.skip(reason="服务器未调试通过")
def test_jinrizhuangfuzuidagengduo(poco):
    """
    今日涨幅最大更多跳转
        1、滑动今日涨幅最大板块至最后
        2.点击更多按钮
    """
    poco("行情").click()

    while not (poco("board").exists() and poco("board").children()):
        if poco(text="意见反馈").exists():
            raise Exception("热点板块不存在")
        tmp_ele = poco("lazy_scroll").children()[1]
        tmp_ele.swipe([0, -tmp_ele.get_size()[1]], duration=1)

    poco(text="今日涨幅最大").click()
    bankuai_item_list = poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
        "com.hexin.plat.android:id/hsViewPager").offspring("com.hexin.plat.android:id/vertical_container").child(
        "android.webkit.WebView").offspring("board").child("android.view.View")[1].child("android.view.View").child(
        "android.view.View").child("android.view.View")[1].child("android.view.View").child("android.view.View").child(
        "android.view.View").child("android.view.View").child("android.view.View")
    swipe_num = 0
    while not poco(text="查看更多").exists() and swipe_num < 10:
        bankuai_item_list[-2].swipe([-0.5, 0])
        swipe_num += 1
        if swipe_num == 10:
            raise Exception("查看更多按钮不存在")
    poco(text="查看更多").click()
    assert "板块" == poco("com.hexin.plat.android:id/title_bar_middle").get_text()

@pytest.mark.skip(reason="服务器未调试通过")
def fanhui_1(poco):
    """
    返回
        1、点击返回按钮/物理返回/手势返回
    """

    poco("com.hexin.plat.android:id/title_bar_img").click()
    assert poco("board").exists()

@pytest.mark.skip(reason="服务器未调试通过")
def test_zijinliuruzuiduogengduo(poco):
    """
    资金流入最多更多跳转
        1、滑动资金流入最多板块至最后
        2.点击更多按钮
    """

    poco(text="资金流入最多").click()
    bankuai_item_list = poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
        "com.hexin.plat.android:id/hsViewPager").offspring("com.hexin.plat.android:id/vertical_container").child(
        "android.webkit.WebView").offspring("board").child("android.view.View")[1].child("android.view.View").child(
        "android.view.View").child("android.view.View")[1].child("android.view.View").child("android.view.View").child(
        "android.view.View").child("android.view.View").child("android.view.View")
    swipe_num = 0
    while not poco(text="查看更多").exists() and swipe_num < 10:
        bankuai_item_list[-2].swipe([-0.5, 0])
        swipe_num += 1
        if swipe_num == 10:
            raise Exception("查看更多按钮不存在")
    poco(text="查看更多").click()
    assert "看资金" == poco("com.hexin.plat.android:id/title_bar_middle").get_text()

@pytest.mark.skip(reason="服务器未调试通过")
def fanhui_2(poco):
    """
    返回
        1、点击返回按钮/物理返回/手势返回
    """

    poco("com.hexin.plat.android:id/title_bar_img").click()
    assert poco("board").exists()

@pytest.mark.skip(reason="服务器未调试通过")
def test_5rizhangfuzuidagengduo(poco):
    """
    五日涨幅更多跳转
        1、滑动5日涨幅最大至最后
        2.点击更多按钮
    """

    poco(text="5日涨幅最大").click()
    bankuai_item_list = poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
        "com.hexin.plat.android:id/hsViewPager").offspring("com.hexin.plat.android:id/vertical_container").child(
        "android.webkit.WebView").offspring("board").child("android.view.View")[1].child("android.view.View").child(
        "android.view.View").child("android.view.View")[1].child("android.view.View").child("android.view.View").child(
        "android.view.View").child("android.view.View").child("android.view.View")
    swipe_num = 0
    while not poco(text="查看更多").exists() and swipe_num < 10:
        bankuai_item_list[-2].swipe([-0.5, 0])
        swipe_num += 1
        if swipe_num == 10:
            raise Exception("查看更多按钮不存在")
    poco(text="查看更多").click()
    assert "板块" == poco("com.hexin.plat.android:id/title_bar_middle").get_text()

@pytest.mark.skip(reason="服务器未调试通过")
def fanhui_3(poco):
    """
    返回
        1、点击返回按钮/物理返回/手势返回
    """

    poco("com.hexin.plat.android:id/title_bar_img").click()
    assert poco("board").exists()
