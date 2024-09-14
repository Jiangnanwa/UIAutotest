#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    login 
   Description :
   Author : chenqiyue
   CreateDate：2023/03/11  用例id:
-------------------------------------------------
"""
from airtest.core.api import *

from common.app_operation import back_findelement
from common.function import homePageFindElements


def vip_login(passname, pwd, appPackage, poco):
    from time import sleep
    from common.app_operation import stop_app_open_app
    print("start...")
    if poco("com.hexin.plat.android:id/vip_logo"):
        print("vip帐号已经登录")
    else:
        sleep(2.0)
        poco("com.hexin.plat.android:id/head_img").click()
        poco("com.hexin.plat.android:id/personalLoginByMoreIcon").click()
        poco("com.hexin.plat.android:id/account_img").click()
        if poco("com.android.permissioncontroller:id/permission_allow_button").exists():
            poco("com.android.permissioncontroller:id/permission_allow_button").click()

        poco("com.hexin.plat.android:id/user_account").click()
        if poco("com.hexin.plat.android:id/clear_account"):
            poco("com.hexin.plat.android:id/clear_account").click()
        else:
            print("用户名输入框全部删除按钮不存在")
        poco("com.hexin.plat.android:id/user_account").set_text(passname)
        poco("com.hexin.plat.android:id/password_input").click()
        poco("com.hexin.plat.android:id/password_input").set_text(pwd)
        poco("com.hexin.plat.android:id/login_text").click()
        poco("com.hexin.plat.android:id/confirm").click()
        if poco("com.hexin.plat.android:id/cancel_btn").exists():
            poco("com.hexin.plat.android:id/cancel_btn").click()
        else:
            print("取消按钮不存在")
        poco("com.hexin.plat.android:id/iv_personal_back").wait_for_appearance(timeout=20)
        poco("com.hexin.plat.android:id/iv_personal_back").click()
        if poco("com.hexin.plat.android:id/tv_skip").exists():
            poco("com.hexin.plat.android:id/tv_skip").click()
        else:
            print("跳过按钮不存在")
        stop_app_open_app(appPackage)


def login_by_password(passname, pwd, appPackage, poco):
    from time import sleep
    from common.app_operation import stop_app_open_app
    from airtest.core.api import keyevent
    from common.function import homePageFindElements
    # 点击左上角头像进入个人中心
    keyevent("BACK")
    homePageFindElements(poco("com.hexin.plat.android:id/head_img"), 1, poco).click()
    # 处理个人中心广告
    # sleep(3)
    # poco("com.hexin.plat.android:id/personalLoginByPhoneIcon").click()
    sleep(3)
    if poco(textMatches="images-.*").exists():
        poco(textMatches="images-.*").click()
    if not poco(textMatches="登录账号 体验更多服务|已购服务").exists():
        keyevent("BACK")
    if poco(text="手机验证码登录").exists or poco("com.android.permissioncontroller:id/permission_allow_button").exists():
        print("个人中心无广告")
    else:
        stop_app_open_app(appPackage)
        poco("com.hexin.plat.android:id/head_img").wait_for_appearance(30)
        poco("com.hexin.plat.android:id/head_img").click()
        poco("com.hexin.plat.android:id/personalLoginByPhoneIcon").wait_for_appearance(30)
        poco("com.hexin.plat.android:id/personalLoginByPhoneIcon").click()
    # 首次登录允许同花顺获取设备信息（华为mate40 鸿蒙3.0）,点击头像进入后如果有"登录帐号体验更多服务的文案就是未登录状态"
    if poco("com.hexin.plat.android:id/pagePersonalTopLoginText").exists():
        print("当前未登录帐号")
    else:
        # 如果是已经登录的状态,需要退出帐号
        sleep(3)
        if  poco("com.hexin.plat.android:id/iv_personal_setting").exists():
            poco("com.hexin.plat.android:id/iv_personal_setting").click()
        else:
            touch(Template(r"tpl1721629698912.png", record_pos=(0.434, -0.949), resolution=(1080, 2340)))
        poco("com.hexin.plat.android:id/scroll").swipe([-0.0593, -0.7521])
        poco("com.hexin.plat.android:id/scroll").swipe([-0.0593, -0.7521])
        if poco(text="退出当前账号").exists():
            poco(text="退出当前账号").click()
        if poco("com.hexin.plat.android:id/btnLogout").exists():
            poco("com.hexin.plat.android:id/btnLogout").click()
        if poco("com.hexin.plat.android:id/ok_btn").exists():
            poco("com.hexin.plat.android:id/ok_btn").click()

    # 切换账密登录
    # 点击帐号密码登录,帐号登录的元素会存在这两个
    if poco(nameMatches="com.hexin.plat.android:id/account_tv").exists() or poco(text="账号登录").exists():
        if poco(nameMatches="com.hexin.plat.android:id/account_tv").exists():
            print("com.hexin.plat.android:id/account_tv")

            poco(nameMatches="com.hexin.plat.android:id/account_tv").click()
        else:
            #personalLoginByLastIcon是上一次登录的方式,可能不是帐号登录的方式,所以要根据其他兄弟节点进行判断
            poco(text="账号登录").sibling("com.hexin.plat.android:id/personalLoginByLastIcon").click()
        # 点击帐号登录会出现允许登录弹窗-选择同意
        elements_to_click = [
            "com.hexin.plat.android:id/confirm",
            "com.android.permissioncontroller:id/permission_allow_button"
        ]

        for element_id in elements_to_click:
            element = poco(element_id)
            if element.exists():
                element.click()

    else:
        # 如果没有帐号密码登录的图标需要点击更多去找
        print("没有帐号密码登录的图标需要点击更多去找")
        poco("com.hexin.plat.android:id/personalLoginByMoreIcon").click()
        account_element = poco(nameMatches="com.hexin.plat.android:id/account_img|com.hexin.plat.android:id/account_tv")
        if account_element.exists():
            account_element.click()
        else:
            raise Exception("未找到帐号登录按钮")
    if poco("com.android.permissioncontroller:id/permission_allow_button").exists():
        poco("com.android.permissioncontroller:id/permission_allow_button").click()
    poco("com.hexin.plat.android:id/user_account").set_text(passname)
    poco("com.hexin.plat.android:id/password_input").set_text(pwd)
    poco("com.hexin.plat.android:id/cb_read_agree").click()
    poco("com.hexin.plat.android:id/login_text").click()
    sleep(2.0)
    if poco("com.hexin.plat.android:id/cancel_btn").exists():
        poco("com.hexin.plat.android:id/cancel_btn").click()
    if not poco("com.hexin.plat.android:id/head_img").exists():
        keyevent("BACK")


def login_out(appPackage, poco):
    from common.app_operation import stop_app_open_app
    # stop_app_open_app("com.hexin.plat.android")
    # sleep(5.0)

    zixuan = poco(text="自选", name="com.hexin.plat.android:id/title")
    back_findelement(zixuan)
    homePageFindElements(poco(text="首页"), 1, poco)
    poco(text="首页").click()
    sleep(3.0)
    poco("com.hexin.plat.android:id/head_img").click()
    poco("com.hexin.plat.android:id/iv_personal_setting").click()
    poco("com.hexin.plat.android:id/scroll").swipe([-0.0593, -0.7521])
    poco("com.hexin.plat.android:id/scroll").swipe([-0.0593, -0.7521])
    if not  poco(text="退出当前账号").exists():
        poco("com.hexin.plat.android:id/scroll").swipe([-0.0593, -0.7521])
    sleep(3.0)
    poco(text="退出当前账号").click()
    poco(text="退出登录").click()
    if not poco(text="登录账号 体验更多服务").exists():
        raise AssertionError("退出帐号失败")
    if poco("com.hexin.plat.android:id/ok_btn").exists():
        poco("com.hexin.plat.android:id/ok_btn").click()

    if poco("com.hexin.plat.android:id/iv_personal_back").exists():
        poco("com.hexin.plat.android:id/iv_personal_back").click()

