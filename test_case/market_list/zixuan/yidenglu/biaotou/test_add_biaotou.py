#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_add_biaotou 
   Description :
   Author : chenqiyue
   CreateDate：2024/03/13  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import keyevent, sleep, touch
from airtest.core.cv import Template


@pytest.mark.parametrize("final_teardown_yidenglu", [{}], indirect=True)
@pytest.mark.parametrize("type,child_text", [("行情表头", "上市涨幅"), ("董事长常用", "董事长姓名")])
def test_add_hq_biaotou(poco, type, child_text):
    """
    用例名称
    TC_自选表头_添加行情表头（回归）
    用例id
    1282777
    操作步骤:
    """
    if poco(text="我知道了").exists():
        poco(text="我知道了").click()
    if poco("com.hexin.plat.android:id/closeBt").exists():
        poco("com.hexin.plat.android:id/closeBt").click()
    if not poco(
            nameMatches="com.hexin.plat.android:id/slidingmenu_editview|com.hexin.plat.android:id/slidingmenu_tx2").exists():
        keyevent('BACK')
    poco(nameMatches="com.hexin.plat.android:id/slidingmenu_editview|com.hexin.plat.android:id/slidingmenu_tx2").click()
    if not poco(text="编辑表头").exists():
        poco(nameMatches=".*#.*#.*").swipe([-0.595, 0.0065])

    poco(text="编辑表头").click()
    sleep(5.0)
    # poco(text="打开").click()
    poco(text="编辑表头")[1].click()
    sleep(5.0)
    if poco(text="恢复默认").exists():

        poco(text="恢复默认").click()
    else:
        touch(Template(r"恢复默认.png", record_pos=(0.405, -0.499), resolution=(1080, 2340)))
    sleep(3.0)
    if  poco(text="确认恢复").exists():

        poco(text="确认恢复").click()
    else:
        touch(Template(r"确认恢复按钮.png", record_pos=(0.168, 0.189), resolution=(1080, 2340)))

    sleep(3.0)
    if poco(text="添加表头").exists():
        poco(text="添加表头").click()
    else:
        touch(Template(r"tpl1721981467800.png", record_pos=(0.256, -0.495), resolution=(1080, 2340)))

    poco(text=type).click()
    sleep(5.0)
    # 获取父节点
    # 找到所有包含文本“已添加”的元素
    # added_elements = poco(text="已添加")[4]
    # added_elements.click()

    # parent_node = add.parent()
    # # 获取兄弟节点
    # sibling_node = parent_node.sibling()
    # # 获取子节点
    # child_text = sibling_node.child("android.widget.TextView").get_text()
    # print(child_text)

    # add = poco(text="添加", name="android.widget.TextView")[3]
    # add.click()

    touch(Template(r"添加表头页面添加按钮.png", record_pos=(0.399, -0.623), resolution=(1080, 2340)))
    keyevent('BACK')
    poco(text="保存").click()
    keyevent('BACK')
    sleep(3.0)
    if not poco(text=child_text).exists():
        print("表头添加失败")
        raise AssertionError(f"{child_text}表头添加失败")
