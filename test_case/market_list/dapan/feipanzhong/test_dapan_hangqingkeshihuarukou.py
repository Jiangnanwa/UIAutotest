#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapan_hangqingkeshihuarukou
   Description：  TC_行情可视化复盘入口点击
   Author：       duanxufei
   CreateDate：   2024/3/12 14:43
   CaseID：       1753985
-------------------------------------------------
"""
import time

from airtest.core.api import keyevent


def test_jinru(poco):
    """
    点击入口
        1.点击大盘下的每日市场复盘入口
        2.查看跳转页面
    """
    poco("行情").click()
    # tmp_list = poco("applications").offspring("android.widget.TextView")
    # for item in tmp_list:
    #     if item.get_text() == "大盘回顾":
    #         item.click()
    #         break
    while '每日市场复盘' != poco("com.hexin.plat.android:id/market_comment_title").get_text():
        time.sleep(1)
    poco("com.hexin.plat.android:id/market_comment_title").click()

    assert "行情可视化复盘" == poco("com.hexin.plat.android:id/page_content").child("android.widget.RelativeLayout").child(
        "android.webkit.WebView").child("android.webkit.WebView").get_text()


def test_fanhui(poco):
    """
    点击页面的返回按钮/手势返回
    """
    keyevent("BACK")



