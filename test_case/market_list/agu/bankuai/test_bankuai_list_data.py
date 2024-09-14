#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_bankuai_list_data 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/09  用例id:
-------------------------------------------------
"""
import re

import pytest
from airtest.core.api import keyevent, sleep

from common.function import fenshixiangqingye_find_elements, find_elements_with_same_x_position
from common.sort_operations import sort_elements_by_criteria, process_element_names, sort_elements_by_percentage
from common.swipe_operations import horizontal_swipe_until_element_found

# biaotou = [("涨幅", 1), ("主力净流入", 2), ("涨速", 4), ("量比", 5), ("涨家数", 6), ("跌家数", 7), ("5日涨幅", 8), ("10日涨幅", 9),
#            ("20日涨幅", 10), ("60日涨幅", 11), ("最新", 12), ("换手", 13), ("金额", 14), ("总手", 15)]
biaotou = [("涨幅", 1)]


@pytest.mark.parametrize("btn,biaotou,desc,asc", [("行业", biaotou, "desc", "asc"), ("全部", biaotou, "desc", "asc"),
                                                  ("概念", biaotou, "desc", "asc")])
def test_bankuai_list_sort_data(poco, btn, biaotou, desc, asc):
    """
    用例id     用例名称
    1300909 TC_全部板块_竖屏表头排序（回归）
    1300934 TC_行业板块_竖屏表头排序
    1300958 TC_概念板块_竖屏表头排序
    """
    right_more = poco("com.hexin.plat.android:id/right_more")
    # 记录位置
    sleep(2.0)
    right_more.click()
    sleep(2.0)
    poco(text=btn).click()
    for item in biaotou:
        horizontal_swipe_until_element_found(poco(text=item[0]), poco(textMatches=".*%"))
        print()
        if not item[0] == "涨幅":
            poco(text=item[0]).click()
        # 找到所有与第一个元素具有相同x位置的元素
        elements = find_elements_with_same_x_position(poco, ".*%", attr_name='pos')
        sort_elements_by_percentage(elements, sorting_type=desc)
        poco(text=item[0]).click()
        print("点击表头使表头升序")
        elements = find_elements_with_same_x_position(poco, ".*%", attr_name='pos')
        sort_elements_by_percentage(elements, sorting_type=asc)


# biaotou = [("涨幅", 1), ("主力净流入", 2), ("涨速", 4), ("量比", 5), ("涨家数", 6), ("跌家数", 7), ("5日涨幅", 8), ("10日涨幅", 9),
#            ("20日涨幅", 10), ("60日涨幅", 11), ("最新", 12), ("换手", 13), ("金额", 14), ("总手", 15)]
#
biaotou = [("涨幅", 1)]


@pytest.mark.parametrize("btn,biaotou", [("风格", biaotou), ("全部", biaotou),
                                         ("地域", biaotou)])
def test_bankuai_list_sort_data_jump_to_fenshi(poco, btn, biaotou):
    """
    用例id     用例名称
    1300911 TC_全部板块_排序状态跳转分时（回归）
    1300984 TC_风格板块_排序状态跳转分时
    1301008 TC_地域板块_排序状态跳转分时

    """
    right_more = poco("com.hexin.plat.android:id/right_more")
    # 记录位置
    right_more.wait(10).click()
    poco(text=btn).wait(10).click()
    for item in biaotou:
        navi_titles = []
        # 横滑找元素
        horizontal_swipe_until_element_found(poco(text=item[0]), poco(textMatches=".*%"))
        print()
        if not item[0] == "涨幅":
            poco(text=item[0]).click()
        elements_with_name = poco(textMatches=".*%")
        # bk_items = process_element_names(elements_with_name, 0)
        bk_items = []
        # 定义一个正则表达式来匹配6个数字的字符串
        # six_digit_pattern = re.compile(r'^\d{6}$')

        matches = poco(textMatches="^8\\d{5}$")

        for i in matches:
            # 检查是否已经添加了三个元素
            print(i.get_text())
            if len(bk_items) < 3:
                # 获取当前元素的兄弟节点的文本值
                bk_item = i.sibling("android.widget.TextView").get_text()
                # 将文本值添加到列表中
                bk_items.append(bk_item)
            else:
                # 如果已经添加了三个元素，就跳出循环
                break
        print(bk_items)
        elements_with_name[0].click()
        # 如果弹出 i_know 弹窗，则点击
        if poco("com.hexin.plat.android:id/i_know").exists():
            poco("com.hexin.plat.android:id/i_know").click()
            sleep(2)  # 等待页面加载完成
        # 校验 navi_title_text 的值与 bankuai_name 是否
        for i in range(3):
            navi_title_text = poco("com.hexin.plat.android:id/navi_title_text").get_text()
            navi_titles.append(navi_title_text)
            poco("com.hexin.plat.android:id/navi_right_icon").click()
        if navi_titles == bk_items:
            print(f"全部板块-更多列表-{btn}tab-{item}表头降序前三个股票名称:{bk_items}")
            print("分时详情页切换股票前三个股票名称:", navi_titles)
            print("更多-板块列表前三的数据和进入分时后切换的股票一致")
        else:
            print(f"全部板块-更多列表-{btn}tab-{item}表头降序前三个股票名称:{bk_items}")
            print("分时详情页切换股票前三个股票名称:", navi_titles)
            raise AssertionError("更多-板块列表前三的数据和进入分时后切换的股票不一致")
        # 返回上一级,表头降序
        keyevent('BACK')
        sleep(2)
        poco(text=item[0]).click()
        elements_with_name = poco(textMatches=".*%")
        bk_items = []
        # 定义一个正则表达式来匹配6个数字的字符串
        matches = poco(textMatches="^8\\d{5}$")

        for i in matches:

            # 检查是否已经添加了三个元素
            if len(bk_items) < 3:
                # 获取当前元素的兄弟节点的文本值
                bk_item = i.sibling("android.widget.TextView").get_text()
                # 将文本值添加到列表中
                bk_items.append(bk_item)
            else:
                # 如果已经添加了三个元素，就跳出循环
                break
        print(bk_items)
        elements_with_name[0].click()
        # 如果弹出 i_know 弹窗，则点击
        if poco("com.hexin.plat.android:id/i_know").exists():
            poco("com.hexin.plat.android:id/i_know").click()
            sleep(2)  # 等待页面加载完成
        # 校验 navi_title_text 的值与 bankuai_name 是否
        navi_titles = []
        for i in range(3):
            navi_title_text = poco("com.hexin.plat.android:id/navi_title_text").get_text()
            navi_titles.append(navi_title_text)
            poco("com.hexin.plat.android:id/navi_right_icon").click()

        if navi_titles == bk_items:
            print(f"全部板块-更多列表-{btn}tab-{item}表头升序前三个股票名称:{bk_items}")
            print("分时详情页切换股票前三个股票名称:", navi_titles)
            print("更多-板块列表前三的数据和进入分时后切换的股票一致")
        else:
            print(f"全部板块-更多列表-{btn}tab-{item}表头升序前三个股票名称:{bk_items}")
            print("分时详情页切换股票前三个股票名称:", navi_titles)
            raise AssertionError("更多-板块列表前三的数据和进入分时后切换的股票不一致")
        keyevent('BACK')
