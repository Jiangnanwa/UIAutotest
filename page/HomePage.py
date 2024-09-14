#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：HomePage 
   Description :
   Author : chenqiyue
   CreateDate：2023/03/23 
   用例id:
------------------------------------------------
"""


class HomePage:
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    hangqing = poco("行情")
    xiaoxizhongxin = poco("消息中心")
    text_switcher = poco("com.hexin.plat.android:id/text_switcher")
    search_input = poco("com.hexin.plat.android:id/search_input")
    ths_shopping = poco(text="同顺商城")
