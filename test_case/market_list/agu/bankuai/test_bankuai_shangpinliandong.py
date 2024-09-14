#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_bankuai_shangpinliandong 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/06  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import  sleep

from common.function import find_element_within_timeout, scroll_element_below_another_element



@pytest.mark.parametrize("tab,tabname, biaotou", [
    ("com.hexin.plat.android:id/tv_qhld", "期股联动", "涨幅"), ("com.hexin.plat.android:id/tv_xhld", "现货联动", "涨幅"),
    ("com.hexin.plat.android:id/tv_cyld", "产业联动", "同比变化")
])
def test_bankuai_shangpinliandong_asc(poco, tab, tabname,biaotou):
    """
    TC_商品联动_切换期股联动_{biaotou}升序
    用例id
    1300857
    """

    # 调用函数并指定要查找的元素
    find_element_within_timeout(poco(text="商品联动"), timeout=500)
    # 把对应板块移动到板块tab下方100
    bankuaitab = poco("com.hexin.plat.android:id/bankuai")
    scroll_element_below_another_element(poco(text="商品联动"), bankuaitab, poco(text="商品联动"))
    #scroll_element_below_another_element(poco, poco(text="商品联动"), bankuaitab)
    sleep(2.0)

    poco(tab).click()
    poco(text=biaotou).click()
    # swipe((0.5 * w, 0.8 * h), vector=(0, -0.2), duration=0.1)  # 在0.2s内上划0.3个屏幕
    first_item = poco("com.hexin.plat.android:id/rv_sector_good")
    zhangfu_elements = first_item.offspring("com.hexin.plat.android:id/stock_zhangfu")
    # 获取所有 bankuai_zhangfu 元素的文本值，去掉百分号并转换为数字
    zhangfu_values = [element.get_text().replace('%', '') for element in zhangfu_elements]
    print(zhangfu_values)
    # 检查文本值是否按照升序排列
    sorted_values = sorted(zhangfu_values, reverse=False, key=float)
    print(sorted_values)
    if zhangfu_values == sorted_values:
        print("文本值按照升序排列")
    else:
        print("文本值未按照升序排列")
        raise AssertionError("文本值未按照升序排列")


@pytest.mark.parametrize("tab", [
    ("com.hexin.plat.android:id/tv_qhld"), ("com.hexin.plat.android:id/tv_xhld"), ("com.hexin.plat.android:id/tv_cyld")
])
def test_bankuai_shangpinliandong_des(poco, tab):
    """
    TC_商品联动_切换期股联动涨幅降序
    用例id
    1300857
    """

    # 调用函数并指定要查找的元素文本和超时时间
    find_element_within_timeout(poco(text="商品联动"), timeout=500)
    # 把对应板块移动到板块tab下方100
    bankuaitab = poco("com.hexin.plat.android:id/bankuai")
    scroll_element_below_another_element(poco(text="商品联动"), bankuaitab, poco(text="商品联动"))
    poco("com.hexin.plat.android:id/right_more").swipe([0.003, 0.0595])
    sleep(2.0)
    poco(tab).click()
    first_item = poco("com.hexin.plat.android:id/rv_sector_good")
    # 获取第一个 rv_sector_item 元素下的所有 bankuai_zhangfu 元素
    zhangfu_elements = first_item.offspring("com.hexin.plat.android:id/stock_zhangfu")
    # 获取所有 bankuai_zhangfu 元素的文本值，去掉百分号并转换为数字
    sleep(1.0)
    zhangfu_values = [element.get_text().replace('%', '') for element in zhangfu_elements]
    print(zhangfu_values)
    # 检查文本值是否按照升序排列
    sorted_values = sorted(zhangfu_values, reverse=True, key=float)
    print(sorted_values)
    if zhangfu_values == sorted_values:
        print("文本值按照降序排列")
    else:
        print("文本值未按照降序排列")
        raise AssertionError("文本值未按照降序排列")



