#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_qiehuanfuwuqi 
   Description :
   Author : chenqiyue
   CreateDate：2024/08/06  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.assertions import assert_exists
from airtest.core.cv import Template

from common.function import myFindElements
from common.image import get_color_by_element, get_screenshot_by_element, get_color


@pytest.mark.parametrize("final_teardown_gerenzhongxin", [{}], indirect=True)
def test_qiehuanfuwuqi(poco):
    """
用例名称
TC_（已自动化）切换服务器
用例id
1100995
    """
    print("test_qiehuanfuwuqi")
    myFindElements("com.hexin.plat.android:id/iv_personal_setting", 2, poco)
    if poco("返回").exists():
        poco("返回").click()
    poco("com.hexin.plat.android:id/iv_personal_setting").click()
    server_list = [
        {
            "name": "联通服务器",
            "poco_selector": poco(text="联通服务器"),
            "resource_id": "com.hexin.plat.android:id/ltserver_iv"
        },
        {
            "name": "移动服务器",
            "poco_selector": poco(text="移动服务器"),
            "resource_id": "com.hexin.plat.android:id/ydserver_iv"
        },
        {
            "name": "电信服务器",
            "poco_selector": poco(text="电信服务器"),
            "resource_id": "com.hexin.plat.android:id/dxserver_iv"  # 假设电信服务器的资源ID
        },
        {
            "name": "VIP专线服务器",
            "poco_selector": poco(text="VIP专线服务器"),
            "resource_id": "com.hexin.plat.android:id/vipserver_iv"  # 假设VIP专线服务器的资源ID
        },
        {
            "name": "自动选择",
            "poco_selector": poco(text="自动选择"),
            "resource_id": "com.hexin.plat.android:id/qtserver_iv"  # 假设自动选择的资源ID
        }
    ]

    # 示例代码，使用这个列表
    for server in server_list:
        print(f"正在切换到: {server['name']}")

        switch_button = poco(text="切换服务器")
        switch_button.click()
        server['poco_selector'].click()
        poco_selector = poco(text=server['name'])
        print(poco_selector.get_text())
        # 使用服务器特定的资源ID来找到旁边的元素
        anniu = poco_selector.sibling(server['resource_id'])
        tmp_png = get_screenshot_by_element(anniu)
        title_color = get_color(tmp_png, shield_list=['white'])
        print(title_color)
        assert title_color == "red2"
        # 这里可以根据需要添加颜色断言或其他逻辑

        confirm_button = poco("com.hexin.plat.android:id/ok_btn")
        confirm_button.click()

        if server['name'] == "VIP专线服务器":
            if not poco(text="同花顺VIP"):
                assert AssertionError("没有跳转到同花顺VIP页面")
            assert_exists(Template(r"tpl1722935802208.png", record_pos=(0.006, -0.599), resolution=(1080, 2400)),
                          "同花顺金牛会员权益礼包价值2888")
            poco("com.hexin.plat.android:id/title_bar_img").click()
