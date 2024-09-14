#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    element_utils 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/09  用例id:
-------------------------------------------------
"""
def get_nth_tv_item(poco, parent_name, descendant_name, count):
    # 获取 content_scrollview 元素
    content_scrollview = poco(parent_name)

    # 获取 content_scrollview 元素下所有的子孙节点
    all_descendants = content_scrollview.offspring()

    # 遍历所有子孙节点，找到符合条件的节点
    found_count = 0
    nth_tv_item = None

    for descendant in all_descendants:
        # 检查是否符合条件
        if descendant.get_name() == descendant_name:
            found_count += 1
            if found_count == count:
                nth_tv_item = descendant
                break

    return nth_tv_item