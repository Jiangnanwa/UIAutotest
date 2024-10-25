#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：conftest.py
   Description :
   Author : chenqiyue
   CreateDate：2023/04/03
   用例id:
------------------------------------------------
"""
import pytest
from airtest.core.android import Android
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException

from common.app_operation import stop_app_open_app, back_findelement
from common.function import myFindElements, homePageFindElements
from poco.exceptions import PocoNoSuchNodeException
from airtest.core.api import touch, sleep
from common.login import login_by_password



@pytest.fixture(scope="module", autouse=True)
def test_setup(poco):
    print("手机连接成功,进行初始化准备`")
    # 获取当前文件所在目录的路径
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 获取当前目录的上一级目录的路径
    parent_dir = os.path.dirname(current_dir)

    # 获取上一级目录下的image文件夹的路径
    image_dir = os.path.join(parent_dir, 'image')

    # 添加image文件夹路径到G.BASEDIR
    G.BASEDIR.append(image_dir)
    device().wake()  # 唤醒屏幕
    clear_app("com.hexin.plat.android")
    start_app("com.hexin.plat.android", activity="LogoEmptyActivity")
    sleep(10.0)

    # 点击同意按钮
    # agree_button = myFindElements("同意", 4, poco)
    # if agree_button.exists():
    #     agree_button.click()
    # sleep(2.0)
    #
    # 再次检查同意按钮是否存在，存在则点击
    if poco(text="同意").exists():
        print("点击同意")
        poco(text="同意").click()
    else:
        print("寻找点击同意")
        myFindElements("同意", 4, poco)
    sleep(10.0)
    if poco("com.hexin.plat.android:id/btn_close").exists():
        poco("com.hexin.plat.android:id/btn_close").click()
    # 尝试定位元素 "没有炒过股"
    try:
        element = poco(text="没有炒过股")
        if not element.exists():
            print("点击没有炒过股")
            touch((495, 665))  # 坐标定位
        else:
            element.click()
    except PocoNoSuchNodeException:
        touch((495, 665))  # 坐标定位

        # 尝试定位元素 "股票直接上手"
        # try:
        element = poco(text="股票直接上手")
        if not element.exists():
            print("点击股票直接上手")
            touch((508, 627))  # 坐标定位
        else:
            element.click()
    except PocoNoSuchNodeException:
        touch((508, 627))  # 坐标定位

    if poco(text="直接开户服务").exists():
        poco(text="直接开户服务").click()

    # 点击右上角按钮
    try:
        poco(name="com.hexin.plat.android:id/capsule_right").wait(2).click()
    except Exception as e:
        print(e)
    if poco("com.hexin.plat.android:id/close_button").exists():
        poco("com.hexin.plat.android:id/close_button").click()
    # 处理新手开户弹窗
    try:
        if poco(name="android.widget.Image").exists():
            poco(nameMatches="android.widget.Image")[0].click()

    except PocoNoSuchNodeException:
        print("新手弹窗点击失败")
    # stop_app_open_app("com.hexin.plat.android")
    # image_template = Template(r"tpl1720858284488.png")
    # try:
    # # 查找图像并点击
    #     if exists(image_template):
    #         touch(Template(r"tpl1720858284488.png"))
    #         sleep(5)
    #         touch(Template(r"tpl1720858297840.png"))
    #         sleep(5)
    #         touch(Template(r"tpl1720862719944.png", record_pos=(-0.002, 0.891), resolution=(1176, 2400)))
    # except Exception as e:
    #     print(e)
    #     print("引导点击错误重启app")
    #     stop_app_open_app("com.hexin.plat.android")
    if poco(text="直接开户服务").exists():
        poco(text="直接开户服务").click()

    # 点击右上角按钮
    try:
        poco(name="com.hexin.plat.android:id/capsule_right").wait(2).click()
    except Exception as e:
        print(e)
    if poco("com.hexin.plat.android:id/close_button").exists():
        poco("com.hexin.plat.android:id/close_button").click()
    # 处理新手开户弹窗
    try:
        if poco(name="android.widget.Image").exists():
            poco(nameMatches="android.widget.Image")[0].click()

    except PocoNoSuchNodeException:
        print("新手弹窗点击失败")
    stop_app_open_app("com.hexin.plat.android")
    sleep(5.0)
    close_button = poco("com.hexin.plat.android:id/close_button")
    if close_button.exists():
        close_button.click()
    # image_template = Template(r"tpl1720858284488.png")
    # if exists(image_template):
    #     print("存在下一步弹窗，重启APP")
    #     stop_app_open_app("com.hexin.plat.android")
    #     sleep(5.0)
    #     print("等待3s结束")
    #     close_button = poco("com.hexin.plat.android:id/close_button")
    #     if close_button.exists():
    #         close_button.click()
        # hangqing = poco(text="行情", name="com.hexin.plat.android:id/title")
        # homePageFindElements(hangqing, 2, poco)
        # if not hangqing.exists():
        #     back_findelement(hangqing)


@pytest.fixture(scope="module", autouse=True)
def test_loginin(poco):
    login_by_password('slf1994', 'sns654321', 'com.hexin.plat.android', poco)