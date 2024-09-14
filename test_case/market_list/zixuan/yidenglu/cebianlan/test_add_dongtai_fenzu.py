# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """
# -------------------------------------------------
#    File Name：    test_add_dongtai_fenzu
#    Description :
#    Author : chenqiyue
#    CreateDate：2024/03/11  用例id:
# -------------------------------------------------
# """
# import random
#
# import pytest
# from airtest.core.api import keyevent, sleep
#
# from common.app_operation import back_findelement
#
#
# @pytest.mark.skip(reason="服务器未调试通过")
# def test_add_dongtai_fenzu(poco):
#     """
#     用例名称
#     TC_自选侧边栏_添加动态分组
#     用例id
#     610718
#     """
#     try:
#         # 点击侧边栏菜单
#         sleep(3.0)
#         poco("com.hexin.plat.android:id/slidingmenu_menu").click()
#         if poco(text="我知道了").exists():
#             poco(text="我知道了").click()
#         # 点击新建动态分组
#         poco("com.hexin.plat.android:id/dynamic_group_btn").click()
#         poco("com.hexin.plat.android:id/create_group_text").click()
#         poco(text="上升通道").click()
#         if poco(text="下一步").exists():
#             poco(text="下一步").click()
#         sleep(3.0)
#         if poco(text="知道了").exists():
#             poco(text="知道了").click()
#             print("知道了点击")
#         poco(text="收藏策略(同步动态分组)").click()
#         # # 可能当前的动态分组已经被添加,需要取消收藏
#         # if poco(text="取消收藏(同步动态分组)").exists():
#         #     poco(text="取消收藏(同步动态分组)").click()
#         n = 1
#         while n < 100:
#             if not poco(text="动态分组中已存在该问句").exists():
#                 break
#             poco(text="取消").click()
#             # random_number = random.randint(1, 100)  # 生成一个1到100之间的随机整数
#             random_number = random.uniform(0.1, 1.0)
#             n = n + random_number
#             wenju = f"美股,盘前涨幅大于{n}%"
#             print(wenju)  # 打印结果，例如："前42日的上升通道"
#             poco("searchInput").click()
#             poco("searchInput").set_text(wenju)
#             poco(text="搜索").click()
#             sleep(5.0)
#             if poco(text="取消收藏(同步动态分组)").exists():
#                 poco(text="取消收藏(同步动态分组)").click()
#             poco(text="收藏策略(同步动态分组)").click()
#         sleep(3.0)
#         if poco(text="是否同步动态分组").exists():
#
#             poco(text="是否同步动态分组").click()
#         text1 = poco("android.widget.EditText").get_text()
#
#         poco(text="确认").click()
#         if poco(text="下一步").exists():
#             poco(text="下一步").click()
#             print("下一步点击")
#         if poco(text="知道了").exists():
#             poco(text="知道了").click()
#             print("知道了点击")
#         keyevent('BACK')
#         keyevent('BACK')
#         sleep(5.0)
#         dg_header_title_tv = poco("com.hexin.plat.android:id/dg_header_title_tv").get_text()
#
#         # 获取文案后面的数据的前6位
#         data1 = text1.split("大于")[1][:6]
#         data2 = dg_header_title_tv.split("大于")[1][:6]
#         print(f"data1{data1},data2{data2}")
#         # 比较前6位数据是否相同
#         if not data1 == data2:
#             raise  AssertionError(f"动态分组添加后，回到自选，不是新添加的分组，添加动态分组是{text1},回到自选tab展示的是{dg_header_title_tv}")
#
#         #if not poco("com.hexin.plat.android:id/dg_header_title_tv").get_text == text1:
#         # 展开侧边栏，查看是否存在新增的动态分组
#         poco("com.hexin.plat.android:id/slidingmenu_menu").click()
#         group_name = poco("com.hexin.plat.android:id/group_name").get_text()
#         # 获取文案后面的数据的前6位
#
#         data3 = group_name.split("大于")[1][:6]
#         print(data3)
#         if not data1 == data3:
#             raise  AssertionError(f"动态分组添加后，回到自选，侧边栏第一个动态分组不是新增的动态分组，新增的为{text1},动态分组第一个为{group_name}")
#     finally:
#         zixuan = poco(text="自选", name="com.hexin.plat.android:id/title")
#         print("finally恢复页面，回到自选股页面")
#         #恢复页面，回到自选股页面
#         if not zixuan.exists():
#             back_findelement(zixuan)
#         if zixuan.exists():
#             zixuan.click()
#         elif poco("自选").exists():
#             poco("自选").click()
#         poco("com.hexin.plat.android:id/slidingmenu_menu").click()
#         poco("com.hexin.plat.android:id/self_group_btn").click()
#         poco("com.hexin.plat.android:id/self_stock_name").click()