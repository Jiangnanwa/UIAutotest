#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_zidingyi_fenzu_jump 
   Description :
   Author : chenqiyue
   CreateDate：2024/03/07  用例id:
-------------------------------------------------
"""
import pytest

from common.app_operation import back_findelement


@pytest.mark.parametrize("final_teardown_yidenglu", [{}], indirect=True)
def test_zidingyi_group_jump(poco):
    """
    用例名称
    TC_自选侧边栏_已登录跳转自定义分组
    用例id
    1244492
    """
    #try:
    stock_group_name = poco("com.hexin.plat.android:id/stock_group_name").get_text()
    print(stock_group_name)
    poco("com.hexin.plat.android:id/stock_group_name").click()
    # 定义要校验的元素列表
    elements_to_check = [
        (poco('com.hexin.plat.android:id/slidingmenu_menu'), "slidingmenu_menu"),
        (poco('com.hexin.plat.android:id/voice_assistant'), "voice_assistant"),
        (poco(stock_group_name), "stock_group_name"),
        (poco('com.hexin.plat.android:id/new_title_search'), "new_title_search")
    ]

    # 遍历元素列表，逐个校验元素是否存在
    for locator, element_name in elements_to_check:
        if not locator.exists():
            raise AssertionError(f"Element '{element_name}' not found.")
        else:
            print(f"Element '{element_name}' found.")
    # finally:
    #     zixuan = poco(text="自选", name="com.hexin.plat.android:id/title")
    #     print("finally恢复页面，回到自选股页面")
    #     # 恢复页面，回到自选股页面
    #     if not zixuan.exists():
    #         back_findelement(zixuan)
    #     if zixuan.exists():
    #         zixuan.click()
    #     elif poco("自选").exists():
    #         poco("自选").click()
    #     poco("com.hexin.plat.android:id/slidingmenu_menu").click()
    #     poco("com.hexin.plat.android:id/self_group_btn").click()
    #     poco("com.hexin.plat.android:id/self_stock_name").click()
