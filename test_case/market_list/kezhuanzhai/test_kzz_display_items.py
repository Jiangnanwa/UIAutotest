#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_kzz_display_items 
   Description :
   Author : chenqiyue
   CreateDate：2024/01/06  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import sleep

from common.swipe_operations import horizontal_swipe_until_element_found, right_swipe_until_element_found


def test_kzz_display_items(poco):
    """
    用例id    用例名称
    1752756  TC_转债列表校验展示项
    操作步骤:
    """
    # 获取两个元素的位置信息
    zhuanzhai = poco(text="转债排行").get_position()
    mingcheng = poco(text="名称代码").get_position()

    # 检查转债排行元素是否在名称代码元素正上方
    if zhuanzhai[1] < mingcheng[1]:
        print("转债排行在名称代码上方")
    else:
        print("转债排行不在名称代码上方")
    biaotou = [("名称代码"), ("转债排行"), ("名称代码"), ("涨幅"), ("涨速"), ("转股溢价率"), ("转股价值"), ("成交额"),
               ("换手率"), ("正股名称"), ("正股最新价"), ("正股涨速"), ("正股涨幅"), ("正股PE"), ("正股波动率"), ("双低"),
               ("期权价值"), ("评级"), ("纯债价值"), ("转股价"), ("到期赎回价"), ("强赎触发价"), ("转债占比"), ("到期日期"),
               ("剩余年限"), ("剩余规模")]

    i = 2
    for item in biaotou:
        if poco(text=item).exists():
            print(f"{item}表头存在")
        else:
            # 横滑找元素
            # horizontal_swipe_until_element_found(poco(text=item), poco("com.hexin.plat.android:id/tv_value")[0])
            horizontal_swipe_until_element_found(poco(text=item), poco("com.hexin.plat.android:id/tv_value")[i],
                                                 max_swipes=30)
    poco("com.hexin.plat.android:id/tv_value")[2].swipe([-0.7271, 0.0023])
    # 获取强赎触发价元素
    qiangshu = poco(text="剩余规模")

    # 记录初始位置
    initial_position = qiangshu.get_position()

    # 执行滑动操作
    poco("com.hexin.plat.android:id/tv_value")[2].swipe([-0.7271, 0.0023])

    # 获取滑动后的强赎触发价元素位置
    updated_position = qiangshu.get_position()

    # 检查位置是否变化
    if initial_position == updated_position:
        print("位置无变化")
    else:
        raise AssertionError("位置有变化")
    #向右横滑到一直到最新
    right_swipe_until_element_found(poco,poco(text="最新"), poco("com.hexin.plat.android:id/tv_value")[2], max_swipes=100)
    # 获取可转债和转债排行元素
    kezhuanzhai = poco("可转债")
    zhuanzhai_paihang = poco(text="转债排行")

    # 记录初始位置
    initial_kezhuanzhai_position = kezhuanzhai.get_position()
    initial_zhuanzhai_paihang_position = zhuanzhai_paihang.get_position()

    # 执行三次滑动操作
    for i in range(3):
        poco(textMatches="转债.*|.*%").swipe([-0.027, -0.4721])
        poco(textMatches="转债.*|.*%").refresh()
        sleep(1.0)  # 等待页面加载

    # 记录滑动后的位置
    updated_kezhuanzhai_position = kezhuanzhai.get_position()
    updated_zhuanzhai_paihang_position = zhuanzhai_paihang.get_position()

    # 校验位置是否变化
    if (
            initial_kezhuanzhai_position[1] < initial_zhuanzhai_paihang_position[1]
            and updated_kezhuanzhai_position[1] < updated_zhuanzhai_paihang_position[1]
    ):
        print("可转债在转债排行正上方")
    else:
        print("可转债不在转债排行正上方")