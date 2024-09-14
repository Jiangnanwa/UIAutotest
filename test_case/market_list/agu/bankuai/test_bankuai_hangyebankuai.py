#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_bankuai_hangyebankuai 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/06  用例id:
-------------------------------------------------
"""




def test_hangye_zhangfu_paixu_asc(poco):
    """
    TC_行业板块切换涨幅升序
    用例id
    1300781

    """

    poco(text="涨幅").wait(15).click()
    first_item = poco("com.hexin.plat.android:id/rv_sector_item")[0]

    # 获取第一个 rv_sector_item 元素下的所有 bankuai_zhangfu 元素
    zhangfu_elements = first_item.offspring("com.hexin.plat.android:id/bankuai_zhangfu")

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


def test_hangye_zhangfu_paixu_des(poco):
    """
    TC_行业板块切换涨幅降序
    用例id
    1300781

    """


    first_item = poco("com.hexin.plat.android:id/rv_sector_item")[0]

    # 获取第一个 rv_sector_item 元素下的所有 bankuai_zhangfu 元素
    zhangfu_elements = first_item.offspring("com.hexin.plat.android:id/bankuai_zhangfu")

    # 获取所有 bankuai_zhangfu 元素的文本值，去掉百分号并转换为数字
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


def test_hangye_zhangsu_paixu_des(poco):
    """
    用例名称
    TC_行业板块切换涨速降序
    用例id
    1300782
    """

    poco(text="涨速").wait(15).click()
    first_item = poco("com.hexin.plat.android:id/rv_sector_item")[0]

    # 获取第一个 rv_sector_item 元素下的所有 bankuai_zhangfu 元素
    zhangsu_elements = first_item.offspring("com.hexin.plat.android:id/sector_sort_value")

    # 获取所有 zhangsu_values 元素的文本值，去掉百分号并转换为数字
    zhangsu_values = [element.get_text().replace('%', '') for element in zhangsu_elements]
    print(zhangsu_values)
    # 检查文本值是否按照升序排列
    sorted_values = sorted(zhangsu_values, reverse=True, key=float)
    print(sorted_values)
    if zhangsu_values == sorted_values:
        print("文本值按照降序排列")

    else:
        print("文本值未按照降序排列")
        raise AssertionError("文本值未按照降序排列")
    # TC_行业板块切换涨速升序
    poco(text="涨速").click()
    # 获取第一个 rv_sector_item 元素下的所有 bankuai_zhangfu 元素
    zhangsu_elements = first_item.offspring("com.hexin.plat.android:id/sector_sort_value")
    # 获取所有 zhangsu_values 元素的文本值，去掉百分号并转换为数字
    zhangsu_values = [element.get_text().replace('%', '') for element in zhangsu_elements]
    print(zhangsu_values)
    # 检查文本值是否按照升序排列
    sorted_values = sorted(zhangsu_values, reverse=False, key=float)
    print(sorted_values)
    if zhangsu_values == sorted_values:
        print("文本值按照升序排列")

    else:
        print("文本值未按照升序排列")
        raise AssertionError("文本值未按照升序排列")


def test_hangye_liangbi_paixu_des(poco):
    """
    TC_行业板块切换量比升序
    用例id
    1300783
    """

    poco(text="量比").wait(15).click()
    first_item = poco("com.hexin.plat.android:id/rv_sector_item")[0]

    # 获取第一个 rv_sector_item 元素下的所有 bankuai_zhangfu 元素
    zhangsu_elements = first_item.offspring("com.hexin.plat.android:id/sector_sort_value")

    # 获取所有 zhangsu_values 元素的文本值，去掉百分号并转换为数字
    zhangsu_values = [element.get_text().replace('%', '') for element in zhangsu_elements]
    print(zhangsu_values)
    # 检查文本值是否按照升序排列
    sorted_values = sorted(zhangsu_values, reverse=True, key=float)
    print(sorted_values)
    if zhangsu_values == sorted_values:
        print("文本值按照降序排列")

    else:
        print("文本值未按照降序排列")
        raise AssertionError("文本值未按照降序排列")
    # TC_行业板块切换涨速升序
    poco(text="量比").click()
    # 获取第一个 rv_sector_item 元素下的所有 bankuai_zhangfu 元素
    zhangsu_elements = first_item.offspring("com.hexin.plat.android:id/sector_sort_value")
    # 获取所有 zhangsu_values 元素的文本值，去掉百分号并转换为数字
    zhangsu_values = [element.get_text().replace('%', '') for element in zhangsu_elements]
    print(zhangsu_values)
    # 检查文本值是否按照升序排列
    sorted_values = sorted(zhangsu_values, reverse=False, key=float)
    print(sorted_values)
    if zhangsu_values == sorted_values:
        print("文本值按照升序排列")

    else:
        print("文本值未按照升序排列")
        raise AssertionError("文本值未按照升序排列")
