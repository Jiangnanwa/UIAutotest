#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_zijin_list_jump_fenshi 
   Description :
   Author : chenqiyue
   CreateDate：2024/03/11  用例id:
-------------------------------------------------
"""
import pytest
from airtest.core.api import sleep

from common.app_operation import stop_app_open_app, back_findelement
from common.function import homePageFindElements


@pytest.mark.parametrize("final_teardown_yidenglu", [{}], indirect=True)
@pytest.mark.parametrize("testcase_id,biaotou,index,tab_name",
                         [("1337460", "最新", 2, "自选"), ("1337461", "涨幅", 3, "自选"), ("1337462", "主力净流入", 1, "自选"),
                          ("1337486", "主力净流入", 1, "沪深")])
def test_zijin_zixuan_list_biaotou_paixu(poco, testcase_id, biaotou, index, tab_name):
    """
    看资金-自选列表排序
    1337461
    TC_看资金_自选列表排序_竖屏_涨跌幅
    1337460
    TC_看资金_自选列表排序_竖屏_最新
    1337462
    TC_看资金_自选列表排序_竖屏_主力净流入
    1337486
    TC_看资金_沪深列表排序_竖屏_主力净流入
    """
    if tab_name == "沪深":
        # 如果是沪深,需要重启 因为排序记忆不好判断当前是什么排序
        stop_app_open_app("com.hexin.plat.android")
        sleep(5.0)
        # back_findelement(poco(text="自选", name="com.hexin.plat.android:id/title"))
        zixuan = poco(text="自选", name="com.hexin.plat.android:id/title")
        homePageFindElements(zixuan, 1, poco)
        back_findelement(zixuan)
        if zixuan.exists():
            zixuan.click()
        elif poco("自选").exists():
            poco("自选").click()
        poco(text="资金").click()
        # 点击沪深tab
        poco(text=tab_name).click()
    else:
        # 如果不是沪深则直接点击资金
        poco(text="资金").click()
    sleep(2.0)
    print(biaotou)
    # 如果取消排序存在,取消排序恢复默认排序
    if poco(text="取消排序").exists():
        poco(text="取消排序").click()
    # 点击表头,沪深tab下默认是主力净流入降序,没有取消排序按钮,所有在测试降序时,如果是沪深下就不用再次点击表头
    if not tab_name == "沪深":
        poco(text=biaotou).click()
    # 定义空列表
    biaotou_shuju = []
    # 获取列表数据
    zixuanlist = poco(nameMatches=".*#.*")
    # 遍历列表数据找到被排序的数据
    for i in zixuanlist:
        name = i.get_name()
        print(i)
        shuzhi = name.split('#')
        print("转换前数据", shuzhi[index])
        # 如果获取的股票数据试用#分割后的列表是大于1
        if len(shuzhi) > 1:
            # 如果包含百分比符号
            if '%' in shuzhi[index]:
                biaotou_values = shuzhi[index].replace('%', '')
            # 如果包含“万”
            elif '万' in shuzhi[index]:
                biaotou_values = float(shuzhi[index].replace('万', '')) * 10000
            # 如果包含“亿”
            elif '亿' in shuzhi[index]:
                biaotou_values = float(shuzhi[index].replace('亿', '')) * 100000000
            else:
                biaotou_values = shuzhi[index]
            # 将处理后的数据添加到数组中
        biaotou_shuju.append(biaotou_values)
    print(biaotou_shuju)
    # 将获取的数据按照字符串降序排列

    sorted_values = sorted(biaotou_shuju, reverse=True, key=float)

    # 校验获取的数据是否是降序排列
    if biaotou_shuju == sorted_values:
        print("split_values", biaotou_shuju)
        print("sorted_values", sorted_values)
        print(f"获取的数据是降序排列,客户端展示{biaotou_shuju},计算机排序{sorted_values}")
    else:
        print("split_values", biaotou_shuju)
        print("sorted_values", sorted_values)
        print(f"获取的数据不是降序排列,客户端展示{biaotou_shuju},计算机排序{sorted_values}")
        raise AssertionError(f"获取的数据不是降序排列,客户端展示{biaotou_shuju},计算机排序{sorted_values}")

    # 校验升序
    poco(text=biaotou).click()
    biaotou_shuju = []
    zixuanlist = poco(nameMatches=".*#.*")
    for i in zixuanlist:
        name = i.get_name()
        print(i)
        shuzhi = name.split('#')
        # 如果获取的股票数据试用#分割后的列表是大于1
        if len(shuzhi) > 1:
            # 如果包含百分比符号
            if '%' in shuzhi[index]:
                biaotou_values = shuzhi[index].replace('%', '')
            # 如果包含“万”
            elif '万' in shuzhi[index]:
                biaotou_values = float(shuzhi[index].replace('万', '')) * 10000
            # 如果包含“亿”
            elif '亿' in shuzhi[index]:
                biaotou_values = float(shuzhi[index].replace('亿', '')) * 100000000
            else:
                biaotou_values = shuzhi[index]
            # 将处理后的数据添加到数组中
        biaotou_shuju.append(biaotou_values)
    print(biaotou_shuju)
    # 将获取的数据按照字符串降序排列
    # 检查文本值是否按照升序排列
    sorted_values = sorted(biaotou_shuju, reverse=False, key=float)
    print(sorted_values)
    if biaotou_shuju == sorted_values:
        print(f"文本值按照升序排列,客户端展示{biaotou_shuju},计算机排序{sorted_values}")
    else:
        print("文本值未按照升序排列")
        raise AssertionError(f"文本值未按照升序排列,客户端展示{biaotou_shuju},计算机排序{sorted_values}")
