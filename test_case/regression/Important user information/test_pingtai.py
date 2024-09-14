from airtest.core.android import Android
from airtest.core.api import *

from common.app_operation import *
from common.function import *




def test_yonghuzhongyaoxinxi(poco):
    # 测试用户重要信息非空
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
        if poco(text="用户重要信息").exists():
            found_button = True
            poco(text="用户重要信息").click()
            break
    if found_button:
        str = poco("android.widget.TextView").get_text()
    else:
        print("未找到目标按钮")

    result = has_invalid_values(str)
    print(result)
    assert result == False, "信息存在null或者空"
