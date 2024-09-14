#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    sorting_type_operations
   Description :
   Author : chenqiyue
   CreateDate：2023/12/09  用例id:
-------------------------------------------------
"""


def sort_elements_by_percentage(elements_with_name, sorting_type="asc"):
    """
    实现功能:一组含有%的数据,遍历每一个数据去掉%,进行升降序排列
    """
    # 获取这些元素的text值存入数组
    split_values = []
    for element in elements_with_name:
        split_name = element.get_text()
        print(split_name)
        split_values.append(split_name)

    # 将获取的数据按照字符串排序将%剔除进行排序
    if sorting_type == "asc":
        sorted_values = sorted(split_values, key=lambda x: float(x.rstrip('%')))
    elif sorting_type == "desc":
        sorted_values = sorted(split_values, key=lambda x: float(x.rstrip('%')), reverse=True)
    print(sorted_values)

    # 校验获取的数据是否是排序
    if split_values == sorted_values:
        print("split_values", split_values)
        print("sorted_values", sorted_values)
    else:
        print("split_values", split_values)
        print("split_values", sorted_values)
        raise AssertionError("获取的数据排序错误")


def sort_elements_by_criteria(item, sort, elements_with_name):
    """
    Sorts elements based on given criteria (asc/desc).

    Args:
    - poco: Poco instance
    - item: Tuple containing element information
    - sort: Sorting criteria (asc/desc)
    """
    """
       根据给定的条件（asc/desc）对元素进行排序。
       适用于表头数据获取到的时候是#分割的字符串,此方法实现1.将字符串按照#分割后放入数组,根据数据字典封装的 item[1]是表头是数组中的第几个,
       将想要排序的表头提取出来并处理(带%\带中文单位\小数\整数),处理后存入数组,进行sort排序
       Args:
       - poco: Poco实例
       - item: 包含元素信息的元组
       - sort: 排序条件（asc/desc）
   """
    split_values = []

    # 遍历具有name属性的元素并处理元素名称
    for element in elements_with_name:
        # 获取元素名称
        name = element.get_name()
        # 使用#符号分割元素名称
        split_name = name.split('#')
        # 获取特定位置的数据
        biaotou_data = split_name[item[1]]

        # 如果名称包含#符号
        if len(split_name) > 1:
            # 如果包含百分比符号
            if '%' in biaotou_data:
                zhangdefu_values = biaotou_data.replace('%', '')
            # 如果包含“万”
            elif '万' in biaotou_data:
                zhangdefu_values = float(biaotou_data.replace('万', '')) * 10000
            # 如果包含“亿”
            elif '亿' in split_name[item[1]]:
                zhangdefu_values = float(biaotou_data.replace('亿', '')) * 100000000
            else:
                zhangdefu_values = biaotou_data
            # 将处理后的数据添加到数组中
            split_values.append(zhangdefu_values)
    is_integer = all(isinstance(val, int) for val in split_values)
    if sort == "desc":
        if is_integer:
            sorted_values = sorted(split_values, reverse=True)
            print(item[0], "表头排序,数据都是整数")
        else:
            sorted_values = sorted(split_values, reverse=True, key=float)
            print(item[0], "表头", sort, "排序,数据都是小数,排序key=float")
    elif sort == "asc":
        if is_integer:
            sorted_values = sorted(split_values)
            print(item[0], "表头", sort, "排序,数据都是整数")
        else:
            sorted_values = sorted(split_values, key=float)
            print(item[0], "表头", sort, "排序,数据都是小数,排序key=float")
    else:
        raise ValueError("Invalid sorting criteria. Use 'asc' or 'desc'.")
    if split_values == sorted_values:
        print("手炒", item[0], "表头", sort, "排序后的值:", split_values)
        print("sort方法", item[0], "表头", sort, "排序后的值:", sorted_values)
    else:
        print("手炒", item[0], "表头", sort, "排序后的值:", split_values)
        print("sort方法", item[0], "表头", sort, "排序后的值:", sorted_values)
        raise AssertionError(f"获取的数据 {item[0]} 表头 {sort} 排序错误")


def process_element_names(elements_with_name, num):
    split_values = []
    i = 0
    # 遍历具有name属性的元素并处理元素名称
    for element in elements_with_name:
        if i == 3:
            break
        else:
            # 获取元素名称
            name = element.get_name()
            # 使用#符号分割元素名称
            split_name = name.split('#')
            # 获取特定位置的数据,将板块名称存入数组
            bk_name_data = split_name[num]
            split_values.append(bk_name_data)
            i = i + 1
    return split_values
