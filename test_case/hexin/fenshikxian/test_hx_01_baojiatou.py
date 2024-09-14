# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """
# -------------------------------------------------
#    File Name：    分时K线功能-报价头
#    Description :分时K线核心用例
#    Author : 唐玉娇
#    CreateDate：2023/03/28
#    用例id:1791532
# -------------------------------------------------
# """
# import pytest
#
#
#
# @pytest.mark.skip
# def test_01_baojiatou():
#     from common.app_operation import stop_app_open_app
#     from common.login import login_by_password
#     from time import sleep
#     from poco.drivers.ue4 import UE4Poco
#     poco = UE4Poco()
#     from poco.drivers.android.uiautomation import AndroidUiautomationPoco
#     poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#     from airtest.core.api import *
#     from airtest.cli.parser import cli_setup
#     from common.function import jiaoyan_shujuxiang
#     """
#     1、校验报价头右侧数据项显示正确
#     2、校验现价、涨跌、涨跌幅、报价头右侧数据项数值不显示--
#     """
#     shujuxianglist = ["现价", "涨额", "涨幅", "高", "低", "开", "市值", "流通", "市盈_TTM", "量比", "换", "额"]
#     # 点击 自选-同花顺进入个股详情页
#     poco("com.hexin.plat.android:id/navi_title_text").wait_for_appearance(30)
#     gupiao_name = poco("com.hexin.plat.android:id/navi_title_text").get_text()
#     if gupiao_name != "同花顺":
#         stop_app_open_app("com.hexin.plat.android")
#         poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("自选").child("com.hexin.plat.android:id/icon").wait_for_appearance(30)
#         poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("自选").child("com.hexin.plat.android:id/icon").click()
#         poco("同花顺#300033").wait_for_appearance(15)
#         poco("同花顺#300033").click()
#
#     #获取报价头信息并校验数据项、数据值不为空或--
#     shujuxiang = poco("com.hexin.plat.android:id/fenshi_headline_view").attr("desc")
#     print(shujuxiang)
#     jiaoyan_shujuxiang(shujuxiang, shujuxianglist)
#
