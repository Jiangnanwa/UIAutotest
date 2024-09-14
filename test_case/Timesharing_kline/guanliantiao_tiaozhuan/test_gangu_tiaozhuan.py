from airtest.core.android import Android
from airtest.core.api import *

from common.app_operation import *
from common.function import *
from test_case.Timesharing_kline.guanliantiao_tiaozhuan.test_Agu_kezhuanzai_tiaozhuan import go_to_initial_page

"""
-------------------------------------------------
   File Name：    
   Description :TC_TC_港股页面A股关联条跳转
   Author : wangsutong
   CreateDate：2024/03/07  
   用例id:610942
-------------------------------------------------
"""

def test_gangu_tiaozhuan(poco):
    """
    -------------------------------------------------
       File Name：
       Description :TC_TC_港股页面A股关联条跳转
       Author : wangsutong
       CreateDate：2024/03/07
       用例id:610942
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
        poco(desc="搜索输入框").set_text("600660")
        sleep(5)
        poco(text="福耀玻璃").wait(10).click()
        sleep(10)
        if poco("com.hexin.plat.android:id/i_know").exists():
            poco("com.hexin.plat.android:id/i_know").click()
        sleep(10)
        poco("com.hexin.plat.android:id/recycler_view").click()
        result_title=poco("com.hexin.plat.android:id/navi_title_text").get_text()
        assert result_title=="福耀玻璃","A股页面港股关联条跳转失败"
        sleep(5)
        poco("com.hexin.plat.android:id/fenshi_headline_view").click()
        if( poco(text="港股通")):
            poco(text="港股通").click()
        else:
            assert False
        sleep(5)
        if( poco(text="HK3606")):
            poco("com.hexin.plat.android:id/title_bar_img").click()
        else:
            assert False
        poco("com.hexin.plat.android:id/backButton").click()
        result_title = poco("com.hexin.plat.android:id/navi_title_text").get_text()
        assert result_title == "福耀玻璃", "A股页面港股关联条跳转失败"
        sleep(5)
        poco("com.hexin.plat.android:id/fenshi_headline_view").click()
        if (poco(text="沪股通")):
            poco(text="沪股通").click()
        else:
            assert False
        sleep(5)
        if (poco(text="600660")):
            poco("com.hexin.plat.android:id/title_bar_img").click()
        else:
            assert False
    finally:
        go_to_initial_page(poco)
        sleep(10)
        image_template = Template(r"tpl1720858284488.png")

        # 查找图像并点击
        if exists(image_template):
            touch(Template(r"tpl1720858284488.png"))
            sleep(5)
            touch(Template(r"tpl1720858297840.png"))
            sleep(5)
            touch(Template(r"tpl1720862719944.png", record_pos=(-0.002, 0.891), resolution=(1176, 2400)))
