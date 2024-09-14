#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapanzhishumokuai 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/16  用例id:
-------------------------------------------------
"""
from airtest.core.api import sleep

from common.function import validate_stock_navigation


def test_dapanzhishumokuai_click_jump_check(poco):
    """
    用例id    用例名称
    1752973 TC_大盘指数模块_点击跳转校验
    操作步骤:
    """
    validate_stock_navigation(poco, poco("com.hexin.plat.android:id/index_name"),
                              poco("com.hexin.plat.android:id/navi_title_text"))


def test_dapanzhishumokuai_zhishu_switch(poco):
    """
    用例id    用例名称
    1752974 TC_大盘指数模块_指数切换校验
    操作步骤:
    """
    # 获取前三个元素的 text 值存入数组
    index_names = []
    elements = poco("com.hexin.plat.android:id/index_name")
    for i in range(2):
        index_names.append(elements[i].get_text())

    # 点击第一个元素
    elements[0].click()
    sleep(2)  # 等待页面加载

    # 获取第一个导航标题文本
    navi_title_text_1 = poco("com.hexin.plat.android:id/navi_title_text").get_text()

    # 点击第一个右侧图标
    poco("com.hexin.plat.android:id/navi_right_icon").click()
    sleep(2)  # 等待页面加载

    # 获取第二个导航标题文本
    navi_title_text_2 = poco("com.hexin.plat.android:id/navi_title_text").get_text()

    # 点击第二个右侧图标
    poco("com.hexin.plat.android:id/navi_right_icon").click()
    sleep(2)  # 等待页面加载

    # 获取第三个导航标题文本
    #navi_title_text_3 = poco("com.hexin.plat.android:id/navi_title_text").get_text()

    # 将获取的三个值和数组比较是否一致
    if [navi_title_text_1, navi_title_text_2] != index_names[:2]:

        print(f"获取的导航标题文本：{navi_title_text_1}, {navi_title_text_2}")
        print(f"数组内容：{index_names[:2]}")
        # 进行异常处理或其他操作
        raise  AssertionError("获取的导航标题文本和数组内容不一致！")
    else:
        print(f"获取的导航标题文本：{navi_title_text_1}, {navi_title_text_2}")
        print(f"数组内容：{index_names[:2]}")
        print("获取的导航标题文本和数组内容一致！")
