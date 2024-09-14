#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dongtaifenzu_jump 
   Description :
   Author : chenqiyue
   CreateDate：2024/07/23  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import touch
from airtest.core.cv import Template


@pytest.mark.parametrize("final_teardown_yidenglu", [{}], indirect=True)
def test_dongtaifenzu_jump(poco):
    """
用例名称
TC_自选侧边栏_已登录跳转动态分组
用例id
1244493
    """

    touch(Template(r"tpl1721726792961.png", record_pos=(-0.409, -0.113), resolution=(1080, 2340)))
    if poco(textMatches="美股,盘前涨幅.*").exists():
        poco(textMatches="美股,盘前涨幅.*").click()
    # 定义要校验的元素列表
    elements_to_check = [
        (poco('com.hexin.plat.android:id/slidingmenu_menu'), "slidingmenu_menu"),
        (poco('com.hexin.plat.android:id/voice_assistant'), "voice_assistant"),
        (poco("同花顺条件选股"), "stock_group_name"),
        (poco('com.hexin.plat.android:id/new_title_search'), "new_title_search"),
        (poco("com.hexin.plat.android:id/dg_header_collection_iv"), "dg_header_collection_iv")
    ]

    # 遍历元素列表，逐个校验元素是否存在
    for locator, element_name in elements_to_check:
        if not locator.exists():
            raise AssertionError(f"Element '{element_name}' not found.")
        else:
            print(f"Element '{element_name}' found.")
