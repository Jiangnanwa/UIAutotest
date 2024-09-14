#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapan_zuorizhangtingbiaoxian 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/18  用例id:
-------------------------------------------------
"""
import re

from airtest.core.api import keyevent, sleep

from common.function import check_time_range, check_attr_updated, fenshixiangqingye_find_elements


def test_yesterday_limit_up(poco):
    """
    1752997 TC_昨日涨停表现_（回归）
    """
    sleep(5.0)
    # 确认昨日涨停表现元素是否存在
    yesterday_element = poco(text="昨日涨停表现")
    sleep(3.0)
    # 找到昨日涨停表现元素的兄弟节点
    sibling_element = yesterday_element.sibling()

    # 获取兄弟节点的所有 text 属性值
    # 校验报价头是否刷新
    if check_time_range():
        check_attr_updated(sibling_element, "text")
    else:
        print("当前时间不在允许的时间段内，不执行代码。")
    sibling_text_values = []
    for sibling in sibling_element:
        sibling_text_values.append(sibling.get_text())
    print(sibling_text_values)
    for text in sibling_text_values:
        print(text)
        # 检查文本不等于"--"并提取中文内容
        if text != "--":
            # 定义正则表达式模式
            pattern = r'[\u4e00-\u9fff]+\d+\.\d+%'

            # 使用正则表达式匹配文本
            match = re.match(pattern, text)

            # 检查是否匹配成功
            if match:
                sibling_text_value = match.group()
                print("匹配成功:", sibling_text_value)
        elif text == "--":
            raise AssertionError(f"昨日涨停表现数据{text}存在--")

    pos_initial = poco(text="昨日涨停表现").get_position()
    poco(text="昨日涨停表现").click()
    fenshixiangqingye_find_elements(poco("分时"), 1, poco)
    # 校验报价头是否刷新
    if check_time_range():
        check_attr_updated(poco("com.hexin.plat.android:id/fenshi_headline_view"), "desc")
    else:
        print("当前时间不在允许的时间段内，不执行代码。")
    # 校验 "com.hexin.plat.android:id/navi_title" 的 text 属性值是否为 "昨日涨停表现"
    sleep(3.0)
    if poco(text="我知道了").exists():
        poco(text="我知道了").click()
    # if not poco("com.hexin.plat.android:id/navi_title").get_text() == "昨日涨停表现":
    #     raise AssertionError("昨日涨停表现不存在")
    poco(text="成分股").swipe([0.0428, -0.366])

    sibling_text_value = re.sub(r'[^\u4e00-\u9fff]', '', sibling_text_value)
    # 校验 "com.hexin.plat.android:id/name" 的 text 属性值是否和 chengfengu 一致
    chengfengu = poco("com.hexin.plat.android:id/name").get_text()
    print(f"昨日涨停表现展示的股票:{sibling_text_value},进入详情页展示成份股tab下第一支股票是{chengfengu}")
    if not chengfengu == sibling_text_value:
        raise AssertionError("与昨日涨停表现的成份股tab处的涨幅榜的第一支股票不一致")
    poco(text="成分股").swipe([0.0428, -0.366])
    keyevent("BACK")
    # 获取返回后的行业板块元素位置坐标
    industry_pos_final = poco(text="昨日涨停表现").get_position()
    # 检查位置坐标是否相同
    if pos_initial == industry_pos_final:
        print("返回前后坐标未变化，验证通过")
    else:
        print("操作路径:大盘-点击昨日涨停表现按键返回上一级")

        raise AssertionError("返回前后坐标发生了变化，验证失败")
