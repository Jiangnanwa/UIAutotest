#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_kzz_tljh 
   Description :
   Author : chenqiyue
   CreateDate：2024/01/18  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import sleep, keyevent

from common.swipe_operations import horizontal_swipe_until_element_found

daoqi_biaotous = ["赎回收益", "最新", "到期赎回价", "到期日期"]
zhejia_biaotous = ["理论收益/手", "转股溢价率", "转股价值"]
shuangdi_biaotous = ["双低", "最新", "转股溢价率"]


@pytest.mark.parametrize("tab,testcaseid,explanation,biaotou,biaotous",
                         [("到期赎回套利", "用例id:1752752", "即将到期的可转债，上市公司可能会在到期日以赎回的价格买回可转债。当可转债价格低于赎回价，存在套利机会。", "赎回收益", daoqi_biaotous),
                          ("双低套利", "用例id:1752749", "双低值表示可转债的当前市场价值被低估的程度，双低值越低越容易获利。", "双低",
                           shuangdi_biaotous),
                          ("折价转股套利", "用例id:1752748", "转股期内，溢价率小于0时存在套利机会，且溢价率越小越安全。实行T+1交易制。(默认显示距离转股日10天内，溢价率小于0的可转债)", "理论收益/手",
                           zhejia_biaotous)])
def test_kzz_taolijihui_daoqishuhui(poco, tab,testcaseid, explanation, biaotou, biaotous):
    """
    用例id    用例名称

    1752752  TC_到期赎回套利交互
    1752748 TC_折价转股套利交互
    1752749 TC_双低套利交互
    操作步骤:
    """
    if not poco(text="转债排行").exists():
        keyevent("BACK")
    poco(text="套利机会").click()
    poco(text=tab).click()
    sleep(3)
    if not poco(text=explanation).exists():
        raise AssertionError(f"没有进入到{tab}页面,{testcaseid}")
    # 获取所有的元素
    elements = poco("com.hexin.plat.android:id/tv_value")

    # 遍历元素
    for element in elements:
        # 获取元素的text属性值
        text_value = element.get_text()

        # 校验text值是否等于--
        if text_value == "--":
            # 如果等于--，则抛出异常
            raise ValueError(f"数据存在--：{text_value},{testcaseid}")
        else:
            print("数据无--")

    # 校验是否是按照赎回收益降序
    # 初始化存储元素text的数组
    text_values = []
    # 遍历元素，根据下标 (i-1)%4 == 0 存储text值
    for i, element in enumerate(elements):
        if (i - 1) % 4 == 0:
            text_values.append(element.get_text())
    text_values = text_values[:-2]

    # 检查数组是否是降序
    if tab == "双低套利":
        jiangxu = sorted(text_values, reverse=False, key=float)
    else:
        jiangxu = sorted(text_values, reverse=True, key=float)
    if text_values == jiangxu:
        print(f"数组是降序的{text_values}，功能正常,代码降序{jiangxu},{testcaseid}")
    else:
        print(f"{text_values}")
        raise AssertionError(f"数组不是降序的{text_values}，存在问题,代码降序{jiangxu},{testcaseid}")
    # 检查数组是否是赎回收益升序
    poco(text=biaotou).click()
    # 初始化存储元素text的数组
    text_values = []
    # 遍历元素，根据下标 4n+1 存储text值
    for i, element in enumerate(elements):
        if (i - 1) % 4 == 0:
            text_values.append(element.get_text())
    if tab == "双低套利":
        paixu = sorted(text_values, reverse=True, key=float)
    else:
        paixu = sorted(text_values, reverse=False, key=float)
    if text_values == paixu:
        print("数组是升序的")
    else:
        raise AssertionError("点击赎回收益表头后,列表数据不是升序的，存在问题")
    # 校验表头

    i = 2
    for item in biaotous:
        if poco(text=item).exists():
            print(f"{item}表头存在,{testcaseid}")
        else:
            # 横滑找元素
            # horizontal_swipe_until_element_found(poco(text=item), poco("com.hexin.plat.android:id/tv_value")[0])
            horizontal_swipe_until_element_found(poco(text=item), poco("com.hexin.plat.android:id/tv_value")[i],
                                                 max_swipes=30)
    # 执行三次滑动操作
    for i in range(3):
        poco(textMatches=".*转债|.*%").swipe([-0.027, -0.4721])
        poco(textMatches=".*转债|.*%").refresh()
    sleep(3.0)
    # if not poco(text=biaotou).exists():
    #     raise AssertionError(f"滑动列表{tab}后,表头{biaotou}不存在,{testcaseid}")
    if poco(text=explanation).exists():
        raise AssertionError(f"滑动列表{tab}后,提示依然存在,没有进行置顶,{testcaseid}")
    if not poco(text="转债排行").exists():
        keyevent("BACK")

