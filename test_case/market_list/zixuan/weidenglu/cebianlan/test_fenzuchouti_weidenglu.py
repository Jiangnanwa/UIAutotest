# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """
# -------------------------------------------------
#    File Name：test_fenzuchouti_weidenglu
#    Description :
#    Author : chenqiyue
#    CreateDate：2024/05/13
#    用例id:
# ------------------------------------------------
# """
# import pytest
# from airtest.core.api import exists
# from airtest.core.cv import Template
#
#
# def test_fenzuchouti_weidenglu(poco):
#     """
#     用例名称
#     TC_自选分组抽屉_未登录界面显示
#     用例id
#     2196724
#     """
#     print("test_fenzuchouti_weidenglu")
#
#
#     exists(Template(r"tpl1715568675176.png", record_pos=(-0.366, -0.856), resolution=(1170, 2532)))
#     exists(Template(r"tpl1715568691949.png", record_pos=(-0.362, -0.73), resolution=(1170, 2532)))
#     exists(Template(r"tpl1715568715252.png", record_pos=(-0.112, 0.079), resolution=(1170, 2532)))
#     element_list = [poco(text="快叫朋友分享吧~"), poco(text="我的关注(0)"), poco(text="自选股"), poco(text="持仓股"), poco(text="还不会用？查看自选分组使用技巧"),
#                     poco(text="全部(8)"), poco(text="涨幅大于5%的非新股"), poco(text="昨天涨停不含新股"), poco(text="均线多头排列的股票"),
#                     poco(text="MACD与KDJ双金叉").poco(text="今天的新股开板"), poco(text="今天的新股上市"), poco(text="最近10天有2次涨停"), poco(text="市盈率小于15的股票"),
#                     poco(text="自选分组"), poco(text="动态分组")]
#     for i in element_list:
#         if not i.exists() :
#             assert(f"{i}不存在")
