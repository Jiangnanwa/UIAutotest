# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """
# -------------------------------------------------
#    File Name：    分时K线功能
#    Description :分时K线核心用例
#    Author : 唐玉娇
#    CreateDate：2023/03/16
#    用例id:1791532
# -------------------------------------------------
# """
#
# import pytest
#
# from common.app_operation import stop_app_open_app
# from common.login import login_by_password
# from time import sleep
# from poco.drivers.ue4 import UE4Poco
# poco = UE4Poco()
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# from airtest.core.api import *
#
# @pytest.mark.skip
# def test_00_qianti():
#
#     ST.FIND_TIMEOUT = 30  # 设置隐式等待时长为30s
#     """
#     分时K线核心用例前提：登录同屏灰度内帐号，进入个股详情页
#     """
#     stop_app_open_app("com.hexin.plat.android")
#     sleep(10)
#     login_by_password("lwtest1149", "123456", "com.hexin.plat.android")
#
# @pytest.mark.skip
# def test_01_yindao():
#     """
#     处理同屏引导
#     """
#
#     ST.FIND_TIMEOUT = 30  # 设置隐式等待时长为30s
#     sleep(3)
#     # 点击 自选-同花顺进入个股详情页
#     if poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("自选").child(
#             "com.hexin.plat.android:id/icon").exists():
#         poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("自选").child(
#             "com.hexin.plat.android:id/icon").click()
#     else:
#         stop_app_open_app("com.hexin.plat.android")
#         sleep(10)
#         poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("自选").child(
#             "com.hexin.plat.android:id/icon").click()
#     sleep(5)
#     poco("同花顺#300033").click()
#
#     # 处理首次进入同屏个股详情页引导 "您可在当前页面切换周期啦~"
#     if poco("com.hexin.plat.android:id/iknow").exists():
#         poco("com.hexin.plat.android:id/iknow").click()
