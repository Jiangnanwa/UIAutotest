#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapankongjian_morenzhanshi 
   Description :
   Author : chenqiyue
   CreateDate：2024/02/28  用例id:
-------------------------------------------------
"""



def test_dapankongjian_morenzhanshi(poco):
    """
    用例名称
    TC_大盘控件_股指删除（自动化已实现）
    用例id
    1273937

    """
    zhishu = poco("com.hexin.plat.android:id/zhishu_name").get_text()
    #1.在切换股指页面点击已添加股指“上证指数”前的“—”按钮
    # 2.点击完成按钮
    poco("com.hexin.plat.android:id/guzhi_set_btn").click()
    # if not poco("com.hexin.plat.android:id/operation_btn").exists():
    #     poco(text="沪深指数").click()
    # poco("com.hexin.plat.android:id/operation_btn").click()
    # #assert_exists(Template(r"tpl1709111900600.png", record_pos=(-0.317, -0.67), resolution=(1080, 2340)), "请填写测试点")
    # poco("com.hexin.plat.android:id/tv_finish").click()
    # if poco("com.hexin.plat.android:id/zhishu_name").get_text() =="沪":
    #     raise  AssertionError("切换股指页面关闭，大盘控件 展示“上证指数”")

    delete = poco(text=zhishu).parent().sibling("com.hexin.plat.android:id/index_delete")

    if delete.exists():
        delete.click()

    else:
        poco("com.hexin.plat.android:id/operation_btn").click()
    poco(nameMatches="com.hexin.plat.android:id/back|com.hexin.plat.android:id/title_bar_img").click()

    if poco(text=zhishu).exists():
        raise AssertionError(f"{zhishu}删除失败")