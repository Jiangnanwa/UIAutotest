# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """
# -------------------------------------------------
#    File Name：test_chicanggu_jumpup
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
# from common.image import get_color_by_element
#
#
#
# def test_chicanggu_jump(poco):
#     """
#     用例名称
#     TC_自选分组抽屉_未登录点击持仓股
#     用例id
#     2196731
#     """
#     from page.CebianlanPage import CebianlanPage
#     print("test_chicanggu_jumpup")
#
#     chicanggu = CebianlanPage.ccg_stock_name
#     zixuangu = CebianlanPage.optional_stocks
#     print("点击持仓股")
#     chicanggu.click()
#
#     element_list = [poco(text="手机验证码登录"), poco(text="首次登录将自动注册"),poco("com.hexin.plat.android:id/weixin_login"), poco(text="我已阅读并同意隐私政策和用户协议，根据证监会要求，所有证券交易行为要经过手机号验证")]
#     for i in element_list:
#         if not i.exists():
#             assert (f"{i}不存在,{2196731}")
#     if poco("com.hexin.plat.android:id/close_img").exists():
#         poco("com.hexin.plat.android:id/close_img").click()
#     sleep(3.0)
#     zixuangu = zixuangu.parent()
#     yanse = get_color_by_element(zixuangu, shield_list=["white", "black", "gray", "green"])
#     pytest.assume(yanse == "red")
#     exists(Template(r"tpl1715605324640.png", record_pos=(-0.384, -0.862), resolution=(1170, 2532)))
#     poco("com.hexin.plat.android:id/overlay").swipe([-0.4325, -0.0145])
