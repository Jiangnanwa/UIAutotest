#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_zijin_list_jump_fenshi 
   Description :
   Author : chenqiyue
   CreateDate：2024/03/11  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import sleep


@pytest.mark.parametrize("final_teardown_yidenglu", [{}], indirect=True)
@pytest.mark.parametrize("testcase_id,tab_name", [("1337464", "自选"), ("1337488", "沪深")])
def test_zijin_zixuanlist_jump_fenshi(poco, testcase_id, tab_name):
    """
    用例名称
    TC_看资金_自选列表_竖屏排序状态下跳转分时
    用例id
    1337464
    """
    poco(text="资金").click()
    sleep(2.0)
    print(tab_name)
    list_name = []
    if not poco(text="大盘主力净流入").exists():
        poco(text=tab_name).click()

        zixuanlist = poco(nameMatches=".*#.*")
        for i in zixuanlist:
            name = i.get_name()
            print(i)
            shuzhi = name.split('#')
            list_name.append(shuzhi[0])
        print(f"list_name{list_name}")
        # 点击列表中第一个股票
        print(f"点击列表中第一个股票{zixuanlist[0].get_name()}")
        zixuanlist[0].click()

    elif poco(text="大盘主力净流入").exists():
        matches = poco(textMatches="^d{6}$")
        stock=matches.sibling()
        for i in stock:
            name = i.get_name()
            print(i)
            stock_name = stock.get_text()
            list_name.append(stock_name)
        print(f"点击列表中第一个股票{matches[0].get_name()}")
        matches[0].click()

# 处理首次进入同屏个股详情页引导 "您可在当前页面切换周期啦~"
    if poco("com.hexin.plat.android:id/iknow").exists():
        poco("com.hexin.plat.android:id/iknow").click()
    sleep(2.0)
    navi_title_text = poco("com.hexin.plat.android:id/navi_title_text").get_text()

    if not navi_title_text == list_name[0]:
        raise AssertionError(f"看资金-自选-点击股票{list_name[0]}，进入的分时错误{navi_title_text},用例id{testcase_id}")
    for i in range(2):

        poco("com.hexin.plat.android:id/navi_right_icon").click()
        navi_title_text = poco("com.hexin.plat.android:id/navi_title_text").get_text()
        print(navi_title_text, "跳转前", list_name[i + 1])
        if not navi_title_text == list_name[i + 1]:
            raise AssertionError(f"看资金-自选-点击股票{list_name[i + 1]}，进入的分时错误{navi_title_text},用例id{testcase_id}")