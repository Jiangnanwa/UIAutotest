# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """
# -------------------------------------------------
#    File Name：test_groupall_addgroup_weidenglu
#    Description :
#    Author : chenqiyue
#    CreateDate：2024/05/13
#    用例id:
# ------------------------------------------------
# """
# import pytest
# from airtest.core.api import exists, touch, sleep
# from airtest.core.cv import Template
# from poco.exceptions import PocoNoSuchNodeException
#
#
#
#
# @pytest.mark.parametrize("caseid,tab_name,tab_num", [("TC_自选分组抽屉_全部分组_未登录删除:2196840", "全部", "全部(8)"),
#                                                      ("TC_自选分组抽屉_动态分组_未登录删除/排序动态分组:2196726", "自选分组", "自选分组(0)"),
#                                                      ("TC_自选分组抽屉_自选分组_未登录删除/排序:2196728", "动态分组", "动态分组(8)")])
# def test_groupall_add_dongtaigroup_weidenglu(poco, caseid, tab_name, tab_num):
#     """
#     用例名称
#     2196840
#     TC_自选分组抽屉_全部分组_未登录删除/排序
#     2196726
#     TC_自选分组抽屉_动态分组_未登录删除/排序动态分组
#     2196728
#     TC_自选分组抽屉_自选分组_未登录删除/排序
#     """
#     from page.CebianlanPage import CebianlanPage
#
#     print("test_groupall_addgroup_weidenglu")
#     if poco(text=tab_num).exists():
#         print("不用切换tab")
#     else:
#         poco(text=tab_name).click()
#         if not poco(text=tab_num).exists():
#             assert (f"{tab_num}不存在,{caseid}")
#     CebianlanPage.guanlifenzu.click()
#     CebianlanPage.sort_delete.click()
#
#     element_list = [poco(text="手机验证码登录"), poco(text="首次登录将自动注册"),poco("com.hexin.plat.android:id/weixin_login"), poco(text="我已阅读并同意隐私政策和用户协议，根据证监会要求，所有证券交易行为要经过手机号验证")]
#     for i in element_list:
#         if not i.exists():
#             assert (f"{i}不存在,{caseid}")
#     if poco("com.hexin.plat.android:id/close_img").exists():
#         poco("com.hexin.plat.android:id/close_img").click()
#     print("关闭登录弹窗，分组tab展示")
#     sleep(1.0)
#     if not poco(text=tab_num).exists():
#         print("选中{tab_name},点击新建动态分组，收起登录弹窗，再次展开抽屉，tab未选中{tab_name}")
#     poco("com.hexin.plat.android:id/overlay").swipe([-0.4325, -0.0145])