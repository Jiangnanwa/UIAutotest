#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：
   Description :
   Author : zengwenxin
   CreateDate：2024/05/27  用例id:
-------------------------------------------------
"""


from airtest.core.api import connect_device, sleep, swipe, snapshot


from common.network_operations import disable_wifi, enable_wifi, lockunlock_screen
from common.function import check_attr_updated


def test_01_refresh(poco):
    """
    用例名称
    TC_大盘控件_收起状态盘中分时数据刷新
    用例id
    1238619
    """

    check_attr_updated(poco("com.hexin.plat.android:id/zhishu_value"), "text", second=60)
    # print(poco("com.hexin.plat.android:id/price").get_text())



def test_02_wlan(poco):
    # 断网重连

    disable_wifi(poco)
    sleep(10)#等待一段时间，确保 Wi-Fi 已经完全关闭
    enable_wifi(poco)
    sleep(10)

    check_attr_updated(poco("com.hexin.plat.android:id/zhishu_value"), "text", second=60)

def test_03_lock(poco):

    lockunlock_screen(poco)

    check_attr_updated(poco("com.hexin.plat.android:id/zhishu_value"), "text", second=60)


