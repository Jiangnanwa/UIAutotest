#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_cebianlan_shuliangxianshi 
   Description :
   Author : chenqiyue
   CreateDate：2024/07/24  用例id:
-------------------------------------------------
"""
import pytest


@pytest.mark.parametrize("final_teardown_yidenglu", [{}], indirect=True)
def test_cebianlan_shuliangxianshi(poco):
    """
用例名称
TC_自选侧边栏_已登录0<分组数量<300显示
用例id
1244207
    """
    if poco(textMatches="自选分组.*").exists():
        poco(textMatches="自选分组.*").click()
    elements_to_check = [
        (poco(textMatches="我的关注.*"), "my_follow_head_text"),
        (poco(textMatches="我的分组.*|全部.*|全部|自选分组.*"), "my_group_head_text"),
        (poco(textMatches="还不会用？查看自选分组使用技巧"), "clickable_area")
    ]

    # 遍历元素列表，逐个校验元素是否存在
    for locator, element_name in elements_to_check:
        if not locator.exists():
            raise AssertionError(f"Element '{element_name}' not found.")
        else:
            print(f"Element '{element_name}' found.")

    clickable_area = poco("com.hexin.plat.android:id/clickable_area")
    tips_text = poco("com.hexin.plat.android:id/tips_text")

    # 获取元素的位置信息和宽高信息
    clickable_area_pos = clickable_area.get_position()
    clickable_area_size = clickable_area.get_size()
    # 文案的坐标数据
    tips_text_pos = tips_text.get_position()
    tips_text_size = tips_text.get_size()

    # 计算clickable_area和tips_text的中心点
    clickable_area_center_x = clickable_area_pos[0] + clickable_area_size[0] / 2
    clickable_area_center_y = clickable_area_pos[1] + clickable_area_size[1] / 2
    tips_text_center_x = tips_text_pos[0] + tips_text_size[0] / 2
    tips_text_center_y = tips_text_pos[1] + tips_text_size[1] / 2
    print(f"文案x{tips_text_center_x}")
    print(f"文案y{tips_text_center_y}")
    print(f"容器y{clickable_area_center_y}")
    print(f"容器x{clickable_area_center_x}")
    # 校验tips_text是否居中
    assert abs(clickable_area_center_x - tips_text_center_x) < 0.3, "tips_text未在clickable_area水平居中"
    assert abs(clickable_area_center_y - tips_text_center_y) < 0.3, "tips_text未在clickable_area垂直居中"
    poco(text="动态分组").click()
    assert poco(textMatches="美股,盘前涨幅大于.*").exists(), "动态分组名称"
