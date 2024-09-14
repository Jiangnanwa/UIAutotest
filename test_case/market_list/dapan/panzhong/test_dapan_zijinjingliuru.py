#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapan_zijinjingliuru 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/12  用例id:
-------------------------------------------------
"""
from airtest.core.api import keyevent


def test_dapan_zijinjingliuru(poco):
    """
    用例id    用例名称
    1752966  TC_大盘_资金流入数据

    操作步骤:
    """
    # 查找元素并点击
    market_inflow = poco(text="大盘资金净流入")

    inflow = [market_inflow]
    for market_inflow in inflow:

        market_inflow.click()  # 点击"大盘资金净流入"

        # 检查是否选中
        if market_inflow.get_text() == "大盘资金净流入":

            # 检查是否存在"上证"元素
            if not poco(text="上证").exists():
                raise AssertionError("上证元素不存在")
        else:
            # 检查是否存在"上证"元素
            if not poco(text="深股通").exists():
                raise AssertionError("深股通元素不存在")
        keyevent('BACK')
