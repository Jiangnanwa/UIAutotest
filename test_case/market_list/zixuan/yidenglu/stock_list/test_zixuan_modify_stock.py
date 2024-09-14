#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    test_zixuan_modify_stock.py
   Description :
   Author : chenqiyue
   CreateDate：2024/03/06  用例id:
-------------------------------------------------
"""
import json

import pytest
import requests


@pytest.mark.skip(reason="服务器未调试通过")
def test_long_press_and_edit_group_assignment(poco):
    """
    用例名称
    TC_自选分组_自选股竖屏编辑分组控件删除股票
    用例id
    1262076
    """
    poco(text="沪深京").click()
    poco(nameMatches=".*#.*#.*").long_click()
    poco(text="编辑分组").click()
    stock_text = poco("com.hexin.plat.android:id/tv_stock_name_code").get_text()
    stock_name = stock_text.split()[0]
    stock_code = stock_text.split()[1]

    print(stock_name)
    poco("com.hexin.plat.android:id/stock_checked_iv").click()
    poco("com.hexin.plat.android:id/btn_complete").click()
    if poco(stock_name).exists():
        raise AssertionError(f"长按编辑-编辑分组-取消勾选自选股-自选股依然存在{stock_name}")
    url = 'http://ugc.10jqka.com.cn/optdata/selfstock/open/api/v1/query?extra_fields=tops'
    url2 = 'http://ugc.10jqka.com.cn/optdata/selfstock/open/api/v1/add'
    headers = {
        "cookie": 'v=A5CV01TZwfsmI53_Uz0zyLI8ZdTiWXSjlj3Ip4phXOu-xT_PMmlEM-ZNmDTZ; escapename=lwtest1149; ticket=3ccaf41ed0162694b86d2d72c8fb1bcf; u_name=lwtest1149; user=MDpsd3Rlc3QxMTQ5OjpOb25lOjUwMDo1Mjc3NTM0NzI6NywxMTExMTExMTExMSw0MDs0NCwxMSw0MDs2LDEsNDA7NSwxLDQwOzEsMTAxLDQwOzIsMSw0MDszLDEsNDA7NSwxLDQwOzgsMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDEsNDA7MTAyLDEsNDA6Ojo6NTE3NzUzNDcyOjE3MDk3MzAxMzI6OjoxNTg1NzA3OTAwOjI2Nzg0MDA6MDoxODAyOGM1NDM3NDA4YTdlYjRjMTE4NTUyMDNiNjJkNjg6OjA%3D; user_status=0; userid=517753472; IFUserCookieKey={"userid":"517753472","escapename":"lwtest1149"}'
    }

    # 发送GET请求
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    selfstock = json_data['data']['tops']
    first_data = selfstock.split('|')
    if stock_code in first_data:
        raise ValueError("删除失败：股票代码已存在于第一个数据中")
    print("删除成功")
    print(selfstock)
    # POST数据
    data = {
        'version': '999999',
        'from': 'sjcg_ios',
        'selfstock': '300033|600000|,33|17|'
    }
    response = requests.post(url2, data=data, headers=headers)
    print(response)
