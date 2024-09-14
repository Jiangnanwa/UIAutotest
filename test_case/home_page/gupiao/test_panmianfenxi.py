#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_panmianfenxi 
   Description :
   Author : chenqiyue
   CreateDate：2024/08/06  用例id:
-------------------------------------------------
"""
from airtest.core.api import touch, exists
from airtest.core.cv import Template

from common.image import get_screenshot_by_element, image_to_base64, ths_ocr


def test_panmianfenxi(poco):
    """
用例名称
TC_盘面异动
用例id
587369
    """
    print("test_panmianfenxi")

    poco("com.hexin.plat.android:id/more_tv").click()
    stock_sz = poco("com.hexin.plat.android:id/navi_title_text").get_text()
    assert stock_sz == "上证指数"
    exists(Template(r"tpl1722947810993.png", record_pos=(0.421, -0.522), resolution=(1080, 2400)))
    element_list = [poco("com.hexin.plat.android:id/tv_yd_recorder"),
                    poco("com.hexin.plat.android:id/tv_date")]
    for i in element_list:
        if not i.exists():
            raise AssertionError(f"{i}元素不存在")
    poco("com.hexin.plat.android:id/backButton").click()
    bankuai  =   poco("com.hexin.plat.android:id/stock_top")

    Temp_pic = get_screenshot_by_element(bankuai)
    Temp_str = ths_ocr(image_to_base64(Temp_pic))
    target_text = Temp_str["text"].split("\n")
    print(target_text)
    # 使用列表推导式和split方法提取空格前的中文
    extracted_chinese = [text.split(' ')[0] for text in target_text]
    poco("com.hexin.plat.android:id/stock_top").click()
    #
    # #成分股tab选中
    exists(Template(r"tpl1722948302242.png", record_pos=(-0.396, 0.673), resolution=(1080, 2400)))
    stock_name = poco("com.hexin.plat.android:id/navi_title_text").get_text()
    assert  stock_name==extracted_chinese[0]
    poco("com.hexin.plat.android:id/backButton").click()
    poco("com.hexin.plat.android:id/yidong_curve_layout").sibling().click()
    title = poco("com.hexin.plat.android:id/title").get_text()
    bankuai  =   poco("com.hexin.plat.android:id/stock_top")

    Temp_pic = get_screenshot_by_element(bankuai)
    Temp_str = ths_ocr(image_to_base64(Temp_pic))
    target_text = Temp_str["text"].split("\n")
    print(target_text)
    # 使用列表推导式和split方法提取空格前的中文
    extracted_chinese = [text.split(' ')[0] for text in target_text]
    print(title)
    print(extracted_chinese[0])
    assert extracted_chinese[0] in title