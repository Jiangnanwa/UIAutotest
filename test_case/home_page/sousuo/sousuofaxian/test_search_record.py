#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_search_record 
   Description :
   Author : chenqiyue
   CreateDate：2024/07/17  用例id:
-------------------------------------------------
"""

from common.app_operation import back_findelement
from airtest.core.api import touch, sleep, exists
from airtest.core.cv import Template


def test_search_record(poco):
    """
用例名称
TC_综合搜索_历史记录生成
用例id
1482562
    """

    assert poco(text="综合").attr('selected') == True, "综合TAB未被选中"
    # 1. 点击热股榜中股票，查看历史搜索记录情况
    for index, stock in enumerate(poco("com.hexin.plat.android:id/stock_name")):
        stock_name = stock.get_text()
        print(f"点击股票：{stock_name}")
        stock.click()
        # poco("com.hexin.plat.android:id/backButton").click()
        # if not poco("查看更多").exists():
        #     keyevent("BACK")
        back_findelement(poco(text="综合"))
        sleep(1.0)
        if poco("com.hexin.plat.android:id/ime_change_bar_close").exists():
            poco("com.hexin.plat.android:id/ime_change_bar_close").click()
            print("收起键盘")

        records = poco("com.hexin.plat.android:id/name")

        # 跳过第四个元素的断言检查
        if index < 3:
            assert records[0].get_text() == stock_name, f"第一个记录不是：{stock_name}"
        sleep(1.0)
    # 2. 横滑并点击热基榜中股票，查看历史搜索记录情况
    poco(text="热股榜").swipe([-0.7802, 0.0117])
    hot_funds = poco("com.hexin.plat.android:id/content")
    for fund in hot_funds:
        fund_name = fund.get_text()
        print(f"点击基金：{fund_name}")
        fund.click()
        back_findelement(poco(text="综合"))
        # poco("com.hexin.plat.android:id/left_btn").click()
        if poco("com.hexin.plat.android:id/ime_change_bar_close").exists():
            poco("com.hexin.plat.android:id/ime_change_bar_close").click()
            print("收起键盘")
        records = poco("com.hexin.plat.android:id/name")
        assert records[0].get_text() == fund_name, f"第一个记录不是：{fund_name}"

    # 3. 选中股票tab，点击股票tab下的词条，按键返回综合tab，查看历史搜索记录情况
    # poco(text="股票").click()
    # stock_items = poco("com.hexin.plat.android:id/title")
    #
    # item_name = stock_items.get_text()
    # stock_items.click()
    # keyevent("BACK")
    # records = poco("com.hexin.plat.android:id/name")
    # assert records[0].get_text() == item_name, f"第一个记录不是：{item_name}"
    # poco(text="综合").click()

    # 4. 在搜索栏中输入“茅台”，在弹起键盘中点击【搜索】，查看历史搜索记录情况
    poco("com.hexin.plat.android:id/search_input").click()
    poco("com.hexin.plat.android:id/search_input").set_text("茅台")
    sleep(1.0)
    poco(text="搜索").click()
    poco("com.hexin.plat.android:id/close_image").click()
    records = poco("com.hexin.plat.android:id/name")
    assert records[0].get_text() == "茅台", "第一个记录不是：茅台"

    # 5. 在搜索栏中输入“FTSE”，在联想结果中点击【搜索：FTSE】，查看历史搜索记录情况
    poco("com.hexin.plat.android:id/search_input").click()
    poco("com.hexin.plat.android:id/search_input").set_text("FTSE")
    sleep(1.0)
    poco("com.hexin.plat.android:id/search_action").click()
    poco("com.hexin.plat.android:id/close_image").click()
    records = poco("com.hexin.plat.android:id/name")
    assert records[0].get_text() == "FTSE", "第一个记录不是：FTSE"

    # 6. 在搜索栏中输入不存在的股票代码“344678”，在联想结果中点击股票词条，查看历史搜索记录情况
    poco("com.hexin.plat.android:id/search_input").click()
    sleep(1.0)
    poco("com.hexin.plat.android:id/search_input").set_text("344678")
    poco("com.hexin.plat.android:id/search_action").click()
    poco("com.hexin.plat.android:id/close_image").click()
    records = poco("com.hexin.plat.android:id/name")
    assert records[0].get_text() == "344678", "第一个记录不是：344678"

    # 7. 在搜索栏中输入“决策”，在弹起键盘中点击【搜索】，查看历史搜索记录情况
    poco("com.hexin.plat.android:id/search_input").click()
    poco("com.hexin.plat.android:id/search_input").set_text("决策")
    sleep(1.0)
    poco("com.hexin.plat.android:id/search_action").click()
    poco("com.hexin.plat.android:id/close_image").click()
    records = poco("com.hexin.plat.android:id/name")
    assert records[0].get_text() == "决策", "第一个记录不是：决策"

    # 8. 在搜索栏中输入“快速选股”，在联想结果中点击【搜索：快速选股】，查看历史搜索记录情况
    poco("com.hexin.plat.android:id/search_input").click()
    poco("com.hexin.plat.android:id/search_input").set_text("快速选股")
    poco("com.hexin.plat.android:id/search_action").click()
    poco("com.hexin.plat.android:id/close_image").click()
    records = poco("com.hexin.plat.android:id/name")
    assert records[0].get_text() == "快速选股", "第一个记录不是：快速选股"

    # 9. 在搜索栏中输入“沪深港通”，在联想结果中点击沪深港通宫格图标，查看历史搜索记录情况
    poco("com.hexin.plat.android:id/search_input").click()
    poco("com.hexin.plat.android:id/search_input").set_text("沪深港通")
    poco("com.hexin.plat.android:id/search_action").click()
    poco("com.hexin.plat.android:id/close_image").click()
    records = poco("com.hexin.plat.android:id/name")
    assert records[0].get_text() == "沪深港通", "第一个记录不是：沪深港通"

    # 10. 连续两次搜索“沪深港通”，验证历史记录生成情况
    for _ in range(2):
        poco("com.hexin.plat.android:id/search_input").click()
        poco("com.hexin.plat.android:id/search_input").set_text("沪深港通")
        poco("com.hexin.plat.android:id/search_action").click()
        poco("com.hexin.plat.android:id/close_image").click()
    records = poco("com.hexin.plat.android:id/name")
    assert records[0].get_text() == "沪深港通", "第一个记录不是：沪深港通"
    assert len([record for record in records if record.get_text() == "沪深港通"]) == 1, "找到重复记录：沪深港通"


def test_history_record_updates(poco):
    """
用例名称
TC_推荐页_历史记录_收起与删除功能校验
用例id
1368838
    """
    # 检查并点击增加历史记录的按钮
    global new_count
    initial_records = poco("com.hexin.plat.android:id/name")
    initial_count = len(initial_records)
    if not exists(Template(r"搜索历史记录展开按钮.png", record_pos=(0.386, -0.413), resolution=(1080, 2340))):

        poco("com.hexin.plat.android:id/stock_name").click()
        # poco("com.hexin.plat.android:id/backButton").click()
        # if not poco("查看更多").exists():
        #     keyevent("BACK")
        back_findelement(poco(text="综合"))
        if poco("com.hexin.plat.android:id/ime_change_bar_close").exists():
            poco("com.hexin.plat.android:id/ime_change_bar_close").click()
            print("收起键盘")
        records = poco("com.hexin.plat.android:id/name")
        poco("com.hexin.plat.android:id/search_input").click()
        poco("com.hexin.plat.android:id/search_input").set_text("茅台")
        sleep(1.0)
        poco(text="搜索").click()
        poco("com.hexin.plat.android:id/close_image").click()
        records = poco("com.hexin.plat.android:id/name")

        # 5. 在搜索栏中输入“FTSE”，在联想结果中点击【搜索：FTSE】，查看历史搜索记录情况
        poco("com.hexin.plat.android:id/search_input").click()
        poco("com.hexin.plat.android:id/search_input").set_text("FTSE")
        sleep(1.0)
        poco("com.hexin.plat.android:id/search_action").click()
        poco("com.hexin.plat.android:id/close_image").click()
        records = poco("com.hexin.plat.android:id/name")

        # 6. 在搜索栏中输入不存在的股票代码“344678”，在联想结果中点击股票词条，查看历史搜索记录情况
        poco("com.hexin.plat.android:id/search_input").click()
        sleep(1.0)
        poco("com.hexin.plat.android:id/search_input").set_text("3446785555555")
        poco("com.hexin.plat.android:id/search_action").click()
        poco("com.hexin.plat.android:id/close_image").click()
        records = poco("com.hexin.plat.android:id/name")

        # 7. 在搜索栏中输入“决策”，在弹起键盘中点击【搜索】，查看历史搜索记录情况
        poco("com.hexin.plat.android:id/search_input").click()
        poco("com.hexin.plat.android:id/search_input").set_text("决策5555555")
        sleep(1.0)
        poco("com.hexin.plat.android:id/search_action").click()
        poco("com.hexin.plat.android:id/close_image").click()
        records = poco("com.hexin.plat.android:id/name")

        # 8. 在搜索栏中输入“快速选股”，在联想结果中点击【搜索：快速选股】，查看历史搜索记录情况
        poco("com.hexin.plat.android:id/search_input").click()
        poco("com.hexin.plat.android:id/search_input").set_text("快速选股222222")
        poco("com.hexin.plat.android:id/search_action").click()
        poco("com.hexin.plat.android:id/close_image").click()
        records = poco("com.hexin.plat.android:id/name")

        # 9. 在搜索栏中输入“沪深港通”，在联想结果中点击沪深港通宫格图标，查看历史搜索记录情况
        poco("com.hexin.plat.android:id/search_input").click()
        poco("com.hexin.plat.android:id/search_input").set_text("历史记录生成收起标签get")
        poco("com.hexin.plat.android:id/search_action").click()
        poco("com.hexin.plat.android:id/close_image").click()
        # 9. 在搜索栏中输入“沪深港通”，在联想结果中点击沪深港通宫格图标，查看历史搜索记录情况
        poco("com.hexin.plat.android:id/search_input").click()
        poco("com.hexin.plat.android:id/search_input").set_text("300033")
        poco("com.hexin.plat.android:id/search_action").click()
        poco("com.hexin.plat.android:id/close_image").click()

        # 10. 连续两次搜索“沪深港通”，验证历史记录生成情况
        for _ in range(1):
            poco("com.hexin.plat.android:id/search_input").click()
            poco("com.hexin.plat.android:id/search_input").set_text("沪深港通")
            poco("com.hexin.plat.android:id/search_action").click()
            poco("com.hexin.plat.android:id/close_image").click()
        records = poco("com.hexin.plat.android:id/name")

    if touch(Template(r"搜索历史记录展开按钮.png", record_pos=(0.386, -0.413), resolution=(1080, 2340))):
        sleep(2)  # 等待页面更新
        new_records = poco("com.hexin.plat.android:id/name")
        new_count = len(new_records)
        assert new_count > initial_count, f"历史记录未增加: initial_count={initial_count}, new_count={new_count}"

    # 检查并点击减少历史记录的按钮
    if touch(Template(r"tpl1721289433715.png", record_pos=(0.246, -0.006), resolution=(1080, 2340))):
        sleep(2)  # 等待页面更新
        updated_records = poco("com.hexin.plat.android:id/name")
        updated_count = len(updated_records)
        assert updated_count < new_count, f"历史记录未减少: new_count={new_count}, updated_count={updated_count}"

    # 点击删除图标并验证二次确认弹窗
    poco("com.hexin.plat.android:id/delete_btn").click()
    assert poco("com.hexin.plat.android:id/prompt_content").exists(), "二次确认弹窗未出现"
    assert poco("com.hexin.plat.android:id/prompt_content").get_text() == "确认清除全部历史记录吗？", "确认弹窗提示语不正确"

    # 点击取消按钮，验证历史记录未被删除
    poco("com.hexin.plat.android:id/cancel_btn").click()
    sleep(2)  # 等待页面更新
    records_after_cancel = poco("com.hexin.plat.android:id/name")
    assert len(records_after_cancel) == updated_count, "历史记录被错误删除"

    # 再次点击删除图标并验证二次确认弹窗
    poco("com.hexin.plat.android:id/delete_btn").click()
    assert poco("com.hexin.plat.android:id/prompt_content").exists(), "二次确认弹窗未出现"
    assert poco("com.hexin.plat.android:id/prompt_content").get_text() == "确认清除全部历史记录吗？", "确认弹窗提示语不正确"

    # 点击确认按钮，验证历史记录被删除
    poco("com.hexin.plat.android:id/ok_btn").click()
    sleep(2)  # 等待页面更新
    records_after_confirm = poco("com.hexin.plat.android:id/name")
    assert len(records_after_confirm) == 0, "历史记录未被清除"
