#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_gwqh_jump_fenshi 
   Description :
   Author : chenqiyue
   CreateDate：$ 用例id:
-------------------------------------------------
"""
import time

import pytest
from airtest.core.api import keyevent, sleep

from common.app_operation import back_findelement


def test_hotlist_navigation(poco):
    """
用例名称
TC_推荐页_热点榜_页面跳转
用例id
1368852
    """

    # 初始化错误列表
    errors = []

    # 1. 校验综合TAB是否被选中
    try:
        assert poco(text="综合").attr('selected') == True, "综合TAB未被选中"
    except AssertionError as e:
        errors.append(str(e))

    # 2. 点击热点榜单中的标题
    hotlist_title = poco("com.hexin.plat.android:id/content").get_text()
    poco("com.hexin.plat.android:id/content").click()
    expected_title = f"#{hotlist_title}|{hotlist_title}"


    # 获取详情页中的标题并校验
    try:
        assert poco(textMatches=expected_title).exists(), "详情页中未找到标题"
    except AssertionError as e:
        errors.append(str(e))

    # 校验详情页布局合理，展示完整（根据具体UI元素添加详细的校验步骤）

    # 3. 按键返回
    back_findelement(poco(text="综合"))
    try:
        assert poco(text="综合").attr('selected') == True, "返回搜索页后综合TAB未被选中"
    except AssertionError as e:
        errors.append(str(e))
    sleep(2.0)
    # 4. 点击【查看更多】
    poco(text="查看更多").click()

    # 校验跳转至同花顺热榜页成功
    try:
        assert poco("com.hexin.plat.android:id/title_bar_middle").exists(), "未跳转至同花顺热榜页"
    except AssertionError as e:
        errors.append(str(e))

    assert poco(text="热门文章").exists(), "同花顺热榜页未找到相应标题"

    # 5. 点击左上角的返回
    poco("com.hexin.plat.android:id/title_bar_img").click()
    try:
        assert poco(text="综合").attr('selected') == True, "返回搜索页后综合TAB未被选中"
    except AssertionError as e:
        errors.append(str(e))

    if errors:
        raise AssertionError(" | ".join(errors))
