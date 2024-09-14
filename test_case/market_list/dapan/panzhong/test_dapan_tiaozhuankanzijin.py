#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapan_tiaozhuankanzijin.py
   Description：  TC_大盘_跳转看资金
   Author：       duanxufei
   CreateDate：   2024/3/11 20:03
   CaseID：       1752967
-------------------------------------------------
"""

from common.image import get_screenshot_by_element, get_color


def test_tiaozhuankanzijin_1(poco):
    """
    CaseID：       1752967
    跳转看资金页面
        1、当前显示大盘资金净流入数据
        2、点击资金净流入数据区域
    """
    poco("行情").click()

    poco("com.hexin.plat.android:id/hs_index_funds_flow_tips").wait(timeout=30).click()

    tmp_png = get_screenshot_by_element(poco("com.hexin.plat.android:id/hs_funds_inflow_tips"))
    title_color = get_color(tmp_png, shield_list=['white', 'gray'])
    assert title_color == "black"
    poco("com.hexin.plat.android:id/title_bar_img").click()


