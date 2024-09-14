# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """
# -------------------------------------------------
#    File Name：conftest.py
#    Description :
#    Author : chenqiyue
#    CreateDate：2023/04/03
#    用例id:
# ------------------------------------------------
# """
#
# from airtest.core.api import *
#
# from common.app_operation import stop_app_open_app, back_findelement
# from common.function import homePageFindElements
#
# import pytest
#
# from common.login import login_by_password, login_out
#
#
# @pytest.fixture(scope="function")
# def final_teardown_yidenglu(poco, request):
#     # 获取传入的账号和密码，如果没有传入则使用默认值
#     username = request.param.get("username", "lwtest1149")
#     password = request.param.get("password", "123456")
#     nicheng = request.param.get("nicheng", "自动化专用")
#     # 重启app
#     stop_app_open_app("com.hexin.plat.android")
#     sleep(8.0)
#     start_app("com.hexin.plat.android", activity="LogoEmptyActivity")
#     homePageFindElements(poco(text="首页"), 1, poco)
#     # 点击左上角头像进入个人中心
#     keyevent("BACK")
#     homePageFindElements(poco("com.hexin.plat.android:id/head_img"), 1, poco).click()
#     # 处理个人中心广告
#     # sleep(3)
#     # poco("com.hexin.plat.android:id/personalLoginByPhoneIcon").click()
#     sleep(3)
#     if poco(textMatches="images-.*").exists():
#         poco(textMatches="images-.*").click()
#     if not poco(text=nicheng).exists():
#         login_by_password(username, password, "com.hexin.plat.android", poco)
#
#
#
#
# @pytest.fixture(scope="session", autouse=True)
# def session_teardown(poco):
#     yield
#     # 这里放置测试会话结束后需要执行的代码
#     print("结束后运行退出帐号")
#     stop_app_open_app("com.hexin.plat.android")
#     sleep(8.0)
#     login_out("com.hexin.plat.android", poco)
