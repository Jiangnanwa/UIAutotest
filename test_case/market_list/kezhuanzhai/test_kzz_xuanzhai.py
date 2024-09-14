#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_kzz_xuanzhai
   Description：  TC_选债
   Author：       duanxufei
   CreateDate：   2024/3/14 20:46
   CaseID：       1752706
-------------------------------------------------
"""
from airtest.core.api import keyevent
from time import sleep


def test_setup(poco):
    """
    前提
        行情-可转债-功能入口界面
    """
    poco("行情").click()
    poco("com.hexin.plat.android:id/tool_bar").offspring("可转债").click()


def test_jinruxuanzhai(poco):
    """
    选债跳转
        点击宫格的选债
    """
    poco(text="选债").click()
    assert "选债条件" == poco("com.hexin.plat.android:id/title_bar_middle").get_text()


def test_biaotou(poco):
    """
    筛选列表表头数据项
        查看筛选列表
    """
    target_list = ['最新', '涨幅', '涨速', '转股溢价率', '转股价值', '成交额', '正股涨速', '正股涨幅', '正股成交额', '评级', '剩余规模']
    header_name_list = []
    flag = False
    poco(text="查看可转债").click()

    while not flag:
        header_list = poco("com.hexin.plat.android:id/title_scrollview").child("android.widget.LinearLayout").child(
            "android.widget.LinearLayout")
        for item in header_list:
            if item.child("android.widget.TextView").exists():
                tmp_name = item.child("android.widget.TextView").get_text()
                if tmp_name and tmp_name not in header_name_list:
                    header_name_list.append(tmp_name)
        header_list[-2].drag_to(header_list[0])
        tmp = poco("com.hexin.plat.android:id/title_scrollview").child("android.widget.LinearLayout").child(
            "android.widget.LinearLayout")[-1].child("android.widget.TextView").get_text()
        if tmp in header_name_list:
            flag = True
    assert header_name_list == target_list
    keyevent("BACK")


def test_morenpaixu(poco):
    """
    表头默认排序
        查看筛选列表
    """
    poco(text="查看可转债").click()
    data_list = poco("com.hexin.plat.android:id/recyclerview_id").offspring(
        "com.hexin.plat.android:id/content_scrollview")
    tmp_data = None
    for item in data_list:
        current_data = float(item.offspring("com.hexin.plat.android:id/tv_value")[1].get_text()[0:-1])
        if tmp_data:
            assert tmp_data >= current_data
        tmp_data = current_data


def test_shengxu(poco):
    """
    单个表头排序校验
        1、查看筛选列表
        2、点击最新价升序排序
        3、等待15S更新
    """
    zuixin_button = poco("com.hexin.plat.android:id/title_scrollview").child("android.widget.LinearLayout").child(
        "android.widget.LinearLayout")[0]
    zuixin_button.click()
    zuixin_button.click()
    sleep(15)
    data_list = poco("com.hexin.plat.android:id/recyclerview_id").offspring(
        "com.hexin.plat.android:id/content_scrollview")
    tmp_data = None
    for item in data_list:
        current_data = float(item.offspring("com.hexin.plat.android:id/tv_value")[0].get_text())
        if tmp_data:
            assert tmp_data <= current_data
        tmp_data = current_data


def test_fanhui_1(poco):
    """
    选债结果页返回
        1、点击选债结果页面返回按钮/手势返回/物理返回
    """
    keyevent("BACK")
    assert "选债条件" == poco("com.hexin.plat.android:id/title_bar_middle").get_text()


def test_fanhui_2(poco):
    """
    选债条件页面返回
        1、点击选债结果页面返回按钮/手势返回/物理返回
    """
    keyevent("BACK")
    assert poco("com.hexin.plat.android:id/tool_bar").offspring("可转债").exists()
