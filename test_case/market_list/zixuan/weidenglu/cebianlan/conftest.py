# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """
# -------------------------------------------------
#    File Name：conftest
#    Description :
#    Author : chenqiyue
#    CreateDate：2024/02/22
#    用例id:
#    机型：p40pro
# ------------------------------------------------
# """
#
# import pytest
# from airtest.core.api import sleep, touch
# from airtest.core.cv import Template
# from poco.exceptions import PocoNoSuchNodeException
#
# from common.app_operation import stop_app_open_app
# from common.function import homePageFindElements
#
#
# @pytest.fixture(scope="function", autouse=True)
# def enter_main_inflow_cebianlan(poco):
#     print("打开自选股边栏")
#     try:
#
#         poco("com.hexin.plat.android:id/slidingmenu_menu").click()
#     except PocoNoSuchNodeException:
#         touch(Template(r"tpl1715584836254.png", record_pos=(-0.431, -0.904), resolution=(1170, 2532)))
#     finally:
#         sleep(3.0)