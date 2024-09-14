#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_kzz_zhangdiefenbu
   Description：  TC_涨跌分布图表_叠加正股数量_正股数量大于0_图表展示
   Author：       duanxufei
   CreateDate：   2024/3/15 9:49
   CaseID：       2025528
-------------------------------------------------
"""

from common.image import get_screenshot_by_element, cut_image, get_color


def test_setup(poco):
    """
    前提
        行情-可转债，点击涨跌分布卡片
        点击勾选正股数量
    """
    poco("行情").click()
    poco("com.hexin.plat.android:id/tool_bar").offspring("可转债").click()
    poco(text="涨跌分布").click()
    # 点击正股数量单选框
    poco(text="正股涨跌").sibling("android.widget.ImageView").click()


def test_dayu0(poco):
    """
    转债涨幅在大于0的区间_图表展示
        1：校验矩形颜色
    """
    # 先获取到图表所在的元素
    chart = poco("android.widget.ScrollView").offspring("android.widget.RelativeLayout")[0].child("android.view.View")
    tmp_path = get_screenshot_by_element(chart)
    # 将0~3%区间的图片裁切出来
    tmp_path_2 = cut_image(tmp_path, 1 / 11 * 6, 0, 1 / 11 * 7, 1, None, True)
    # 再切出来转债对应柱子的区间
    tmp_path_3 = cut_image(tmp_path_2, 0, 0, 0.5, 1, None, True)
    # 再切出来正股对应柱子的区间
    tmp_path_4 = cut_image(tmp_path_2, 0.5, 0, 1, 1, None, True)
    assert "red" in get_color(tmp_path_3, shield_list=['white'])
    assert "gray" == get_color(tmp_path_4, shield_list=['white'])


def test_xiaoyu0(poco):
    """
    转债涨幅在小于0的区间_图表展示
        1：校验矩形颜色
    """
    # 先获取到图表所在的元素
    chart = poco("android.widget.ScrollView").offspring("android.widget.RelativeLayout")[0].child("android.view.View")
    tmp_path = get_screenshot_by_element(chart)
    # 将-3~0%区间的图片裁切出来
    tmp_path_2 = cut_image(tmp_path, 1 / 11 * 4, 0, 1 / 11 * 5, 1, None, True)
    # 再切出来转债对应柱子的区间
    tmp_path_3 = cut_image(tmp_path_2, 0, 0, 0.5, 1, None, True)
    # 再切出来正股对应柱子的区间
    tmp_path_4 = cut_image(tmp_path_2, 0.5, 0, 1, 1, None, True)
    assert "green" == get_color(tmp_path_3, shield_list=['white'])
    assert "gray" == get_color(tmp_path_4, shield_list=['white'])


def test_dengyu0(poco):
    """
    转债涨幅在等于0的区间_图表展示
        1：校验矩形颜色
    """
    # 先获取到图表所在的元素
    chart = poco("android.widget.ScrollView").offspring("android.widget.RelativeLayout")[0].child("android.view.View")
    tmp_path = get_screenshot_by_element(chart)
    # 将0%区间的图片裁切出来
    tmp_path_2 = cut_image(tmp_path, 1 / 11 * 5, 0, 1 / 11 * 6, 1, None, True)
    # 再切出来转债对应柱子的区间
    tmp_path_3 = cut_image(tmp_path_2, 0, 0, 0.5, 1, None, True)
    # 再切出来正股对应柱子的区间
    tmp_path_4 = cut_image(tmp_path_2, 0.5, 0, 1, 1, None, True)
    assert "gray" == get_color(tmp_path_3, shield_list=['white'])
    assert "gray" == get_color(tmp_path_4, shield_list=['white'])
