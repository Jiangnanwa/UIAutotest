#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    add_stock_whole_market
   Description :
   Author : chenqiyue
   CreateDate：2023/08/17  用例id:
-------------------------------------------------
"""

from airtest.core.api import sleep


def test_add_stock(poco):
    # login_by_password(login_account, login_password, 'com.hexin.plat.android', poco)
    stocks = ["1A0001", "600519", "900953", "122071", "510150", "300308", "399001", "300033", "200596", "128130",
              "159968", "AUUSDO", "c2311", "CF2401", "ag2310", "899050", "430047", "881101", "884002", "000088",
              "nr8888", "y8888", "AP8888", "AU100", "N225", "865018", "871016", "841001", "USDCNH", "HKDJPY", "USDEUR",
              "USDCNM", "JPYCNY", "480015", "HSI999", "TCH999", "930701", "IF9999", "899301", "400002",
              "420016", "820002", "GSK", "GSK", "BABA", "AAMC", "AFIF", "HSI", "HK0001", "HK8001", "K10784", "HK0405",
              "HK4239", "K", "AAPL", "ABEO", "TPXG", "CN0Y", "AUUSDO", "BRN0Y", "10005475", "005001",
              "NDX", "TIVC", "VCP", "si8888", "ADDYY", "lc2401C190E", "K50830"]
    print(len(stocks))
    # poco(text="自选").click()
    # poco("com.hexin.plat.android:id/slidingmenu_editview").click()
    # poco("com.hexin.plat.android:id/select_all_check_box_stocks").click()
    # poco("com.hexin.plat.android:id/selfcode_delete").click()
    # poco("com.hexin.plat.android:id/ok_btn")
    # keyevent('BACK')
    # poco("com.hexin.plat.android:id/iv_add_stock").click()
    stock_search_editview = poco("com.hexin.plat.android:id/stock_search_editview")
    tv_add_stock = poco("com.hexin.plat.android:id/tv_add_stock")

    for stock in stocks:
        stock_search_editview.click()
        print(stock)
        stock_search_editview.set_text(stock)
        sleep(1.0)
        if tv_add_stock.exists():
            tv_add_stock.click()
        if poco(text="股票代码不存在").exists():
            print(f"股票代码不存在{stock}")
