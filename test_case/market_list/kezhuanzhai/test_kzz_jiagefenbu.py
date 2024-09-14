#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_kzz_jiagefenbu
   Description：  TC_可转债均价_价格分布_列表展示
   Author：       duanxufei
   CreateDate：   2024/3/15 21:25
   CaseID：       2025560
-------------------------------------------------
"""
from common.image import get_screenshot_by_element, ths_ocr, image_to_base64, get_device_full_screenshot

Temp_pic = None
Temp_str = None


def test_setup(poco):
    """
    用例id :2025560
    前提
        行情-可转债，点击可转债均价卡片
        点击价格分布tab
    """
    poco("行情").click()
    poco("com.hexin.plat.android:id/tool_bar").offspring("可转债").click()
    poco(text="可转债均价").click()
    poco(text="价格分布").click()


def test_jiaoyanbiaotou(poco):
    """
    表头展示
        1：校验价格分布列表的表头
    """
    # 先获取到图表所在的元素
    chart = poco(text="价格分布").parent().parent().sibling("android.view.ViewGroup").child("android.view.View")

    global Temp_pic, Temp_str
    Temp_pic = get_screenshot_by_element(chart)
    Temp_str = ths_ocr(image_to_base64(Temp_pic))
    target_text = Temp_str["text"].split("\n")[0]

    assert "价格区间 转债数量 平均涨幅" == target_text


def test_jiagequjian(poco):
    """
    价格区间展示
        1：校验价格分别价格区间列表内容
    """
    # 先获取到图表所在的元素
    global Temp_pic, Temp_str
    str_list = Temp_str["text"].split("\n")
    print(str_list)
    assert "<90" == str_list[1].split(" ")[0]
    assert "90~110" == str_list[2].split(" ")[0]
    assert "110~120" == str_list[3].split(" ")[0]
    assert "120~130" == str_list[4].split(" ")[0]
    assert "130" == str_list[5].split(" ")[0]
