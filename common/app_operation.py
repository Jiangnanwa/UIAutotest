#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    app_operation 
   Description :
   Author : chenqiyue
   CreateDate：2023/03/10  用例id:
-------------------------------------------------
"""



# 函数定义
def stop_app_open_app(appPackage):
    """
    停止指定的应用程序，然后重新启动该应用程序，并指定启动的活动。

    Args:
        appPackage (str): 应用程序包名。

    Returns:
        无
    """
    from airtest.core.api import stop_app, start_app
    stop_app(appPackage)
    start_app(appPackage, activity="LogoEmptyActivity")



def Slide_up_speed(poco, PPI, second, Repetitions=20):
    from airtest.core.api import swipe
    from airtest.core.api import device
    '''
    获取手机分辨率
    设备像素是1080x2340，根据像素密度的计算公式，设备的像素密度为：
    Density = sqrt((1080^2 + 2340^2) / (6.18^2)) = 480 ppi
    设备像素是1080x2340，根据像素密度的计算公式，设备的像素密度为：`dpi`为480像素每英寸  高度（毫米）= 高度（像素）/ PPI × 25.4
    在durs内上划1个屏幕 上为负
    '''
    if second == 600:
        sudu = "快速"
    if second == 300:
        sudu = "正常"
    w, h = device().get_current_resolution()  # 获取手机分辨率
    # 设备像素是1080x2340，根据像素密度的计算公式，设备的像素密度为：
    # Density = sqrt((1080^2 + 2340^2) / (6.18^2)) = 480 ppi
    # 根据荣耀8X的规格，其像素密度为397 PPI
    # 设备像素是1080x2340，根据像素密度的计算公式，设备的像素密度为：`dpi`为480像素每英寸  高度（毫米）= 高度（像素）/ PPI × 25.4
    mm_size = h / PPI * 25.4
    print(h)
    print(mm_size)
    dur = mm_size / second
    for i in range(Repetitions):
        swipe((0.8 * w, 0.8 * h), vector=(0, -1), duration=dur)  # 在durs内上划1个屏幕 上为负
        print(sudu, "向上滑动第", i, "次")


def Slide_down_speed(poco, PPI, second, Repetitions=10):
    from airtest.core.api import swipe
    from airtest.core.api import device
    '''
    获取手机分辨率
    设备像素是1080x2340，根据像素密度的计算公式，设备的像素密度为：
    Density = sqrt((1080^2 + 2340^2) / (6.18^2)) = 480 ppi
    设备像素是1080x2340，根据像素密度的计算公式，设备的像素密度为：`dpi`为480像素每英寸  高度（毫米）= 高度（像素）/ PPI × 25.4
    在durs内上划1个屏幕 上为负
    '''
    w, h = device().get_current_resolution()  # 获取手机分辨率
    # 设备像素是1080x2340，根据像素密度的计算公式，设备的像素密度为：
    # Density = sqrt((1080^2 + 2340^2) / (6.18^2)) = 480 ppi
    # 根据荣耀8X的规格，其像素密度为397 PPI
    # 设备像素是1080x2340，根据像素密度的计算公式，设备的像素密度为：`dpi`为480像素每英寸  高度（毫米）= 高度（像素）/ PPI × 25.4
    mm_size = h / PPI * 25.4
    print(h)
    print(mm_size)
    dur = mm_size / second
    for i in range(Repetitions):
        swipe((0.7 * w, 0.7 * h), vector=(0, 1), duration=dur)  # 在durs内上划1个屏幕 上为负
        print("向下滑动第", i, "次")


def Start_Performance_Test(poco):
    if poco("com.hexin.plat.android:id/close_button").exists():
        poco("com.hexin.plat.android:id/close_button").click()
    try:
        poco(name="com.hexin.plat.android:id/text_switcher", type="android.widget.TextSwitcher").wait().click()
    except Exception as e:
        print(e, "没找到输入框")
        # 元素刷新
        poco(name="com.hexin.plat.android:id/text_switcher", type="android.widget.TextSwitcher").refresh()
        poco(name="com.hexin.plat.android:id/text_switcher", type="android.widget.TextSwitcher").click()
    # poco(text="搜索").wait().click()
    # if poco("com.hexin.plat.android:id/search_input").exists():
    #     poco("com.hexin.plat.android:id/search_input").set_text("MYHEXIN")
    try:
        poco("com.hexin.plat.android:id/search_input").set_text("MYHEXIN")
    except Exception as e:
        print(e, "没找到输入框 ")
        poco("com.hexin.plat.android:id/search_input").refresh()
        poco("com.hexin.plat.android:id/search_input").click()

    if poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").exists():
        print("仅仅在试用期间允许")
        poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
    if poco("com.android.permissioncontroller:id/permission_allow_always_button").exists():
        print("仅仅在试用期间允许")
        poco("com.android.permissioncontroller:id/permission_allow_always_button").click()
    if poco(text="仅使用期间允许").exists():
        print("仅使用期间允许")
        poco(text="仅使用期间允许").click()
    if poco(text="允许").exists():
        print("始终允许")
        poco(text="允许").click()
    if poco(text="打开或者关闭小白球").exists():
        poco(text="打开或者关闭小白球").click()

    if poco(text="打开或者关闭小白球").exists():
        pass
    else:

        ths = poco(text="同花顺")
        swipe_up_findelement(ths)
        ths.click()
        poco("android:id/switch_widget").wait().click()
    back_findelement(poco(text="行情"))


def Show_Performance_Test(poco):
    poco("com.hexin.plat.android:id/text_switcher").wait().click()
    try:
        poco(text="搜索").wait().click()
    except Exception as e:
        print(e, "没有获取到搜索按钮,没有点击")
    try:
        poco("com.hexin.plat.android:id/search_input").set_text("MYHEXIN")

    except Exception as e:
        print(e, "没有输入MYHEXIN ")
    if poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").exists():
        poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").wait().click()
    # 打开小白球

    poco(text="显示性能数据").wait().click()
    a = poco("android.widget.TextView").get_text()
    print(a)


def swipe_up_findelement(ele):
    from airtest.core.api import swipe
    from airtest.core.api import device
    w, h = device().get_current_resolution()  # 获取手机分辨率
    print(w, h)

    i = 0
    while i < 50:
        swipe((0.5 * w, 0.8 * h), vector=(0, -0.1), duration=0.3)
        i = i + 1
        if ele.exists():
            break


def back_findelement(ele):
    from airtest.core.api import keyevent
    from airtest.core.api import sleep
    """
       在指定元素出现前，模拟按下返回键，以便返回上一个页面。

       Args:
           ele (Element): 要等待出现的元素对象。

       Returns:
           无
       """
    i = 0
    while i < 10:
        if ele.exists():
            break
        keyevent('BACK')
        sleep(3.0)
        i = i + 1
        ele.refresh()


def first_setup_android(poco):
    import time
    from common.function import myFindElements
    from airtest.core.api import keyevent

    """
    首次安装弹窗处理
    """
    from common.function import refreshPage_find_to_elements
    myFindElements("com.hexin.plat.android:id/ok_btn", 2, poco)
    refreshPage_find_to_elements(10, poco("com.hexin.plat.android:id/ok_btn"))
    poco("com.hexin.plat.android:id/ok_btn").wait().click()
    # sleep(3)
    poco(text="没有炒过股").wait_for_appearance()
    poco(text="没有炒过股").wait().click()
    # sleep(3)
    try:
        poco(text="股票直接上手").wait_for_appearance()
        poco(text="股票直接上手").wait().click()
    except Exception as e:
        if poco(text="同顺商城").exists():
            pass

    time.sleep(3)
    # touch(Template(r"tpl1679645312526.png", record_pos=(0.356, -0.547), resolution=(1440, 3200)))
    keyevent('BACK')


def second_setup_android(poco):
    import time

    """
    处理第二次启动出现的弹窗
    """
    stop_app_open_app("com.hexin.plat.android")
    time.sleep(10)
    # 更新说明
    if poco(name="com.hexin.plat.android:id/iv_rocket_logo").exists():
        poco(name="com.hexin.plat.android:id/imgbtn_closebtn").click()
    # 新股批量申购弹窗
    if poco(text="新股批量申购").exists():
        poco("com.hexin.plat.android:id/close_button").click()
