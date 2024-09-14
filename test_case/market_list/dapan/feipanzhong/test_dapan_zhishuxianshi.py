#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapan_zhishuxianshi
   Description：  TC_大盘指数模块显示
   Author：       duanxufei
   CreateDate：   2024/3/12 13:39
   CaseID：       1752972
-------------------------------------------------
"""
from airtest.core.api import swipe


def test_chakanweizhi(poco):
    """
    查看大盘指数模块在大盘tab的位置
    """
    poco("行情").click()

    # 通过父级元素获取子元素，和子元素是否可见判断是否在顶部展示
    target_name = poco("com.hexin.plat.android:id/vertical_container").child()[0].get_name()
    target_element = poco("com.hexin.plat.android:id/marketv2_component_hs_index_layout")

    assert "com.hexin.plat.android:id/marketv2_component_hs_index_layout" == target_name \
           and target_element.attr("visible")


def test_dapanzhishuzhanshi(poco):
    """
    查看大盘指数模块显示
    """
    mokuai_list = poco("com.hexin.plat.android:id/gz_index_container").children()
    for item in range(len(mokuai_list)-1):
        # 获取指数对应名称、现价、指数涨跌、指数涨跌幅
        zhishu_text = mokuai_list[item].offspring("com.hexin.plat.android:id/index_name").get_text()
        xianjia_text = mokuai_list[item].offspring("com.hexin.plat.android:id/index_price").get_text()
        zhangdie_text = mokuai_list[item].offspring("com.hexin.plat.android:id/index_rise_price").get_text()
        zhangfu_text = mokuai_list[item].offspring("com.hexin.plat.android:id/index_rise_percent").get_text()

        assert zhishu_text and xianjia_text and zhangdie_text and zhangfu_text


def test_chakanzuihou(poco):
    """
    在大盘指数模块上左滑至指数模块最右侧，查看指数模块最后一个模块显示
    """
    mokuai_list = poco("com.hexin.plat.android:id/gz_index_container").children()
    diff_X = - mokuai_list[-2].get_position()[0] - mokuai_list[0].get_position()[0]
    # 向左滑动列表直到定制模块显示
    while not poco("com.hexin.plat.android:id/index_edit_text").exists():
        mokuai_list[-2].swipe([diff_X, 0])

    assert "定制" == poco("com.hexin.plat.android:id/index_edit_text").get_text()
