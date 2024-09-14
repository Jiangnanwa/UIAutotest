from airtest.core.api import *

from common.app_operation import back_findelement, stop_app_open_app
from common.function import refreshPage_find_to_elements, swipe_until, switch, homePageFindElements


def test_quanqiu_switch_stock(poco):
    # TC_行情tab-回归,用例id:731326
    stop_app_open_app("com.hexin.plat.android")
    sleep(3.0)
    homePageFindElements(poco(text="行情"), 1, poco)

    try:
        poco(text="行情", name="com.hexin.plat.android:id/title").click()
        poco(name="全球").click()
        poco(text="更多").click()
        poco(name="com.hexin.plat.android:id/stock_name").click()
        # 点击列表的第一支股票，切换100次
        stock_name = poco("com.hexin.plat.android:id/navi_title_text").get_text()
        right = poco("com.hexin.plat.android:id/navi_right_icon")
        cnt = 0
        for i in range(100):
            refreshPage_find_to_elements(1, right)
            right.click()
            sleep(1)
            stock_name0 = poco("com.hexin.plat.android:id/navi_title_text").get_text()
            print(stock_name0)
            cnt = cnt + 1

        poco("com.hexin.plat.android:id/backButton").click()
        poco(name="com.hexin.plat.android:id/title_bar_img").click()
    finally:
        hq = poco(text="行情", name="com.hexin.plat.android:id/title")
        print("finally恢复页面，回到行情页面")
        # 恢复页面，回到行情页面
        if not hq.exists():
            back_findelement(hq)
        if hq.exists():
            hq.click()
        elif poco("行情").exists():
            poco("行情").click()


def test_dp_switch_stock(poco):
    # TC_行情tab-回归,用例id:731326
    try:
        stop_app_open_app("com.hexin.plat.android")
        sleep(3.0)
        homePageFindElements(poco(text="行情"), 1, poco)
        poco(text="行情", name="com.hexin.plat.android:id/title").click()
        sleep(5.0)
        poco("A股").click()
        poco(text="大盘").click()
        poco("com.hexin.plat.android:id/queue_scroller").swipe([-0.0576, -0.3724])
        poco(text="更多").click()
        if poco("com.hexin.plat.android:id/tv_guide_pop_title").exists():
            poco("com.hexin.plat.android:id/tv_guide_pop_title").click()
        poco("com.hexin.plat.android:id/stock_name").click()
        # 点击列表的第一支股票，切换100次
        stock_name = poco("com.hexin.plat.android:id/navi_title_text").get_text()
        right = poco("com.hexin.plat.android:id/navi_right_icon")
        cnt = 0
        for i in range(100):
            refreshPage_find_to_elements(1, right)
            right.click()
            sleep(1)
            stock_name0 = poco("com.hexin.plat.android:id/navi_title_text").get_text()
            print(stock_name0)
            cnt = cnt + 1

        poco("com.hexin.plat.android:id/backButton").click()
        poco(name="com.hexin.plat.android:id/title_bar_img").click()
    finally:
        print("finally恢复页面，回到行情页面")
        hq = poco(text="行情", name="com.hexin.plat.android:id/title")

        # 恢复页面，回到行情页面
        if not hq.exists():
            back_findelement(hq)
        if hq.exists():
            hq.click()
        elif poco("行情").exists():
            poco("行情").click()


def test_bk_switch_stock(poco):
    # TC_行情tab-回归,用例id:731326
    try:
        poco(text="行情", name="com.hexin.plat.android:id/title").click()
        poco(name="A股").click()
        sleep(2.0)
        poco(nameMatches="板块|com.hexin.plat.android:id/bankuai").click()
        first_item = poco("com.hexin.plat.android:id/bankuai_name")
        bankuai_name = first_item.get_text()
        print(bankuai_name)
        # 点击第一个 view_bankuai_tablayout_item
        poco("com.hexin.plat.android:id/right_more").click()
        sleep(2.0)

        poco(text=bankuai_name).click()
        # 如果弹出 i_know 弹窗，则点击
        if poco("com.hexin.plat.android:id/i_know").exists():
            poco("com.hexin.plat.android:id/i_know").click()
            sleep(2)  # 等待页面加载完成
        # 点击列表的第一支股票，切换100次
        stock_name = poco("com.hexin.plat.android:id/navi_title_text").get_text()
        right = poco("com.hexin.plat.android:id/navi_right_icon")
        cnt = 0
        stocklist = []
        for i in range(100):
            refreshPage_find_to_elements(1, right)
            right.click()
            sleep(1)
            stock_name0 = poco("com.hexin.plat.android:id/navi_title_text").get_text()
            print(stock_name0)
            stocklist.append(stock_name0)
            cnt = cnt + 1
        print(stocklist)
        set_stock_list = set(stocklist)
        if not len(stocklist) == len(set_stock_list):
            raise AssertionError(f"存在重复的股票,切换股票获取到的数据{stocklist},去重后的数据{set_stock_list}")

        poco("com.hexin.plat.android:id/backButton").click()
        poco(name="com.hexin.plat.android:id/title_bar_img").click()
    finally:
        hq = poco(text="行情", name="com.hexin.plat.android:id/title")
        print("finally恢复页面，回到行情页面")
        # 恢复页面，回到行情页面
        if not hq.exists():
            back_findelement(hq)
        if hq.exists():
            hq.click()
        elif poco("行情").exists():
            poco("行情").click()


def test_qita_switch_stock(poco):
    stop_app_open_app("com.hexin.plat.android")
    sleep(3.0)
    homePageFindElements(poco(text="行情"), 1, poco)
    try:
        poco(text="行情", name="com.hexin.plat.android:id/title").click()
        swipe_until(poco(text="其他"), poco(text="期货"), [-0.5, 0])
        poco(text="其他").click()
        swipe_until(poco(text="个股"), poco(text="全球市场"), [0, -0.5])
        poco(text="上证A股").click()
        poco(name="android.view.View").click()
        switch(5, poco)
        poco("com.hexin.plat.android:id/backButton").click()
        poco(name="com.hexin.plat.android:id/title_bar_img").click()
    finally:
        hq = poco(text="行情", name="com.hexin.plat.android:id/title")
        print("finally恢复页面，回到行情页面")
        # 恢复页面，回到行情页面
        if not hq.exists():
            back_findelement(hq)
        if hq.exists():
            hq.click()
        elif poco("行情").exists():
            poco("行情").click()
