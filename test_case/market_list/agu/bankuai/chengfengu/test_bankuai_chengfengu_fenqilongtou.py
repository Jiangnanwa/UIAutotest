#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_bankuai_chengfengu_fenqilongtou.py 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/12  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import sleep

from common.function import fenshixiangqingye_find_elements, find_element_within_timeout, check_attr_updated, \
    check_time_range

@pytest.mark.skip(reason="页面更改不适用自动化")
def test_bankuai_chengfengu_fenqilongtou(poco):
    """
        用例id    用例名称
        117508    TC_板块成分股tab_人气龙头模块（已实现自动化）

    """
    first_item = poco("com.hexin.plat.android:id/bankuai_name")
    first_item.click()
    if poco("com.hexin.plat.android:id/i_know").exists():
        poco("com.hexin.plat.android:id/i_know").click()
        sleep(2)  # 等待页面加载完成    # 把对应板块移动到板块tab下方100
    # 调用函数并指定要查找的元素文本和超时时间
    chengfengu_tab = poco(text="最新价")  # 把对应板块移动到板块tab下方100
    # 调用函数并指定要查找的元素文本和超时时间
    find_element_within_timeout(chengfengu_tab, timeout=20)
    # 步骤 1
    elements_stock_name = poco("com.hexin.plat.android:id/txt_stock_name")
    array_A = []
    for element in elements_stock_name:
        text_value = element.get_text()
        if text_value:
            array_A.append(text_value)

    # 校验龙虎榜图标是否存在
    assert poco(text="1").exists(), "Element with text '1' not found!"

    # 校验涨跌幅数据是否为空是否存在
    elements_zhangfu = poco("com.hexin.plat.android:id/txt_zhangfu")
    for element in elements_zhangfu:
        text_value = element.get_text()
        assert text_value, "Text value is empty for element!"

    # 步骤 4:点击第一个龙虎榜
    poco("com.hexin.plat.android:id/txt_stock_name")[0].click()
    # 进入到详情页的时候会有挂单分布的弹窗
    fenshixiangqingye_find_elements(poco("com.hexin.plat.android:id/navi_title_text"), 1, poco)
    # 步骤 5:获取股票名称
    first_record = poco("com.hexin.plat.android:id/navi_title_text").get_text()
    # 校验报价头是否刷新
    if check_time_range():
        check_attr_updated(poco("com.hexin.plat.android:id/fenshi_headline_view"), "desc")
    else:
        print("当前时间不在允许的时间段内，不执行代码。")
    # 步骤 6:切换股票
    poco("com.hexin.plat.android:id/navi_right_icon").click()

    # 步骤 7:获取下一个股票的名称
    second_record = poco("com.hexin.plat.android:id/navi_title_text").get_text()
    print(first_record, second_record)
    # 步骤 校验分时详情页的股票是否和成份股tab下的顺序一致
    if array_A[:2] != [first_record, second_record]:
        print("Error: Data mismatch!")
        print("Array A: ", array_A[:2])
        print("Records: ", [first_record, second_record])
        raise AssertionError("Data mismatch!")
