#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：test_gerenzhongxin
   Description :TC_（已自动化）个股详情设置
   Author : wangsutong
   CreateDate：2024/06/21
   用例id:1101000
------------------------------------------------
"""
from airtest.core.api import touch, sleep
from airtest.core.cv import Template

import pytest


@pytest.mark.parametrize("final_teardown_gerenzhongxin", [{}], indirect=True)
def test_geguxiangqingshezhi(final_teardown_gerenzhongxin,poco):
    poco("com.hexin.plat.android:id/iv_personal_setting").click()
    poco(text="个股详情设置").click()
    assert poco(text="个股详情设置").exists(),"个股详情设置存在"
    poco("com.hexin.plat.android:id/title_bar_img").click()
    assert poco(text="系统设置").exists() , "未返回到上一级页面"


