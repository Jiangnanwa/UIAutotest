#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_documentation 
   Description :
   Author : chenqiyue
   CreateDate：2024/07/29  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import touch
from airtest.core.assertions import assert_exists
from airtest.core.cv import Template


@pytest.mark.parametrize("final_teardown_gerenzhongxin", [{}], indirect=True)
def test_documentation(poco):
    """
    用例名称
    TC_（已自动化）使用文档
    用例id
    1101034
    """
    poco("com.hexin.plat.android:id/iv_personal_setting").click()
    poco("com.hexin.plat.android:id/scroll").swipe([-0.0313, -0.763])
    poco(text="使用文档").click()
    # 校验“使用文档”页面是否存在
    assert_exists(Template(r"tpl1722234711013.png", record_pos=(-0.001, -0.246), resolution=(1080, 2340)), "使用文档页面校验")

    # 点击页面中的某个元素
    poco("com.hexin.plat.android:id/title_bar_middle").click()

    # 点击“如何添加自选股”并校验
    poco(text="如何添加自选股").click()

    assert_exists(Template(r"tpl1722234772329.png", record_pos=(-0.006, -0.063), resolution=(1080, 2340)), "如何添加自选股")
    poco("com.hexin.plat.android:id/title_bar_img").click()
    # 点击“自选股看资金”并校验
    poco(text="自选股看资金").click()
    assert_exists(Template(r"tpl1722234802922.png", record_pos=(-0.014, -0.461), resolution=(1080, 2340)), "自选股看资金")
    poco("com.hexin.plat.android:id/title_bar_img").click()

    # 点击“查看我的持仓”并校验
    poco(text="查看我的持仓").click()
    assert_exists(Template(r"tpl1722234823938.png", record_pos=(-0.019, 0.08), resolution=(1080, 2340)), "查看我的持仓")
    poco("com.hexin.plat.android:id/title_bar_img").click()

    # 点击“自选股排序”并校验
    poco(text="自选股排序").click()
    assert_exists(Template(r"tpl1722234861469.png", record_pos=(-0.006, -0.222), resolution=(1080, 2340)), "自选股排序")
    poco("com.hexin.plat.android:id/title_bar_img").click()

    # 点击“分时k线切换”并校验
    poco(text="分时k线切换").click()
    assert_exists(Template(r"tpl1722234881852.png", record_pos=(0.005, -0.07), resolution=(1080, 2340)), "分时k线切换")
    poco("com.hexin.plat.android:id/title_bar_img").click()

    # 点击“查看关联板块、F10”并校验
    poco(text="查看关联板块、F10").click()
    assert_exists(Template(r"tpl1722234899516.png", record_pos=(-0.005, -0.073), resolution=(1080, 2340)), "查看关联板块、F10")
    poco("com.hexin.plat.android:id/title_bar_img").click()

    # 若“分时切换指标”不存在，则点击“分时/k线操作”
    if not poco(text="分时切换指标").exists():
        if poco(text="分时/k线操作").exists():
            poco(text="分时/k线操作").click()
        else:
            touch(Template(r"tpl1722579380498.png", record_pos=(-0.435, -0.155), resolution=(1080, 2376)))


    # 点击“分时切换指标”并校验
    poco(text="分时切换指标").click()
    assert_exists(Template(r"tpl1722234974296.png", record_pos=(-0.007, 0.011), resolution=(1080, 2340)), "分时切换指标")

    poco("com.hexin.plat.android:id/title_bar_img").click()

    # 点击“市场行情”并校验
    poco(text="市场行情").click()
    assert_exists(Template(r"tpl1722235022136.png", record_pos=(-0.01, -0.444), resolution=(1080, 2340)), "请填写测试点")
    poco("com.hexin.plat.android:id/title_bar_img").click()

    # 点击“资讯查看”，再点击提示信息
    poco(text="资讯查看").click()
    if not poco(text="可左右滑动查看各栏目的资讯。"):
        raise AssertionError("无可左右滑动查看各栏目的资讯。")
    poco("com.hexin.plat.android:id/title_bar_img").click()

    # 点击“个人账户”，再点击“第三方登录注册”并校验
    poco(text="个人账户").click()
    poco(text="第三方登录注册").click()
    assert_exists(Template(r"tpl1722235103929.png", record_pos=(-0.014, -0.113), resolution=(1080, 2340)), "请填写测试点")
    poco("com.hexin.plat.android:id/title_bar_img").click()

    # 若“切换行情服务器”不存在，则点击“设置”
    if not poco(text="切换行情服务器").exists():
        poco(text="设置").click()

    # 点击“切换行情服务器”并校验
    poco(text="切换行情服务器").click()
    assert_exists(Template(r"tpl1722235145940.png", record_pos=(-0.017, -0.206), resolution=(1080, 2340)), "请填写测试点")

    poco("com.hexin.plat.android:id/title_bar_img").click()
    poco("com.hexin.plat.android:id/title_bar_middle").click()
