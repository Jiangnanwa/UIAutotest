#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_changwai_jijin_jump 
   Description :
   Author : chenqiyue
   CreateDate：2024/03/08  用例id:
-------------------------------------------------
"""

from airtest.core.api import keyevent, sleep, touch
import pytest
from airtest.core.assertions import assert_exists
from airtest.core.cv import Template

from common.app_operation import back_findelement


@pytest.mark.parametrize("final_teardown_yidenglu", [
    {"username": "zyyt17", "password": "zyy123", "nicheng": "初出茅庐的青..."}
], indirect=True)
def test_changwai_jijin_jump(final_teardown_yidenglu, poco):
    """
    用例id   1846711  用例名称
     自选列表-点击场外基金-跳转查看是否正常
    操作步骤:
    """
    sleep(2.0)

    back_findelement(poco(text="行情"))
    touch(Template(r"场外.png", record_pos=(-0.231, -0.154), resolution=(1080, 2340)))
    if poco("com.hexin.plat.android:id/fund_detail_top_navigation_back").exists():
        poco("com.hexin.plat.android:id/fund_detail_top_navigation_back").click()
    else:
        keyevent('BACK')
    sleep(3.0)
    assert_exists(Template(r"场外.png", record_pos=(-0.231, -0.154), resolution=(1080, 2340)), "没有场外基金标识")
