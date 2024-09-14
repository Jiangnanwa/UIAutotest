#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_dapan_chengjiaoe
   Description：  TC_成交额_数据正确性校验
   Author：       duanxufei
   CreateDate：   2024/3/12 14:18
   CaseID：       1752985
-------------------------------------------------
"""
import pytest


def test_jiaoyanxiaoshu(poco):
    """
    查看成交额及成交额对比小数位
    """
    poco("行情").click()
    chengjiaoe_text = poco("com.hexin.plat.android:id/amount_text").get_text()

    assert '.' not in chengjiaoe_text

@pytest.mark.skip(reason="服务器未调试通过")
def test_shujuyuanjiaoyan(poco):
    """
    查看今日成交额数值，与上证指数成交额、深证成指成交额相加对比
    """
    target_text = poco("com.hexin.plat.android:id/amount_text").get_text()
    # poco("com.hexin.plat.android:id/tips").click()
    # poco("com.hexin.plat.android:id/search_input").set_text("883957")
    # poco("com.hexin.plat.android:id/search_associate_list").children()[0].click()
    # 点击上证指数
    poco("com.hexin.plat.android:id/index_container").click()
    tmp_shangzheng_text = poco("com.hexin.plat.android:id/fenshi_headline_view").attr("desc")
    tmp_shangzheng_list = tmp_shangzheng_text.split("额")
    shangzheng_chengjiaoe = float(tmp_shangzheng_list[-1][0:-1])

    poco("com.hexin.plat.android:id/navi_right_icon").click()
    tmp_shenzheng_text = poco("com.hexin.plat.android:id/fenshi_headline_view").attr("desc")
    tmp_shenzheng_list = tmp_shenzheng_text.split("额")
    shenzheng_chengjiaoe = float(tmp_shenzheng_list[-1][0:-1])

    assert target_text[0:-1] == str(round(shangzheng_chengjiaoe + shenzheng_chengjiaoe))
