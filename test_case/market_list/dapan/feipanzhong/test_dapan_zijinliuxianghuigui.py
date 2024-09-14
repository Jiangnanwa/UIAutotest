#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapan_zijinliuxianghuigui
   Description：  TC_资金流向回归
   Author：       duanxufei
   CreateDate：   2024/3/14 10:51
   CaseID：       1754809
-------------------------------------------------
"""
import time

from airtest.core.api import keyevent

import pytest


@pytest.mark.skip(reason="服务器未调试通过")
def test_shouqi(poco):
    """
    收起/展开-收起
        点击收起
    """
    while not (poco("capital_flows").exists()
               and poco("capital_flows").children()
               and poco("capital_flows").offspring(name="chart").exists()
               and poco("capital_flows").offspring(name="chart").get_bounds()[2] < 1):
        if poco(text="意见反馈").exists():
            raise Exception("资金流动不存在")
        tmp_ele = poco("lazy_scroll").children()[1]
        tmp_ele.swipe([0, -tmp_ele.get_size()[1]], duration=1)

    button_list = poco("capital_flows").child("android.view.View")[0].child("android.widget.TextView")
    tmp_list = sorted(list(button_list), key=lambda v: (v.get_bounds()[1]))
    shouqi_zhankai_button = tmp_list[1]
    shouqi_zhankai_button.click()
    shouqi_zhankai_button.refresh()
    assert "展开" == shouqi_zhankai_button.get_text()
    # TODO 图表收起的断言？
    # assert not poco("capital_flows").offspring(name="chart").exists()

@pytest.mark.skip(reason="服务器未调试通过")
def test_zhankai(poco):
    """
    收起/展开-展开
        点击展开
    """
    button_list = poco("capital_flows").child("android.view.View")[0].child("android.widget.TextView")
    tmp_list = sorted(list(button_list), key=lambda v: (v.get_bounds()[1]))
    shouqi_zhankai_button = tmp_list[1]
    shouqi_zhankai_button.click()
    shouqi_zhankai_button.refresh()
    assert "收起" == shouqi_zhankai_button.get_text()

    # TODO 图表收起的断言？
    # assert not poco("capital_flows").offspring(name="chart").exists()

@pytest.mark.skip(reason="服务器未调试通过")
def test_gengduo(poco):
    """
    点击更多
    """
    poco("capital_flows").child("android.widget.TextView").click()

    assert "资金流向" == \
           poco("app").child("android.view.View")[0].child("android.view.View").child("android.widget.TextView")[
               1].get_text()

@pytest.mark.skip(reason="服务器未调试通过")
def test_fanhui(poco):
    """
    跳转资金流向落地页-标题栏
        1.查看标题栏展示
        2.点击<
    """
    poco("app").child("android.view.View")[0].child("android.view.View").child("android.widget.TextView")[0].click()
    assert poco("capital_flows").exists()

@pytest.mark.skip(reason="服务器未调试通过")
def test_bianji(poco):
    """
    资金流向落地也-编辑
    """
    poco("capital_flows").child("android.widget.TextView").click()
    poco(text="编辑").click()
    tmp_list = poco("app").child("android.widget.TextView")
    # 点击列表第一个
    tmp_list[3].click()
    # 再次点击列表第一个
    tmp_list[3].click()
    assert "最多添加三个图表~" == poco("app").sibling("android.view.View").child("android.widget.TextView").get_text()

    # 获取当前已选择的图表列表
    yixuanze_item_list = poco("app").child("android.view.View")
    yixuanze_name_list = []
    for index in range(1, len(yixuanze_item_list)):
        yixuanze_name_list.append(yixuanze_item_list[index].child("android.widget.TextView")[1].get_text())
    poco(text="完成").click()
    # 点击返回
    poco("app").child("android.view.View")[0].child("android.view.View").child("android.widget.TextView")[0].click()

    # 获取实际展示的图表tab
    tab_list = poco("capital_flows").offspring("tab_capital_flows").offspring("android.widget.TextView")
    for index in range(len(yixuanze_name_list)):
        assert yixuanze_name_list[index] == tab_list[index].get_text()

@pytest.mark.skip(reason="服务器未调试通过")
def test_beixianggengduo(poco):
    """
    点击跳转资金流向落地页-北向资金-查看更多数据>
    """
    poco("capital_flows").child("android.widget.TextView").click()
    tmp_list = poco("app").child("android.widget.TextView")
    tmp_list[1].click()
    assert "沪深港通" == poco("com.hexin.plat.android:id/title_bar_middle").get_text()
    keyevent("BACK")
    keyevent("BACK")

@pytest.mark.skip(reason="服务器未调试通过")
def test_dapanzijingengduo(poco):
    """
    点击跳转资金流向落地页-大盘资金-查看更多数据>
    """
    poco("capital_flows").child("android.widget.TextView").click()
    textview_list = poco("app").child("android.widget.TextView")
    tmp_list = sorted(list(textview_list), key=lambda v: (v.get_bounds()[0], v.get_bounds()[1]))
    tmp_list[3].click()
    assert "看资金" == poco("com.hexin.plat.android:id/title_bar_middle").get_text()
    keyevent("BACK")
    keyevent("BACK")

@pytest.mark.skip(reason="服务器未调试通过")
def test_rongzirongquangengduo(poco):
    """
    点击跳转资金流向落地页-融资融券-查看更多数据>
    """
    poco("capital_flows").child("android.widget.TextView").click()
    textview_list = poco("app").child("android.widget.TextView")
    tmp_list = sorted(list(textview_list), key=lambda v: (v.get_bounds()[0], v.get_bounds()[1]))

    tmp_list[3].swipe([0, -0.5])
    # 这里使用textview_list.refresh()不生效
    tmp_list = sorted(list(poco("app").child("android.widget.TextView")),
                      key=lambda v: (v.get_bounds()[0], v.get_bounds()[1]))
    tmp_list[3].click()
    assert "融资融券" == poco("com.hexin.plat.android:id/title_bar_middle").get_text()
    keyevent("BACK")
    keyevent("BACK")
