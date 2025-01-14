# 用于在首页打开产品页面
from time import sleep
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

def Open_product(poco,url):
    poco("com.hexin.plat.android:id/text_switcher").wait().click()
    try:
        poco("com.hexin.plat.android:id/search_input").set_text("MYHEXIN")
    except Exception as e:
        print(e, "没找到输入框 ")
        poco("com.hexin.plat.android:id/search_input").refresh()
        poco("com.hexin.plat.android:id/search_input").click()
    sleep(5)
    # if poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").exists():
    #     print("仅使用期间允许")
    poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
    # if poco("com.android.permissioncontroller:id/permission_allow_always_button").exists():
    #     print("仅使用期间允许")
    #     poco("com.android.permissioncontroller:id/permission_allow_always_button").click()
    if poco("com.hexin.plat.android:id/dialog_layout").exists():
        poco(text="CLIENT协议跳转").wait().click()
        poco("com.hexin.plat.android:id/et_client").click()
        poco("com.hexin.plat.android:id/et_client").set_text(url)
        poco("com.hexin.plat.android:id/cancel_btn").wait().click()