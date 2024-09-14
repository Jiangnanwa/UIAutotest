#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_laoshouye_slide_FPS 
   Description :
   Author : chenqiyue
   CreateDate：2023/09/20  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.android import Android

from common.function import myFindElements
from common.login import login_by_password
from common.app_operation import Slide_up_speed, Start_Performance_Test, Show_Performance_Test, stop_app_open_app
from airtest.core.api import keyevent, stop_app, clear_app, touch
from airtest.core.api import start_app

@pytest.mark.skip
def test_setup(poco):
    print("bbb`")
    Android().wake()

    # network_switch_10jqka(poco)
    clear_app("com.hexin.plat.android")
    start_app("com.hexin.plat.android",activity="LogoEmptyActivity")
    if poco(text="同意").exists():
        poco(text="同意").wait().click()
    else:
        myFindElements("同意", 4, poco)

    touch((495, 665))
    touch((508, 627))
    try:
        poco(name="com.hexin.plat.android:id/capsule_right").wait().click()
    except Exception as e:
        print(e)
    # 新手开户弹窗
    if poco(name="android.widget.Image").exists():
        poco(nameMatches="android.widget.Image")[0].click()

@pytest.mark.skip
def test_account_login(poco):
    try:

        stop_app_open_app("com.hexin.plat.android")

        login_by_password("zyyt19", "zyy123", "com.hexin.plat.android", poco)
    except Exception as e:
        print(e)
        stop_app_open_app("com.hexin.plat.android")
        login_by_password("zyyt19", "zyy123", "com.hexin.plat.android", poco)


def test_olduser_Slide_up_FPS_fast(poco):
    '''
    测试点:首页2.0推荐tab+快速滑动
    前提:
    1、登录首页2.0账号zyyt19/1登录后重启app
    详细步骤：
    1.启动APP->登录账号→杀死重启；
    2.上滑首页2.0抽屉置顶
    3.快速：600mm/s 速度向上滑动20页，观察滑动过程的FPS最低值、平均值
    '''

    start_app("com.hexin.plat.android",activity="LogoEmptyActivity")
    # 打开小白球,启动性能参数数据计算
    Start_Performance_Test(poco)
    # 根据荣耀8X的规格，其像素密度为397 PPI
    # 通常情况下，你可以在手机的规格或详细信息页面上找到其像素密度。在Android手机上，你可以前往“设置”-“显示”或“关于手机”-“规格”选项卡中查看该信息。在iOS手机上，你可以前往“设置”-“显示与亮度”-“查看”中找到。
    # Slide_up_speed(poco,397,300)
    Slide_up_speed(poco, 397, 600)
    # 进入小白球,查看数据
    Show_Performance_Test(poco)
    stop_app("com.hexin.plat.android")


def test_olduser_slide_up_FPS_Slow(poco):
    '''
    测试点:首页2.0推荐tab+正常滑动
    前提:
    1、登录首页2.0账号zyyt19/1登录后重启app
    详细步骤：
    1.启动APP->登录账号→杀死重启；
    2.上滑首页2.0抽屉置顶
    3.正常：300mm/s 速度向上滑动20页，观察滑动过程的FPS最低值、平均值
    '''

    start_app("com.hexin.plat.android",activity="LogoEmptyActivity")

    # 打开小白球,启动性能参数数据计算
    Start_Performance_Test(poco)
    # 根据荣耀8X的规格，其像素密度为397 PPI
    # 通常情况下，你可以在手机的规格或详细信息页面上找到其像素密度。在Android手机上，你可以前往“设置”-“显示”或“关于手机”-“规格”选项卡中查看该信息。在iOS手机上，你可以前往“设置”-“显示与亮度”-“查看”中找到。
    Slide_up_speed(poco, 397, 300)
    # 开始获取性能数据

    # 延时5秒钟
    # time.sleep(5)
    # Slide_up_speed(poco, 397, 300)
    # 进入小白球,查看数据
    Show_Performance_Test(poco)

    stop_app("com.hexin.plat.android")


def test_olduser_Information_Jump_Return(poco):
    '''
    测试点:首页2.0推荐tab+依次跳转内容详情返回+滑动
    前提:
    详细步骤：
    1.启动APP→登录账号→杀死重启；
    2.上滑首页2.0抽屉置顶
    3.点击第一条内容区域，跳转落地页后返回；
    4.点击第二条内容区域，跳转落地页返回；
    5.点击第三条内容区域，跳转落地页返回；
    6.上滑一页，重复3、4、5，共重复20页（或者共跳转60次落地页）
    '''

    start_app("com.hexin.plat.android",activity="LogoEmptyActivity")

    # 打开小白球,启动性能参数数据计算
    Start_Performance_Test(poco)
    # 上滑首页2.0抽屉置顶
    num = 0
    while num < 60:
        Slide_up_speed(poco, 397, 600, Repetitions=1)
        # 获取所有符合条件的元素
        elements = poco(type='android.widget.TextView', name='com.hexin.plat.android:id/feed_recommend_title_view')
        # 循环点击每个元素返回
        if not elements:
            print("当前页没有资讯可以点击")
        else:

            for element in elements:
                try:
                    element.click()
                except Exception as e:
                    print(e)
                keyevent('BACK')
                num += 1
    print(num)
    Show_Performance_Test(poco)

    stop_app("com.hexin.plat.android")

# def test_olduser_Slide_down_FPS_fast(poco):
#     '''
#     测试点:首页2.0推荐tab+快速滑动
#     前提:
#     1、登录首页2.0账号zyyt19/1登录后重启app
#     详细步骤：
#     1.启动APP->登录账号→杀死重启；
#     2.上滑首页2.0抽屉置顶
#     3.快速：600mm/s 速度向下滑动20页，观察滑动过程的FPS最低值、平均值
#     '''
#     start_app("com.hexin.plat.android",activity="LogoEmptyActivity")
#     # 打开小白球,启动性能参数数据计算
#     Start_Performance_Test(poco)
#     # 根据荣耀8X的规格，其像素密度为397 PPI
#     # 通常情况下，你可以在手机的规格或详细信息页面上找到其像素密度。在Android手机上，你可以前往“设置”-“显示”或“关于手机”-“规格”选项卡中查看该信息。在iOS手机上，你可以前往“设置”-“显示与亮度”-“查看”中找到。
#     # Slide_up_speed(poco,397,300)
#     Slide_down_speed(poco, 397, 600)
#     # 进入小白球,查看数据
#     Show_Performance_Test(poco)
#     stop_app("com.hexin.plat.android")
# def test_olduser_slide_down_FPS_Slow(poco):
#     '''
#     测试点:首页2.0推荐tab+正常滑动
#     前提:
#     1、登录首页2.0账号zyyt19/1登录后重启app
#     详细步骤：
#     1.启动APP->登录账号→杀死重启；
#     2.上滑首页2.0抽屉置顶
#     3.正常：300mm/s 速度向下滑动20页，观察滑动过程的FPS最低值、平均值
#     '''
#
#
#     start_app("com.hexin.plat.android",activity="LogoEmptyActivity")
#
#     # 打开小白球,启动性能参数数据计算
#     Start_Performance_Test(poco)
#     # 根据荣耀8X的规格，其像素密度为397 PPI
#     # 通常情况下，你可以在手机的规格或详细信息页面上找到其像素密度。在Android手机上，你可以前往“设置”-“显示”或“关于手机”-“规格”选项卡中查看该信息。在iOS手机上，你可以前往“设置”-“显示与亮度”-“查看”中找到。
#     Slide_up_speed(poco, 397, 300)
#     # 开始获取性能数据
#
#     # 延时5秒钟
#     # time.sleep(5)
#     # Slide_down_speed()(poco, 397, 300)
#     # 进入小白球,查看数据
#     Show_Performance_Test(poco)
#
#     stop_app("com.hexin.plat.android")
# #
# def test_tongshunshangcheng_slide_FPS_Slow(poco):
#     '''
#     同顺商城-模拟用户正常滑动，滑动至底，观察滑动过程的FPS最低值、平均值
#     正常速度：300mm/s
#
#
#     '''
#     from page.HomePage import HomePage
#     start_app("com.hexin.plat.android",activity="LogoEmptyActivity")
#
#     # 打开小白球,启动性能参数数据计算-回到首页
#     Start_Performance_Test(poco)
#     # 进入同顺商城
#     HomePage.ths_shopping.click()
#     # 根据荣耀8X的规格，其像素密度为397 PPI
#     # 通常情况下，你可以在手机的规格或详细信息页面上找到其像素密度。在Android手机上，你可以前往“设置”-“显示”或“关于手机”-“规格”选项卡中查看该信息。在iOS手机上，你可以前往“设置”-“显示与亮度”-“查看”中找到。
#     # Slide_up_speed(poco,397,300)
#     Slide_up_speed(poco, 397, 300)
#     # 进入小白球,查看数据
#     # 返回首页
#     keyevent('BACK')
#     Show_Performance_Test(poco)
#     stop_app("com.hexin.plat.android")
#

# def test_tongshunshangcheng_slide_FPS_fast(poco):
#     '''
#     同顺商城-模拟用户正常滑动，滑动至底，观察滑动过程的FPS最低值、平均值
#
#     快速：600mm/s
#
#     '''
#     from page.HomePage import HomePage
#     start_app("com.hexin.plat.android",activity="LogoEmptyActivity")
#
#     # 打开小白球,启动性能参数数据计算-回到首页
#     Start_Performance_Test(poco)
#     # 进入同顺商城
#     HomePage.ths_shopping.click()
#     # 根据荣耀8X的规格，其像素密度为397 PPI
#     # 通常情况下，你可以在手机的规格或详细信息页面上找到其像素密度。在Android手机上，你可以前往“设置”-“显示”或“关于手机”-“规格”选项卡中查看该信息。在iOS手机上，你可以前往“设置”-“显示与亮度”-“查看”中找到。
#     # Slide_up_speed(poco,397,300)
#     Slide_up_speed(poco, 397, 600)
#     # 进入小白球,查看数据
#     # 返回首页
#     keyevent('BACK')
#     Show_Performance_Test(poco)
#     stop_app("com.hexin.plat.android")
