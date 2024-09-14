#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    Debug_itesm 
   Description :
   Author : chenqiyue
   CreateDate：2023/09/20  用例id:
-------------------------------------------------
"""
class Debug_items_Page:
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    open_xiaobaiqiu = poco(text="打开或者关闭小白球")
    performance_data_item = poco(text="显示性能数据")
    performance_data = poco(textMatches = ".*性能")
