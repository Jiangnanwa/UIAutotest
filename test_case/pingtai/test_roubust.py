from airtest.core.android import Android
from airtest.core.api import *

from common.app_operation import *
from common.function import *

"""
测试热修复加载成功
"""


def test_rexiufu(poco):
    # 测试热修复加载成功
    try:
        homePageFindElements("com.hexin.plat.android:id/text_switcher", 2, poco).click()
    except Exception as e:
        print(e)
        keyevent("BACK")
        poco("com.hexin.plat.android:id/text_switcher").click()
    poco(desc="搜索输入框").set_text("MYHEXIN")
    search_find_elements('text="查看基本信息"', 1, poco)
    w, h = device().get_current_resolution()  # 获取手机分辨率
    steps = 10
    found_button = False
    for i in range(steps):
        swipe((0.5 * w, 0.8 * h), vector=(0, -0.5), duration=2)
        #time.sleep(0.5)  # 等待页面刷新
        if poco(text="ROBUST热修调试工具").exists():
            found_button = True
            poco(text="ROBUST热修调试工具").click()
            break

    if found_button:
        poco("com.hexin.plat.android:id/env_change").click()
        # str = poco("android.widget.TextView").get_text()
    else:
        print("未找到切换到 测试按钮或者")

    # 触发Toast消息，如果热修复成功则加载成功
    poco("com.hexin.plat.android:id/button").click()

    #滑动热修复提示窗口
    poco("com.hexin.plat.android:id/show_msg").swipe([-0.0405, -0.196])
    str=poco("com.hexin.plat.android:id/show_msg").get_text()
    print(str)
    # 检查Toast消息是否如预期
    assert "补丁加载成功" in str, "补丁加载失败"