from airtest.core.android import Android
from airtest.core.api import *

from common.app_operation import *
from common.function import *
"""
-------------------------------------------------
   File Name：    
   Description :TC_A股页面可转债关联条跳转
   Author : wangsutong
   CreateDate：2024/05/07  
   用例id:615573
-------------------------------------------------
"""


def go_to_initial_page(poco):
    max_attempts = 10
    attempt = 0
    while attempt < max_attempts:
        home_button = poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("首页").child("com.hexin.plat.android:id/icon")
        if home_button.exists():
            home_button.click()
            print("主页按钮已点击")
            break
        else:
            # 如果没有找到主页按钮，发送BACK键尝试返回
            keyevent("BACK")
            print("发送BACK键")
            attempt += 1



def test_kezhuanzai_tiaozhuan(poco):
    """
    -------------------------------------------------
       File Name：
       Description :TC_A股页面可转债关联条跳转
       Author : wangsutong
       CreateDate：2024/05/07
       用例id:615573
    -------------------------------------------------
    """

    try:
        sleep(5)
        try:
            # 增加显式等待
            poco("com.hexin.plat.android:id/text_switcher").wait_for_appearance(10)
            poco("com.hexin.plat.android:id/text_switcher").click()
        except Exception as e:
            print(e)
            keyevent("BACK")
            poco("com.hexin.plat.android:id/text_switcher").click()
        sleep(10)
        poco(desc="搜索输入框").set_text("603501")
        sleep(5)
        poco(text="韦尔股份").click()
        sleep(10)
        if poco("com.hexin.plat.android:id/i_know").exists():
            poco("com.hexin.plat.android:id/i_know").click()

        if poco("com.hexin.plat.android:id/bond_stock_name").exists():
            poco("com.hexin.plat.android:id/bond_stock_name").click()
            print("关联条已点击")

        result1=poco("com.hexin.plat.android:id/navi_title_text").get_text()
        sleep(10)
        assert result1=="韦尔转债"
        poco("com.hexin.plat.android:id/backButton").click()
        sleep(10)
        str=poco("com.hexin.plat.android:id/navi_title_text").get_text()
        assert str == "韦尔股份", "可转债跳转返回A股分时页面失败"
    finally:
        go_to_initial_page(poco)
        # 处理新手开户弹窗
        if poco(name="android.widget.Image").exists():
            poco(nameMatches="android.widget.Image")[0].click()
        image_template = Template(r"tpl1720858284488.png")

        # 查找图像并点击
        image_template = Template(r"tpl1720858284488.png")

        # 查找图像并点击
        if exists(image_template):
            touch(Template(r"tpl1720858284488.png"))
            sleep(5)
            touch(Template(r"tpl1720858297840.png"))
            sleep(5)
            touch(Template(r"tpl1720862719944.png", record_pos=(-0.002, 0.891), resolution=(1176, 2400)))

