# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """
# -------------------------------------------------
#    File Name：test_dongtaifenzu_jump_weidenglu
#    Description :
#    Author : chenqiyue
#    CreateDate：2024/05/14
#    用例id:
# ------------------------------------------------
# """
# import pytest
# from airtest.core.api import exists, sleep, touch
# from airtest.core.cv import Template
# from poco.exceptions import PocoNoSuchNodeException
#
#
# @pytest.mark.parametrize("tab,dtfz_name,wenju,filename",
#                          [("动态分组|动态分组(8)", "涨幅大于5%的非新股", "涨幅大于5%的非新股", "tpl1715757466445.png"),
#                           ("全部|全部(8)", "昨天涨停不含新股", "昨天涨停不含新股", "tpl1715757380557.png")])
# def test_dongtaifenzu_jump_weidenglu(poco, tab, dtfz_name, wenju, filename):
#     """
#     用例名称
#     TC_自选分组抽屉_未登录点击动态分组
#     用例id
#     2196730  poco("涨幅大于5%的非新股"), poco("昨天涨停不含新股")
#     """
#     from page.CebianlanPage import CebianlanPage
#     print("test_dongtaifenzu_jump_weidenglu")
#     try:
#         print(f"{tab}点击")
#         sleep(2.0)
#         poco(textMatches=tab).click()
#     except PocoNoSuchNodeException:
#
#         touch(Template(r"%s" % filename, record_pos=(-0.362, -0.476), resolution=(1170, 2532)))
#     sleep(2.0)
#     print(f"{dtfz_name}点击")
#     poco(text=dtfz_name).click()
#     print(f"{dtfz_name}点击成功")
#     sleep(5.0)
#
#     element_list = [CebianlanPage.dg_header_title_tv,
#                     CebianlanPage.content_column, CebianlanPage.dg_header_update_time_tv, CebianlanPage.voice_assistant,
#                     CebianlanPage.navigation]
#     for index, value in enumerate(element_list):
#
#         if not value.exists():
#             print(f"{index}不存在")
#             raise AssertionError(f"{index}不存在")
#         else:
#             print(f"{index}存在")
#     exists(Template(r"tpl1715669921890.png", record_pos=(-0.001, -0.909), resolution=(1170, 2532)))
#     exists(Template(r"tpl1715655297341.png", record_pos=(0.003, -0.77), resolution=(1170, 2532)))
#     exists(Template(r"tpl1715655308075.png", record_pos=(0.392, -0.651), resolution=(1170, 2532)))
