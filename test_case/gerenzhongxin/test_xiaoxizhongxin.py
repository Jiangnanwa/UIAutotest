#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：test_xiaoxizhongxin
   Description :TC_消息中心（网页）
   Author : wangsutong
   CreateDate：2024/06/18
   用例id:1100946
------------------------------------------------
"""
import pytest

# @pytest.mark.parametrize("",[])
from airtest.core.api import exists, touch, sleep, keyevent
from airtest.core.cv import Template

from common.function import myFindElements

import pytest


@pytest.mark.parametrize("final_teardown_gerenzhongxin", [{}], indirect=True)
def test_xiaoxizhongxin(final_teardown_gerenzhongxin,poco):
    """
    用例名称
    TC_消息中心
    用例id
    1100946
    """
    print("消息中心")

    myFindElements("new setting", 1, poco)
    xiaoxizhongxin =poco("com.hexin.plat.android:id/msgview")

    print("进入个人中心")
    print("刷新消息中心按钮")
    xiaoxizhongxin.refresh()
    print("点击消息中心按钮")
    xiaoxizhongxin.click()
    print("校验消息中心页面内容")
    sleep(5.0)
    elements = [poco(text="消息中心"), poco(text="评论我的")]
    for i in elements:
        if not i.exists():
            raise AssertionError(f"{i}元素缺失")
    keyevent('BACK')
    assert poco("com.hexin.plat.android:id/iv_personal_setting").exists(), "未返回到上一级页面"





