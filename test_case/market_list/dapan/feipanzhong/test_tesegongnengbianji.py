#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_tesegongnengbianji
   Description：  TC_特色功能页面编辑页   需要使用debug包
   Author：       duanxufei
   CreateDate：   2024/3/13 14:52
   CaseID：       1752995
-------------------------------------------------
"""

import pytest


@pytest.mark.skip(reason="服务器未调试通过")
def test_jinrubianji(poco):
    """
    大前提
        1.选择行情-大盘tab
        2.滑动至特色功能宫格的最后一个
        3.点击定制按钮
        TODO 需要登陆账号
    """
    # poco("行情").click()
    swipe_num = 0
    while not poco(text="定制").exists():
        if swipe_num > 10:
            break
        poco("applications").offspring("android.widget.ListView").children()[-2].swipe([-0.5, 0])
        swipe_num += 1
    poco(text="定制").click()

@pytest.mark.skip(reason="服务器未调试通过")
def test_daohanglan(poco):
    """
    导航栏展示
    """
    daohanglan_item_list = poco("app").child("android.view.View")[0].children()
    quxiao_button = daohanglan_item_list[0]
    title = daohanglan_item_list[2]  # TODO dom树中元素是有顺序的但是实际查询返回被重新排序，具体原因待查
    wancheng_button = daohanglan_item_list[1]

    assert "取消" == quxiao_button.get_text()
    assert "功能定制" == title.get_text()
    assert "完成" == wancheng_button.get_text()

@pytest.mark.skip(reason="服务器未调试通过")
def test_chakanzhanshi(poco):
    """
    宫格展示
        查看所有的宫格名称（共14个）
    """
    target_name_list = ["选股", "打新日历", "ETF基金", "同花顺热榜", "大盘回顾", "北交所", "集合竞价", "涨停聚焦", "沪深港通", "龙虎榜", "数据中心", "研报",
                        "融资融券", "业绩预告"]
    gongneng_list = poco("app").child("android.view.View")[3].children()

    # TODO dom树中元素是有顺序的但是实际查询返回结果被重新排序，具体原因待查
    # for index in range(len(target_name_list)):
    #     # assert target_name_list[index] == gongneng_list[index*2].get_text()
    #     print(target_name_list[index] == gongneng_list[index*2].get_text())
    text_num = 0
    for index in range(len(gongneng_list)):
        if gongneng_list[index].get_text():
            assert target_name_list[text_num] == gongneng_list[index].get_text()
            text_num += 1

@pytest.mark.skip(reason="服务器未调试通过")
def test_dianjiquxiao(poco):
    """
    交互-点击取消
        点击导航栏的取消按钮
    """
    quxiao_button = poco("app").child("android.view.View")[0].children()[0]
    quxiao_button.click()
    assert poco("applications").exists()

@pytest.mark.skip(reason="服务器未调试通过")
def test_paixu(poco):
    """
    交互-拖动排序
    """
    # poco(text="定制").click()

    name_list = []
    huakuai_list = []
    temp_list = []

    gongneng_list = poco("app").child("android.view.View")[-1].children()
    for index in range(len(gongneng_list)):
        # assert target_name_list[index] == gongneng_list[index*2].get_text()
        # print(target_name_list[index] == gongneng_list[index*2].get_text())
        print(f"{index}:{gongneng_list[index].get_text()}")
        tmp_text = gongneng_list[index].get_text()
        if tmp_text:
            name_list.append(tmp_text)
        else:
            huakuai_list.append(gongneng_list[index])
    # 将列表最后两个功能调换位置
    huakuai_list[-1].drag_to(huakuai_list[-2])
    # 处理功能名称数组
    tmp_name = name_list[-2]
    del name_list[-2]
    name_list.append(tmp_name)
    # 点击完成按钮保存结果
    # poco("app").child("android.view.View")[0].children()[1].click()
    poco(text="完成").click()

    assert poco("app").exists()
    applist = poco("applications").offspring("android.widget.ListView").children()
    daoyi_app_text = applist[-2].child("android.widget.TextView")[1].get_text()
    daoer_app_text = applist[-3].child("android.widget.TextView")[1].get_text()
    assert daoyi_app_text == name_list[-1] and daoer_app_text == name_list[-2]
