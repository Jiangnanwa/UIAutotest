#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapanyidong_jump 
   Description :
   Author : chenqiyue
   CreateDate：2024/03/08  用例id:
-------------------------------------------------
"""


def test_dapanyidong_jump(poco):
    """
    用例名称
    TC_大盘控件_展开状态大盘异动跳转
    用例id
    1238644
    """
    not_element=[]
    poco(nameMatches = "com.hexin.plat.android:id/dpyd_text|com.hexin.plat.android:id/dpyd_image").click()
    elements_list = [ poco("com.hexin.plat.android:id/tv_yd_recorder"), poco(text="上证指数"),poco("com.hexin.plat.android:id/tv_date")]
    for element in elements_list:
        if not element.exists():
            not_element.append(element.get_text())
        else:
            print(f"元素没有缺失{element}")
    if not_element !="":
        assert  AssertionError(f"大盘异动跳转元素内容缺失{not_element}")


    poco("com.hexin.plat.android:id/backButton").click()
