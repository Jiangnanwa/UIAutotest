#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_kzz_jump_fenshi 
   Description :
   Author : chenqiyue
   CreateDate：2024/01/03  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import keyevent, sleep

# 封装数据
test_data = [
    ("套利机会", "用例id:1752752",
     ["双低套利", "转股期内，溢价率小于0时存在套利机会，且溢价率越小越安全。实行T+1交易制。(默认显示距离转股日10天内，溢价率小于0的可转债)"]),
    ("打新债", "用例id:1752753", ["今日中签公布", "待申购"]),
    ("抢权配债", "用例id:1752707", ["针对未发行的转债，提前买入正股，可以获得配债权，执行配债后可获相应转债。配债与打新互不干扰，有机会享受双份收益哦"])
]


# 使用pytest.mark.parametrize装饰器传入参数
@pytest.mark.parametrize("function, testcaseid, page_elements", test_data)
def test_kzz_function_jump(poco, function, testcaseid, page_elements):
    """
    用例id    用例名称

    1752752  TC_套利机会
    "抢权配债", "用例id:1752707"
    1752753  TC_打新债
    操作步骤:
    """
    poco(text=function).click()
    sleep(3.0)
    for page_element in page_elements:

        print(page_element)
        if not poco(text=page_element).exists():
            raise AssertionError(f"没有进入{function}页面,因为{page_element}元素没有展示,{testcaseid}")
    if function == "抢权配债":
        poco(text="策略解读").click()
        if not poco(
                text="上市公司发行可转债会有一定比例对持股股东进行优先配售，提前买入正股，可以获得配债权，执行配债后进而享受新债上市的收益。同时，配售转债与转债打新互不干扰。").exists() and poco(
            text="标签说明").exists():
            raise AssertionError(f"点击详细规则,没有展示详细规则里弹窗显示详细说明：标题策略解读、抢权配债策略简介、标签说明", {testcaseid})
        poco(text="我知道了").click()
        # poco(text="发行市场").click()
        # navi_title_text = poco("com.hexin.plat.android:id/navi_title_text").get_text()
        # if not poco(text="发行市场").exists():
        #     keyevent("BACK")
        # if not poco(text=navi_title_text).exists():
        #     raise AssertionError(f"点击列表热区没有跳转到跳转至对应的正股分时详情页,跳转到{navi_title_text}的详情页", {testcaseid})
    if not poco(text="转债排行").exists():
        keyevent("BACK")
