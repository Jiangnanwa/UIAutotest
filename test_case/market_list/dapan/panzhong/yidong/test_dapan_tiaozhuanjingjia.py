#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapan_tiaozhuanjingjia
   Description：  TC_大盘_异动_竞价异动_跳转竞价页面
   Author：       duanxufei
   CreateDate：   2024/3/12 17:29
   CaseID：       1753045
-------------------------------------------------
"""

from airtest.core.api import keyevent


def test_dianjijingjiazoushi(poco):
    """
    CaseID：       1753045
    点击竞价走势图区域
        1、点击竞价走势图区域
    """
    poco("行情").click()

    while not (poco("change").exists() and poco("change").children() and poco("change").offspring(name="chart").get_bounds()[2] < 1):
        if poco(text="意见反馈").exists():
            raise Exception("异动不存在")
        tmp_ele = poco("lazy_scroll").children()[1]
        tmp_ele.swipe([0, -tmp_ele.get_size()[1]], duration=1)
    poco(text="竞价异动").click()
    poco("change").offspring(name="chart").click()
    assert "集合竞价" == poco("com.hexin.plat.android:id/title_bar_middle").get_text()


def test_fanhui(poco):
    """
    点击返回按钮/物理返回/手势返回
    """
    keyevent('BACK')
    assert poco("change").exists()
