#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    theme_settings.py 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/07  用例id:
-------------------------------------------------
"""
from airtest.core.api import sleep, stop_app, start_app

def option_light_theme_switch(poco):
    stop_app("com.android.settings")
    start_app("com.android.settings")
    i = 0
    while i < 10:
        poco(text="WLAN").swipe([0, -0.1])
        sleep(1.0)
        i = i + 1
        if poco(text="显示和亮度").exists():
            poco(text="显示和亮度").click()
            break
    poco("DBSDeviceAppearanceOptionLight").wait().click()
