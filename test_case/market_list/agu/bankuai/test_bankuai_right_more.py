#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_bankuai_right_more 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/06  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import keyevent, sleep
from common.function import find_element_within_timeout, scroll_element_below_another_element, scroll_element_into_view, \
    find_elements_with_same_x_position
from common.sort_operations import sort_elements_by_percentage


@pytest.mark.parametrize("bk_name,tab,num",
                         [("概念板块", "涨速", 4), ("行业板块", "涨幅", 1), ("风格板块", "量比", 1), ("地域板块", "涨幅", 1)])
def test_bankuai_right_more_desc(poco, bk_name, tab, num):
    """
        用例id:1300790
        TC_行业板块_跳转板块页面_
        1300810
        TC_概念板块_跳转板块页面_涨速tab（回归）
        1300830
        TC_风格板块_跳转板块页面_量比tab（回归）
        1300847
        TC_地域板块_跳转板块页面_涨幅tab（回归）
        步骤:行情-A股-板块-{bk_name}-{tab}降序
    """
    # 调用函数并指定要查找的元素文本和超时时间
    find_element_within_timeout(poco(text=bk_name), timeout=20)
    # 把对应板块移动到板块tab下方100
    bankuaitab = poco("com.hexin.plat.android:id/bankuai")
    # 拖拽更多，校验目标元素与参考元素小于一定的值
    scroll_element_below_another_element(poco(text=bk_name), bankuaitab, poco("com.hexin.plat.android:id/right_more"))
    sleep(2.0)
    #   在这里进行上滑操作，使目标元素展示出来
    scroll_element_into_view(poco(text=bk_name), max_swipe_attempts=10)
    # 获取更多按钮元素
    right_more = poco("com.hexin.plat.android:id/right_more")
    # 记录位置
    industry_pos_initial = right_more.get_position()
    # 表头值点击
    tab_name = poco(text=tab).get_text()
    print("操作路径:", bk_name, "-点击表头:", tab_name, "-更多")
    # 如果不是涨幅表头需要点击，因为列表默认涨幅降序
    if tab_name != "涨幅":
        poco(text=tab).click()
    # 点击右上角更多按钮
    right_more.click()
    # 获取所有具有name属性存在%和#的元素
    elements_with_name = find_elements_with_same_x_position(poco, ".*%", attr_name='pos')
    # 一组含有%的数据,遍历每一个数据去掉%,进行升降序排列
    sort_elements_by_percentage(elements_with_name, sorting_type="desc")
    # 返回上一级
    keyevent("BACK")
    # 获取返回后的行业板块元素位置坐标
    industry_pos_final = right_more.get_position()
    # 检查位置坐标是否相同
    if industry_pos_initial == industry_pos_final:
        print("返回前后坐标未变化，验证通过")
    else:
        print("操作路径:", bk_name, "-点击表头", tab_name, "-更多-返回上一级")

        raise AssertionError("返回前后坐标发生了变化，验证失败")


@pytest.mark.parametrize("bk_name,tab,num",
                         [("概念板块", "涨速", 4), ("行业板块", "涨幅", 1), ("风格板块", "量比", 1), ("地域板块", "涨幅", 1)])
def test_bankuai_right_more_asc(poco, bk_name, tab, num):
    """
        用例id:1300790
        TC_行业板块_跳转板块页面_
        1300810
        TC_概念板块_跳转板块页面_涨速tab（回归）
        1300830
        TC_风格板块_跳转板块页面_量比tab（回归）
        1300847
        TC_地域板块_跳转板块页面_涨幅tab（回归）
        步骤:行情-A股-板块-{bk_name}-{tab}升序
    """
    # 调用函数并指定要查找的元素文本和超时时间
    find_element_within_timeout(poco(text=bk_name), timeout=20)
    # 把对应板块移动到板块tab下方100
    bankuaitab = poco("com.hexin.plat.android:id/bankuai")
    scroll_element_below_another_element(poco(text=bk_name), bankuaitab, poco("com.hexin.plat.android:id/right_more"))
    sleep(2.0)
    #   在这里进行上滑操作，使目标元素展示出来
    scroll_element_into_view(poco(text=bk_name), max_swipe_attempts=10)
    right_more = poco("com.hexin.plat.android:id/right_more")
    # 记录位置
    industry_pos_initial = right_more.get_position()
    # 表头值
    tab_name = poco(text=tab).get_text()
    print("操作路径:", bk_name, "-点击表头:", tab_name, "-更多")
    poco(text=tab).click()
    if tab_name != "涨幅":
        poco(text=tab).click()
    # 点击右上角更多按钮
    right_more.click()
    # 获取所有具有name属性存在%和#的元素
    elements_with_name = find_elements_with_same_x_position(poco, ".*%", attr_name='pos')
    sort_elements_by_percentage(elements_with_name, sorting_type="desc")

    # 返回上一级
    keyevent("BACK")

    # 获取返回后的行业板块元素位置坐标
    industry_pos_final = right_more.get_position()

    # 检查位置坐标是否相同
    if industry_pos_initial == industry_pos_final:
        print("返回前后坐标未变化，验证通过")
    else:
        print("操作路径:", bk_name, "-点击表头", tab_name, "-更多-返回上一级")

        raise AssertionError("返回前后坐标发生了变化，验证失败")


@pytest.mark.parametrize("bk_name,tab,num,sort,tv_item",
                         [("商品联动", "涨幅", 1, "desc", "com.hexin.plat.android:id/stock_zhangfu"),
                          ("商品联动", "涨幅", 1, "asc", "com.hexin.plat.android:id/stock_zhangfu")
                          ])
def test_bankuai_right_more_spld_sort(poco, bk_name, tab, num, sort, tv_item):
    """
    调试时执行的手机为红米k60
    TC_商品联动_跳转商品联动二级页面_期股联动（回归）
    用例id
    1300866
    """
    # 调用函数并指定要查找的元素文本和超时时间
    try:
        find_element_within_timeout(poco(text=bk_name), timeout=200)
    except Exception as e:
        print(f"没有找到{bk_name}")
        # 继续滑动
        find_element_within_timeout(poco(text=bk_name), timeout=200)
    # 把对应板块移动到板块tab下方100
    bankuaitab = poco("com.hexin.plat.android:id/bankuai")
    scroll_element_below_another_element(poco(text=bk_name), bankuaitab, poco(text=bk_name))
    sleep(2.0)
    #   在这里进行上滑操作，使目标元素展示出来
    scroll_element_into_view(poco(text=bk_name), max_swipe_attempts=10)
    right_more = poco("com.hexin.plat.android:id/right_more")
    # 记录位置
    industry_pos_initial = right_more.get_position()
    # 表头值
    tab_name = poco(text=tab).get_text()
    print("操作路径:", bk_name, "-点击表头:", tab_name, "-更多")
    # 点击涨幅表头
    if sort == "asc":
        poco(text=tab).click()
    # 点击右上角更多按钮
    right_more.click()
    sort_elements_by_percentage(poco(tv_item), sorting_type=sort)
    # 返回上一级
    keyevent("BACK")
    # 获取返回后的行业板块元素位置坐标
    industry_pos_final = right_more.get_position()
    # 检查位置坐标是否相同
    if industry_pos_initial == industry_pos_final:
        print("返回前后坐标未变化，验证通过")
    else:
        print("操作路径:", bk_name, "-点击表头", tab_name, "-更多-返回上一级")

        raise AssertionError("返回前后坐标发生了变化，验证失败")
    sort_elements_by_percentage(poco(tv_item), sorting_type=sort)
