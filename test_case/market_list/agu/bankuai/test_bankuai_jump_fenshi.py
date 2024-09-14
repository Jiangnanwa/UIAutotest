#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_bankuai_jump_fenshi 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/06  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import sleep, keyevent

from common.function import find_element_within_timeout, scroll_element_below_another_element, scroll_element_into_view
from common.sort_operations import sort_elements_by_percentage


@pytest.mark.parametrize("bankuai", [("概念板块"), ("地域板块"), ("行业板块"), ("风格板块")])
def test_record_and_check(poco, bankuai):
    """
    1300793   TC_行业板块_涨幅tab跳转板块分时页（回归）
    1300813 TC_概念板块_涨速tab跳转板块分时页（回归）
    1300833 TC_风格板块_量比tab跳转板块分时页（回归）
    1300850 TC_地域板块_涨幅tab跳转板块分时页（回归）
    步骤:行情-A股-板块-{bankuai}-跳转第一个板块分时页
    """
    # 调用函数并指定要查找的元素文本和超时时间
    find_element_within_timeout(poco(text=bankuai), timeout=200)
    # 把对应板块移动到板块tab下方100
    bankuaitab = poco("com.hexin.plat.android:id/bankuai")
    scroll_element_below_another_element(poco(text=bankuai), bankuaitab, poco("com.hexin.plat.android:id/right_more"))
    sleep(2.0)
    # 记录第一个 view_bankuai_tablayout_item 的 bankuai_name
    #zdf = poco(textMatches=".*%")
    first_item = poco("com.hexin.plat.android:id/bankuai_name")
    bankuai_name = first_item.get_text()
    print(bankuai_name)
    # 点击第一个 view_bankuai_tablayout_item
    first_item.click()

    # 如果弹出 i_know 弹窗，则点击
    if poco("com.hexin.plat.android:id/i_know").exists():
        poco("com.hexin.plat.android:id/i_know").click()
        sleep(2)  # 等待页面加载完成

    # 校验 navi_title_text 的值与 bankuai_name 是否一致
    navi_title_text = poco("com.hexin.plat.android:id/navi_title_text").get_text()
    if navi_title_text != bankuai_name:
        print(navi_title_text, bankuai_name)
        raise AssertionError(f"分享详情页和跳转的不一致,详情页的值:{navi_title_text},点击的板块{bankuai_name}")
    # 返回,校验是否按照涨幅排序
    keyevent("BACK")
    target = poco("com.hexin.plat.android:id/bankuai_zhangfu")
    if not target.exists():
        raise AssertionError("点击板块返回未按照涨幅排序")


@pytest.mark.parametrize("bankuai,sort ", [("商品联动", "desc"), ("商品联动", "asc")])
def test_record_and_check_spld(poco, bankuai, sort):
    """
     用例名称
    TC_商品联动_期股联动tab跳转板块分时页/ETF页面（回归）
    用例id
    1300869
    步骤:行情-A股-板块-{bankuai}-跳转第一个板块分时页
    """
    # 调用函数并指定要查找的元素文本和超时时间
    find_element_within_timeout(poco(text=bankuai), timeout=200)
    # 把对应板块移动到板块tab下方100
    bankuaitab = poco("com.hexin.plat.android:id/bankuai")
    scroll_element_below_another_element(poco(text=bankuai), bankuaitab,poco(text=bankuai))
    sleep(2.0)
    # 记录第一个期货名称
    first_item = poco("com.hexin.plat.android:id/stock_name")
    # 点击涨幅表头
    if sort == "asc":
        poco(text="涨幅").click()
    bankuai_name = first_item.get_text()
    print(bankuai_name)
    # 点击第一个期货
    first_item.click()

    # 如果弹出 i_know 弹窗，则点击
    if poco("com.hexin.plat.android:id/i_know").exists():
        poco("com.hexin.plat.android:id/i_know").click()
        sleep(2)  # 等待页面加载完成

    # 校验 navi_title_text 的值与 bankuai_name 是否一致
    navi_title_text = poco("com.hexin.plat.android:id/navi_title_text").get_text()
    if navi_title_text != bankuai_name:
        print(navi_title_text, bankuai_name)
        raise AssertionError(f"分享详情页和跳转的不一致,详情页的值:{navi_title_text},点击的板块{bankuai_name}")
    # 返回,校验是否按照涨幅排序
    keyevent("BACK")
    sort_elements_by_percentage(poco("com.hexin.plat.android:id/stock_zhangfu"), sorting_type=sort)
