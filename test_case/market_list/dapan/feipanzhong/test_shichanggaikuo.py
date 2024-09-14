#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_shichanggaikuo 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/16  用例id:
-------------------------------------------------
"""
from common.function import check_time_range, check_attr_updated


def test_shichanggaikuo(poco):
    """
    用例id    用例名称
    1752989 TC_市场概况_跳转诊大盘
    操作步骤:
    """
    poco("com.hexin.plat.android:id/arrow").click()
    if not poco(text="诊大盘").exists():
        raise  AssertionError("tab未自动切换到诊大盘tab下")
    # 校验报价头是否刷新
    if check_time_range():
        check_attr_updated(poco(textMatches=".*家"), "text")
    else:
        print("当前时间不在允许的时间段内，不执行代码。")