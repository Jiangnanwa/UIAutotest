#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapan_jiaoyizhuangtai 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/14  用例id:
-------------------------------------------------
"""
from datetime import datetime

from common.function import check_time_range


def test_dapan_jiaoyizhuangtai(poco):
    """
    用例id    用例名称
    1752965 TC_大盘_交易状态_开盘中校验
    操作步骤:
    """
    # 中文数字转换字典
    chinese_weekday = {
        '0': '日',
        '1': '一',
        '2': '二',
        '3': '三',
        '4': '四',
        '5': '五',
        '6': '六'
    }
    if check_time_range():
        hs_index_trade_state = poco("com.hexin.plat.android:id/hs_index_trade_state")
        if hs_index_trade_state.exists() and hs_index_trade_state.get_text() != "开盘中":
            raise AssertionError("盘中大盘交易状态不是开盘中")
        hs_index_date = poco("com.hexin.plat.android:id/hs_index_date")
        if hs_index_date.exists():
            current_date = datetime.now().strftime("%Y-%m-%d 星期") + chinese_weekday[datetime.now().strftime("%w")]
            print(current_date)
            if hs_index_date.get_text() != current_date:
                raise AssertionError("日期格式不符合 x年x月x日 星期x 或者不是当日日期")
    else:
        print("当前时间不在允许的时间段内，不执行代码。")
