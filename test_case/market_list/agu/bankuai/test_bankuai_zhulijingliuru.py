#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_zhulijingliuru 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/06  用例id:


-------------------------------------------------
"""

from airtest.core.api import sleep
from airtest.core.assertions import assert_exists
from airtest.core.cv import Template


def test_01_zhulijingliuru_hangyeqiehuan(poco):
    """
     主力净流入-行业切换 用例id:1300759
    """
    poco("android.widget.HorizontalScrollView").swipe([-0.8464, 0.008])
    sleep(2.0)
    # "报错,复现路径:主力净流入-行业切换-主力净流入-在行业主力净流入页面向左滑动"
    # 概念主力净流入(亿)
    text_bankuai_title = poco("com.hexin.plat.android:id/text_bankuai_title").get_text()
    print(text_bankuai_title)
    if not "概念主力净流入(亿)" in text_bankuai_title:
        raise AssertionError("概念主力净流入(亿)不存在,操作路径:主力净流入-行业切换-主力净流入-在行业主力净流入页面向左滑动")
    # 操作路径:主力净流入-行业切换-主力净流入-在行业主力净流入页面向左滑动"
    if not poco("com.hexin.plat.android:id/rightmore").exists():
        raise AssertionError("更多按钮不存在")
    poco("android.widget.HorizontalScrollView").swipe([-0.8464, 0.008])

    text_bankuai_title = poco("com.hexin.plat.android:id/text_bankuai_title").get_text()
    print(text_bankuai_title)
    if not "地域主力净流入(亿)" in text_bankuai_title:
        raise AssertionError("地域主力净流入(亿)标题不存在,复现路径:主力净流入-行业切换-主力净流入-在行业主力净流入页面向左滑动")

    # if not poco(textMatches=".*地域主力净流入(亿)|地域主力净流入(亿)").exists():
    #     raise AssertionError(".*地域主力净流入(亿)标题不存在,复现路径:主力净流入-行业切换-主力净流入-在行业主力净流入页面向左滑动")
    # if not poco(text="港资流向板块详情").exists():
    #     raise AssertionError("港资流向板块详情不存在")
    # 操作路径:主力净流入-行业切换-主力净流入-在行业主力净流入页面向左滑动"
    if not poco("com.hexin.plat.android:id/rightmore").exists():
        raise AssertionError("更多按钮不存在")


def test_02_zhulijingliuru_jump(poco):
    """
     点击表头最右端“更多 >”
     用例id:1300772
    """

    # poco("android.widget.HorizontalScrollView").swipe([-0.8464, 0.008])
    sleep(1.0)
    poco("com.hexin.plat.android:id/rightmore").click()
    if not poco(text="大盘主力净流入").exists():
        # 跳转至看资金页面自动滑动至列表，且仅选中板块列表中的地域板块。
        if poco(text="地域板块").sibling("com.hexin.plat.android:id/bankuai_item_select_icon").exists():
            print("跳转至看资金页面自动滑动至列表，且仅选中板块列表中的地域板块")
            raise AssertionError("地域板块点击更多-地域板块 被选中,预期只选中行业")
        # 检查概念板块的兄弟节点是否不存在指定元素
        if poco(text="概念板块").sibling("com.hexin.plat.android:id/bankuai_item_select_icon").exists():
            raise AssertionError("概念板块也同时被选中概念,预期只选中行业")

        # 检查行业板块的兄弟节点是否不存在指定元素
        if not poco(text="行业板块").sibling("com.hexin.plat.android:id/bankuai_item_select_icon").exists():
            print("行业板块也同时被选中,预期只选中地域")
            raise AssertionError("行业板块没有被选中")
    else:
        ele = [poco(text="大盘主力净流入"), poco(text="两市成交金额"), poco(text="个股资金"), poco(text="板块资金")]
        for i in ele:
            if not i.exists():
                raise AssertionError(f"{i.get_text()}页面元素缺失")
        assert poco(text="板块资金").attr('selected') == True, "板块资金未被选中"
        # assert_exists(Template(r"tpl1722513576747.png", record_pos=(-0.009, 0.258), resolution=(1080, 2400)), "筛选项存在校验")
        dapanzijin_shuju = poco(text="大盘主力净流入").sibling(textMatches=".*亿")
        assert dapanzijin_shuju, "大盘主力净流入数据为空"
        liangshichengjiaoe_shuju = poco(text="两市成交金额").sibling(textMatches=".*亿")
        assert liangshichengjiaoe_shuju, "两市成交金额数据为空"
