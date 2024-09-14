#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapan_jinrizhangfuzuidabankuai
   Description：  TC_大盘_异动_热点板块_今日涨幅最大板块操作   需要使用debug包
   Author：       duanxufei
   CreateDate：   2024/3/13 10:04
   CaseID：       1753048
-------------------------------------------------
"""
import pytest
from airtest.core.api import keyevent

@pytest.mark.skip(reason="服务器未调试通过")
def test_dianjidiyige(poco):
    """
    跳转第一个热点板块
        1、点击第一个板块
    """
    poco("行情").click()

    while not (poco("board").exists() and poco("board").children()):
        if poco(text="意见反馈").exists():
            raise Exception("热点板块不存在")
        tmp_ele = poco("lazy_scroll").children()[1]
        tmp_ele.swipe([0, -tmp_ele.get_size()[1]], duration=1)

    poco(text="今日涨幅最大 ").click()
    # 第一个板块
    first_item = poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
        "com.hexin.plat.android:id/hsViewPager").offspring("com.hexin.plat.android:id/vertical_container").child(
        "android.webkit.WebView").offspring("board").child("android.view.View")[1].child("android.view.View").child(
        "android.view.View").child("android.view.View")[1].child("android.view.View").child("android.view.View").child(
        "android.view.View").child("android.view.View").child("android.view.View")[0]

    # 第一个板块的名称
    first_item_name = first_item.child("android.view.View")[0].get_text()
    first_item.click()
    # 如果有弹窗则点击
    if poco("com.hexin.plat.android:id/i_know").exists():
        poco("com.hexin.plat.android:id/i_know").click()
    assert first_item_name == poco("com.hexin.plat.android:id/navi_title_text").get_text()

@pytest.mark.skip(reason="服务器未调试通过")
def test_fanhui(poco):
    """
    返回
        1、点击返回按钮/物理返回/手势返回
    """
    poco("com.hexin.plat.android:id/backButton").click()
    assert poco("board").exists()

@pytest.mark.skip(reason="服务器未调试通过")
def test_bianlibankuai(poco):
    """
    遍历所有板块跳转返回
        1、向左滑动，遍历点击所有板块并返回
    """
    bankuai_item_list = poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
        "com.hexin.plat.android:id/hsViewPager").offspring("com.hexin.plat.android:id/vertical_container").child(
        "android.webkit.WebView").offspring("board").child("android.view.View")[1].child("android.view.View").child(
        "android.view.View").child("android.view.View")[1].child("android.view.View").child("android.view.View").child(
        "android.view.View").child("android.view.View").child("android.view.View")
    for bankuai_item in bankuai_item_list:
        if bankuai_item.get_bounds()[1] > 1:
            break
        bankuai_item_name = bankuai_item.child("android.view.View")[0].get_text()
        bankuai_item.click()
        assert bankuai_item_name == poco("com.hexin.plat.android:id/navi_title_text").get_text()
        poco("com.hexin.plat.android:id/backButton").click()
        assert poco("board").exists()

@pytest.mark.skip(reason="服务器未调试通过")
def test_zuoyouhuadong(poco):
    """
    左右滑动
    """
    bankuai_item_list = poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
        "com.hexin.plat.android:id/hsViewPager").offspring("com.hexin.plat.android:id/vertical_container").child(
        "android.webkit.WebView").offspring("board").child("android.view.View")[1].child("android.view.View").child(
        "android.view.View").child("android.view.View")[1].child("android.view.View").child("android.view.View").child(
        "android.view.View").child("android.view.View").child("android.view.View")
    bankuai_item_list[-2].swipe([-0.5, 0])

