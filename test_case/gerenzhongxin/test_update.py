#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    text_update 
   Description :
   Author : chenqiyue
   CreateDate：2024/07/29  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import snapshot
from airtest.core.assertions import assert_exists
from airtest.core.cv import Template

from common.image import ths_ocr, image_to_base64


@pytest.mark.parametrize("final_teardown_gerenzhongxin", [{}], indirect=True)
def test_update(poco):
    """
    用例名称
    TC_（已自动化）版本更新
    用例id
    1101009
    """
    poco("com.hexin.plat.android:id/iv_personal_setting").click()
    poco("com.hexin.plat.android:id/scroll").swipe([-0.0313, -0.763])
    poco(text="版本更新").click()
    snapshot(filename="screenshot.png")
    Temp_str = ths_ocr(image_to_base64("screenshot.png"))
    toast = Temp_str["text"]
    toast = f"{toast}"
    print(toast)
    if "当前已是最新版本" not in toast:
        raise AssertionError(f"当前已是最新版本提示信息为{toast}")
    else:
        print(f"点击版本更新提示信息为{toast}")
    assert_exists(Template(r"tpl1722236634844.png", record_pos=(-0.006, 0.031), resolution=(1080, 2340)),
                  "当前已是最新版本弹窗是否存在")
