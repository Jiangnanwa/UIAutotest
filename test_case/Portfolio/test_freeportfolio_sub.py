# -*- encoding=utf8 -*-
# 华为mate40 pro
from time import sleep

from page.PortfolioBase import PortfolioPage



class TestFreePortfolio(PortfolioPage):
    def test_01(self,poco):
        poco("com.hexin.plat.android:id/first_page_search_layout_container").long_click()
        # if poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").exists():
        #     poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").wait().click()
        # # 打开小白球
        poco(text="CLIENT协议跳转").click()
        poco("com.hexin.plat.android:id/et_client").click()
        poco("com.hexin.plat.android:id/et_client").set_text(
        "https://t.10jqka.com.cn/pkgfront/tgService.html?type=portfolio&id=8317")
        sleep(2)
        if poco.product_name.exists():
            print("seccess")
        else:
            print("fail")
