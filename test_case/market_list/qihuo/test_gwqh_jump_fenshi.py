#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_gwqh_jump_fenshi 
   Description :
   Author : chenqiyue
   CreateDate：2024/01/11  用例id:
-------------------------------------------------
"""
import time


def test_gwqh_jump_fenshi(poco):
    """
    用例id    用例名称
    1300912  TC_全部板块_排序状态列表滑动
    操作步骤:
    """
    poco(text="纽约金主连").click()
    # 获取 "com.hexin.plat.android:id/fenshi_headline_view" 元素
    fenshi_headline_view = poco("com.hexin.plat.android:id/fenshi_headline_view")
    # 获取初始的 desc 属性值
    initial_desc = fenshi_headline_view.attr("desc")
    print(initial_desc)
    # 等待1分钟
    wait_time = 60
    start_time = time.time()
    while time.time() - start_time < wait_time:
        # 等待一小段时间，比如1秒
        time.sleep(1)

        # 再次获取 desc 属性值
        current_desc = poco("com.hexin.plat.android:id/fenshi_headline_view").attr("desc")
        print(current_desc)

        # 检查是否发生变化
        if current_desc != initial_desc:
            print(f"Desc attribute has changed. Exiting wait loop.{current_desc}{initial_desc}")
            break
    else:
        # 如果等待1分钟后还未发生变化，则报错
        raise TimeoutError("Error: Desc attribute has not changed within 1 minute.")