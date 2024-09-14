from airtest.core.android import Android
from airtest.core.api import *

from common.app_operation import *
from common.function import *

#用例id 618099
from test_case.Timesharing_kline.guanliantiao_tiaozhuan.test_Agu_kezhuanzai_tiaozhuan import go_to_initial_page

"""
-------------------------------------------------
   File Name：    
   Description :TC_深圳ETF关联条跳转
   Author : wangsutong
   CreateDate：2024/03/07  
   用例id:618099
-------------------------------------------------
"""

def test_shenzhengETF_tiaozhuan_jijin_step1(poco):
    """
    -------------------------------------------------
       File Name：
       Description :TC_深圳ETF关联条跳转
       Author : wangsutong
       CreateDate：2024/03/07
       用例id:618099
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
        poco(desc="搜索输入框").set_text("159813")
        sleep(10)
        poco(text="半导体ETF").click()
        sleep(5)
        if poco("com.hexin.plat.android:id/i_know").exists():
            poco("com.hexin.plat.android:id/i_know").click()
        sleep(10)
        poco("com.hexin.plat.android:id/feeder_fund_info").click()
        # poco("detailTab").click()
        # poco("detailTab").click()
        # result_title=poco("com.hexin.plat.android:id/navi_title_text").get_text()
        if(poco(text="鹏华国证半导体芯片ETF联接C 012970")):
            assert True
        else:
            assert False
        poco("com.hexin.plat.android:id/left_btn").click()
        sleep(5)
        str=poco("com.hexin.plat.android:id/navi_title_text").get_text()
        assert str == "半导体ETF", "关联基金跳转返回ETF分时页面失败"
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

