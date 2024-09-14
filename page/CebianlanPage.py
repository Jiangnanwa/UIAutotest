#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    CebianlanPage 
   Description :
   Author : chenqiyue
   CreateDate：2024/05/15  用例id:
-------------------------------------------------
"""


class CebianlanPage:
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    # 自选-持仓股
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    ccg_stock_name = poco("com.hexin.plat.android:id/ccg_stock_name")
    # 自选-自选股
    optional_stocks = poco("com.hexin.plat.android:id/optional_stocks")
    # 自选=新建分组
    create_btn = poco("com.hexin.plat.android:id/create_btn")
    # 自选-新建自选分组
    create_custom_group_text = poco("com.hexin.plat.android:id/create_custom_group_text")
    # 自选-新建动态分组
    create_dynamic_group_text = poco("com.hexin.plat.android:id/create_dynamic_group_text")
    # 自选-全部
    all_tab = poco(text="全部")
    #自选-展开自选分组抽屉-管理分组
    guanlifenzu  = poco(text="管理分组")
    #自选-展开自选分组抽屉-排序/删除
    sort_delete = poco(text = "排序/删除")
    #自选-动态分组-语音助手
    voice_assistant= poco("com.hexin.plat.android:id/voice_assistant")
    #自选-动态分组-搜索按钮
    new_title_search = poco("com.hexin.plat.android:id/new_title_search")
    # 自选-动态分组-登录关闭按钮
    close_img =poco("com.hexin.plat.android:id/close_img")
    #自选-动态分组-股票列表表头数据
    content_column = poco("com.hexin.plat.android:id/content_column")
    # 自选-动态分组-股票元素
    fixed_column = poco("com.hexin.plat.android:id/fixed_column")
    # 自选-动态分组-更新时间
    dg_header_update_time_tv =poco("com.hexin.plat.android:id/dg_header_update_time_tv")
    # 自选-动态分组-更新时间
    dg_header_update_tip_tv =poco("com.hexin.plat.android:id/dg_header_update_tip_tv")
    # 自选-动态分组-问句
    dg_header_title_tv =poco("com.hexin.plat.android:id/dg_header_title_tv")
    #自选-动态分组-导航栏
    navigation = poco("同花顺条件选股")