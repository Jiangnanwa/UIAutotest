#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_changwaijijin_tag 
   Description :
   Author : chenqiyue
   CreateDate：2024/07/22  用例id:
-------------------------------------------------
"""
from time import sleep

import pytest
from airtest.core.api import start_app, keyevent
from airtest.core.assertions import assert_exists
from airtest.core.cv import Template

from common.app_operation import stop_app_open_app, back_findelement
from common.function import homePageFindElements
from common.login import login_by_password


# 其他测试函数
@pytest.mark.parametrize("final_teardown_yidenglu", [
    {"username": "zyyt17", "password": "zyy123", "nicheng": "初出茅庐的青..."}
], indirect=True)
def test_changwaijijin_tag(final_teardown_yidenglu, poco):
    """
用例名称
TC_UOFJ市场基金标识显示
用例id
1846710
    """
    back_findelement(poco(text="行情"))
    assert_exists(Template(r"场外.png", record_pos=(-0.231, -0.154), resolution=(1080, 2340)), "没有场外基金标识")
