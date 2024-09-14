#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapan_yidongtioazhuan
   Description：  TC_大盘_异动_大盘异动跳转
   Author：       duanxufei
   CreateDate：   2024/3/12 16:34
   CaseID：       1753039
-------------------------------------------------
"""
from airtest.core.api import keyevent

from common.swipe_operations import scroll_element_into_view


def test_dianjidapanyidong(poco):
    """
    点击大盘异动图表区域
        1、点击大盘异动图表区域
        2、滑动查看分时
    """
    poco("行情").click()

    while not (poco("change").exists() and poco("change").children() and poco("change").offspring(name="chart").get_bounds()[2] < 1):
        if poco(text="意见反馈").exists():
            raise Exception("异动不存在")
        tmp_ele = poco("lazy_scroll").children()[1]
        tmp_ele.swipe([0, -tmp_ele.get_size()[1]], duration=1)
    poco(text="大盘异动").click()
    poco("change").offspring(name="chart").click()
    assert "上证指数" == poco("com.hexin.plat.android:id/navi_title_text").get_text()


def test_fanhui(poco):
    """
    点击返回按钮/物理返回/手势返回
    """
    keyevent('BACK')
    assert poco("change").exists()
