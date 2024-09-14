from airtest.core.android import Android
from airtest.core.api import *

from common.app_operation import *
from common.function import *
from test_case.Timesharing_kline.guanliantiao_tiaozhuan.test_Agu_kezhuanzai_tiaozhuan import go_to_initial_page

"""
-------------------------------------------------
   File Name：    
   Description :TC_可转债页面A股关联条跳转
   Author : wangsutong
   CreateDate：2024/05/07  
   用例id:615577
-------------------------------------------------
"""
def test_kezhuanzai_tiaozhuanAgu(poco):
    """
    -------------------------------------------------
       File Name：
       Description :TC_可转债页面A股关联条跳转
       Author : wangsutong
       CreateDate：2024/05/07
       用例id:615577
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
        poco(desc="搜索输入框").set_text("113616")
        sleep(5)
        poco(text="韦尔转债").click()
        sleep(5)
        # poco(ext="跟踪指数").click()
        if poco("com.hexin.plat.android:id/i_know").exists():
            poco("com.hexin.plat.android:id/i_know").click()
        sleep(10)
        poco("com.hexin.plat.android:id/recycler_view").click()
        # result_title=poco("com.hexin.plat.android:id/navi_title_text").get_text()
        result1=poco("com.hexin.plat.android:id/navi_title_text").get_text()
        assert result1=="韦尔股份"
        poco("com.hexin.plat.android:id/backButton").click()
        str=poco("com.hexin.plat.android:id/navi_title_text").get_text()
        assert str == "韦尔转债", "A股跳转返回可转债分时页面失败"

        # fenshixiangqingye_find_elements(elem, num, poco)
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
