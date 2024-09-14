#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_tesegongneng
   Description：  TC_特色功能    需要使用debug包
   Author：       duanxufei
   CreateDate：   2024/3/13 14:14
   CaseID：       1753054
-------------------------------------------------
"""
from airtest.core.api import keyevent


def test_chakan(poco):
    """
    查看特色功能模块的展示
    """
    poco("行情").click()

    # 断言特色功能模块存在且模块个数大于等于5个
    assert poco("applications").exists() \
           and len(poco("applications").offspring("android.widget.ListView").children()) >= 5


def test_huadong(poco):
    """
    滑动特色功能模块
        手指向左、向右滑动
    """
    app_list = poco("applications").offspring("android.widget.ListView").children()
    swipe_num = 0
    while not poco(text="定制").exists():
        if swipe_num > 10:
            break
        # app_list[-2].swipe([-0.3, 0])
        # 因屏幕存在差异，所以换成倒数第二个元素拖拽到第一个元素的位置上
        app_list[-2].drag_to(app_list[0])
        swipe_num += 1
        # 刷新dom树
        app_list = poco("applications").offspring("android.widget.ListView").children()


def test_dianjigongge(poco):
    """
    点击宫格
        点击具体的宫格
    """
    app_list = poco("applications").offspring("android.widget.ListView").children()
    app_list[-2].click()

    keyevent("BACK")


def test_dianjidingzhi(poco):
    """
    点击功能管理
    """
    # TODO 需要登陆账号
    poco(text="定制").click()
    keyevent("BACK")

