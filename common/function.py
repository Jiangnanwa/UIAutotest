#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：
   Description :
   Author :chenqiyue
   CreateDate：
-------------------------------------------------
"""
import time
from datetime import datetime

from airtest.core.api import sleep, snapshot, device, swipe, keyevent


def jiaoyan_shujuxiang(getshujuxiang, shujuxianglist):
    """
    tangyujiao
    校验数据项字段与shujuxianglist一致、校验数据项值不为空及--
    适用于报价头校验、及其他数据项与数值混合的数据项校验，格式类似：现价1567.13涨额0.13涨幅0.01%高1584.00市值2.0万亿
    getshujuxiang: 获取的数据项
    shujuxianglist：定好的数据项，用于校验获取的数据项事都正确
    备注:
    有缺陷:只能校验展示的不缺少、不能校验展示字段是否多了
    """
    # 校验数据项不少
    getshujuxiangzhi = getshujuxiang
    getshujuxiangziduan = getshujuxiang
    for shujuxiang in shujuxianglist:
        if shujuxiang in getshujuxiang:
            # 删除数据项字段、只余数据项值：用户判断数据非空及--
            getshujuxiangzhi = getshujuxiangzhi.replace(shujuxiang, ' ')
        else:
            print("数据项", shujuxiang, "检测不存在")
            exit(0)

    # 校验数据项不多
    getshujuxiangzhi = getshujuxiangzhi.lstrip(' ')
    shujuzhi = getshujuxiangzhi.split(' ')
    for zhi in shujuzhi:
        getshujuxiangziduan = getshujuxiangziduan.replace(zhi, ' ')
    getshujuxiangziduan = getshujuxiangziduan.rstrip(' ')
    ziduan = getshujuxiangziduan.split(' ')
    for shujuxiang in ziduan:
        if shujuxiang not in shujuxianglist:
            print("数据项", shujuxiang, "多余")
            exit(0)

    # 判断数据项值不为空及--
    for zhi in shujuzhi:
        if zhi == None or zhi == "--":
            print(zhi + "为空或--")
            exit(0)


def get_shuzhi(shuju, ziduanlist):
    """
    tangyujiao
    获取数据项与数值混合中的数值：现价1567.13涨额0.13涨幅0.01%高1584.00市值2.0万亿
    """
    for ziduan in ziduanlist:
        if ziduan in shuju:
            # 删除数据项字段、只余数据项值：用户判断数据非空及--
            shuju = shuju.replace(ziduan, ' ')
    shuzhi = shuju.split(' ')
    del (shuzhi[0])
    return shuzhi


def getintofneshi_fromzixuan(name, code, poco):
    """
    Author :tangyujiao
    2023/04/04
    通过自选tab进入个股详情页
    """
    from common.app_operation import stop_app_open_app

    if poco(text="自选").exists():
        poco(text="自选").click()
    else:
        stop_app_open_app("com.hexin.plat.android")
        poco(text="自选").wait_for_appearance(30)
        poco(text="自选").click()
    poco(name + "#" + code).wait_for_appearance(15)
    poco(name + "#" + code).click()


def refreshPage_find_to_elements(num, elem):
    a = elem.exists()
    # app启动时,会存在五星好评弹窗,需要处理

    i = 0
    while i < num:

        if a != True:
            print("元素没找到重新刷新")
            elem.refresh()
            a = elem.exists()
            i = i + 1
        else:
            return elem
            break


def myFindElements(elem, num, poco):
    """
        Author :chenqiyue
        元素没有出现时，走异常处理，查看当前页面有没有黑名单弹窗，如果有则点击，无则仍然返回元素
        :param :
            elem:元素属性值, num：重复查找黑名单次数,poco
        :return:返回元素
        """
    a = {poco("com.hexin.plat.android:id/close_img"),poco("com.hexin.plat.android:id/iknow"), poco("com.hexin.plat.android:id/info"), poco(text="允许"),
             poco("com.hexin.plat.android:id/tv_skip"), poco("com.hexin.plat.android:id/ok_btn"),
             poco("com.hexin.plat.android:id/iknow"), poco(text="确定")
             }
    i = 0
    while i < num:
        print(i)

        if poco(elem).exists():
            return poco(elem)  # 如果元素存在，立即返回该元素
        elif poco(text=elem).exists():
            return poco(text=elem)
        else:
            # 主要实现是：如果页面中可以找到元素，则返回，没有循环遍历是否有弹窗，有则点击，再次循环查找是否有元素
            for j in a:  # 遍历弹窗元素
                print(j)
                if j.exists():
                    j.click()  # 点击弹窗
                    print(f"弹窗{j}被点击")

                    sleep(1.0)
                    if poco(elem).exists():
                        print(f"查找元素第{i}次,{elem}存在,方法返回元素")
                        return poco(elem)  # 如果元素存在，立即返回该元素

            i += 1

    # 如果在所有迭代后仍未找到元素，返回 None 或者进行适当处理
    return poco(elem)  # 或者针对未找到元素的情况进行适当处理
from airtest.core.api import *

def homePageFindElements(elem, num, poco):
    """
        Description :此方法为首页元素处理弹窗的方法，黑名单弹窗为首页可能出现的弹窗元素
        Author :chenqiyue
        元素没有出现时，走异常处理，查看当前页面有没有黑名单弹窗，如果有则点击，无则仍然返回元素
        :param :
            elem:元素属性值, num：重复查找黑名单次数,poco
        :return:返回元素
        """

    a = {poco("com.hexin.plat.android:id/close_button"), poco("com.hexin.plat.android:id/closeBt"),
         poco("com.hexin.plat.android:id/imgbtn_closebtn"), poco("com.hexin.plat.android:id/tv_skip"), poco(name="com.hexin.plat.android:id/capsule_right")
         }
    i = 0
    while i < num:
        print(f"查找元素第{i}次")
        if elem.exists():
            print(f"查找元素第{i}次,{elem}存在,方法返回元素")
            return elem  # 如果元素存在，立即返回该元素
        else:
            # 主要实现是：如果页面中可以找到元素，则返回，没有循环遍历是否有弹窗，有则点击，再次循环查找是否有元素
            for j in a:  # 遍历弹窗元素
                print(j)
                if j.exists():
                    j.click()  # 点击弹窗
                    print(f"弹窗{j}被点击")
                    sleep(1.0)
                    if elem.exists():
                        print(f"查找元素第{i}次,{elem}存在,方法返回元素")
                        return elem  # 如果元素存在，立即返回该元素
            i += 1
    # 有的弹窗不会被定位到,可以增加稳定性,循环了黑名单但是还是没有,可以选择点击安卓的返回按钮也可以将弹窗消失
    # if not elem.exists():
    #     keyevent("BACK")
    # 如果在所有迭代后仍未找到元素，返回 None 或者进行适当处理
    return elem  # 或者针对未找到元素的情况进行适当处理


def zixuan_tab_find_elements(elem, num, poco):
    """
        Description :此方法为自选页元素处理弹窗的方法，黑名单弹窗为首页可能出现的弹窗元素
        Author :chenqiyue
        元素没有出现时，走异常处理，查看当前页面有没有黑名单弹窗，如果有则点击，无则仍然返回元素
        :param :
            elem:元素属性值, num：重复查找黑名单次数,poco
        :return:返回元素
        """

    a = {poco(text="我知道了")
         }
    i = 0
    while i < num:
        print(i)
        if elem.exists():
            return elem  # 如果元素存在，立即返回该元素
        else:
            # 主要实现是：如果页面中可以找到元素，则返回，没有循环遍历是否有弹窗，有则点击，再次循环查找是否有元素
            for j in a:  # 遍历弹窗元素
                print(j)
                if j.exists():
                    j.click()  # 点击弹窗
                    print(f"弹窗{j}被点击")
                    sleep(1.0)
                    if elem.exists():
                        print(f"查找元素第{i}次,{elem}存在,方法返回元素")
                        return elem  # 如果元素存在，立即返回该元素
            i += 1

    # 如果在所有迭代后仍未找到元素，返回 None 或者进行适当处理
    return elem  # 或者针对未找到元素的情况进行适当处理


def search_find_elements(elem, num, poco):
    """
        Description :此方法为首页-搜索页面元素处理弹窗的方法，黑名单弹窗为首页可能出现的弹窗元素
        Author :chenqiyue
        元素没有出现时，走异常处理，查看当前页面有没有黑名单弹窗，如果有则点击，无则仍然返回元素
        :param :
            elem:元素属性值, num：重复查找黑名单次数,poco
        :return:返回元素
        """
    try:

        poco(elem).wait_for_appearance(5)
        return poco(elem)
    except Exception as e:
        print(e)
        a = {poco(text="使用时允许"), poco(text="仅在使用中允许"), poco(text="仅使用期间允许"), poco(text="仅在使用该应用时允许"),
             poco(text="使用应用时允许"), poco(text="仅在使用时允许"),
             }
        elemexists = poco(elem).exists()
        i = 0
        while i < num:
            print(i)
            if elemexists != True:
                for j in a:
                    print(j)
                    if j.exists():
                        j.click()
                        print(f"弹窗{j}被点击")
                elemexists = poco(elem).exists()

            else:
                return poco(elem)
            i = i + 1
        return poco(elem)


def hang_qing_find_elements(elem, num, poco):
    """
        Description :此方法为行情页面元素处理弹窗的方法，黑名单弹窗为首页可能出现的弹窗元素
        Author :chenqiyue
        元素没有出现时，走异常处理，查看当前页面有没有黑名单弹窗，如果有则点击，无则仍然返回元素
        :param :
            elem:元素属性值, num：重复查找黑名单次数,poco
        :return:返回元素
        """
    try:

        poco(elem).wait_for_appearance(2)
        return poco(elem)
    except Exception as e:
        print(e)
        a = {poco("在看一会")}
        elemexists = poco(elem).exists()
        i = 0
        while i < num:
            print(i)
            if elemexists != True:
                for j in a:
                    print(j)
                    if j.exists():
                        j.click()
                elemexists = poco(elem).exists()

            else:
                return poco(elem)
            i = i + 1
        return poco(elem)


def fenshixiangqingye_find_elements(elem, num, poco):
    """
        Description :此方法为分时k线页面元素处理弹窗的方法，黑名单弹窗为首页可能出现的弹窗元素
        Author :chenqiyue
        元素没有出现时，走异常处理，查看当前页面有没有黑名单弹窗，如果有则点击，无则仍然返回元素
        :param :
            elem:元素属性值, num：重复查找黑名单次数,poco
        :return:返回元素
        """

    a = {poco(text="我知道了"), poco(text="全景500档里面看全部价位挂单分布"), poco(text="全景500档里面看全部价位挂单分布"),
         poco("com.hexin.plat.android:id/i_know"), poco("com.hexin.plat.android:id/ok_btn")}
    i = 0
    while i < num:
        print(i)
        if elem.exists():
            return elem  # 如果元素存在，立即返回该元素
        else:
            # 主要实现是：如果页面中可以找到元素，则返回，没有循环遍历是否有弹窗，有则点击，再次循环查找是否有元素
            for j in a:  # 遍历弹窗元素
                print(j)
                if j.exists():
                    j.click()  # 点击弹窗
                    sleep(1.0)
                    if elem.exists():
                        print(f"查找元素第{i}次,{elem}存在,方法返回元素")
                        return elem  # 如果元素存在，立即返回该元素
            i += 1

    # 如果在所有迭代后仍未找到元素，返回 None 或者进行适当处理
    return elem  # 或者针对未找到元素的情况进行适当处理


def network_switch_3015(poco):
    '''
       检验当前网络3015是否连接,抓异常,有的手机没有text=修改网络元素,使用坐标点击
       如果是,走更改代理为无
       若否,更改网络为3015,更改代理为无
    '''
    from airtest.core.api import stop_app, start_app
    stop_app("com.android.settings")
    start_app("com.android.settings")
    poco(text="WLAN").wait().click()

    if poco(nameMatches="3015,已连接.*"):
        poco(text="3015").long_click()
    else:
        poco(text="3015").wait().click()
        poco(text="连接").wait().click()
        poco(text="3015").long_click()
    try:
        # 华为p40修改网络会黑屏
        poco(text="修改网络").wait(2).click()

    except Exception as e:
        element = poco(text="删除网络")
        # 获取删除网络元素的x和y值
        x = element.get_position()[0]
        y = element.get_position()[1]
        print(x, y)
        height = element.get_size()[1]
        print(height)
        # y值增加删除网络的高*2
        y = y + height * 2
        print(y)
        poco.click([x, y])

    if poco(text="无"):
        pass
    else:
        poco("com.android.settings:id/proxy_settings").wait(2).click()
        poco(text="无").wait(2).click()
        # 保存
        poco("com.android.settings:id/btn_wifi_connect").wait(5).click()


# def network_switch_10jqka(poco):
#     from airtest.core.api import stop_app, start_app
#     stop_app("com.android.settings")
#     start_app("com.android.settings")
#     poco(text="WLAN").wait().click()
#
#     if poco(nameMatches="10JQKA,已连接.*"):
#         pass
#     else:
#         poco(text="10JQKA").wait().click()
#         poco(text="连接").wait().click()


def goto_network_settings(poco):
    from airtest.core.api import stop_app, start_app

    stop_app("com.android.settings")
    start_app("com.android.settings")
    poco(text="WLAN").wait().click()


def connect_to_10jqka(poco):
    # 等待 10JQKA 已连接
    if poco(nameMatches="10JQKA,已连接.*").exists():
        pass
    else:
        poco(text="10JQKA").wait().click()
        poco(text="连接").wait().click()


def network_switch_10jqka(poco):
    '''
    华为p20切换网络会黑屏
    '''
    goto_network_settings(poco)
    connect_to_10jqka(poco)


def option_light_theme_switch(poco):
    from airtest.core.api import sleep
    from airtest.core.api import stop_app, start_app
    stop_app("com.android.settings")
    start_app("com.android.settings")
    i = 0
    while i < 10:
        poco(text="WLAN").swipe([0, -0.1])
        sleep(1.0)
        i = i + 1
        if poco(text="显示和亮度").exists():
            poco(text="显示和亮度").click()
            break
    poco("DBSDeviceAppearanceOptionLight").wait().click()


def has_invalid_values(input_str):
    # 分割输入字符串为多个字段
    fields = input_str.split('\n')

    # 遍历每个字段
    for field in fields:
        # 分割字段为键和值
        key_value = field.split('=')
        if len(key_value) == 2:
            _, value = key_value
            # 检查值是否无效
            if value in ["null", ""]:
                return True

    return False


def swipe_up():
    from airtest.core.api import swipe
    # # 获取设备的高度和宽度
    # width, height = device().get_current_resolution()
    # start_pt = (height * 0.8, width / 2)
    # end_pt = (height * 0.2, width / 2)
    # # 滑动5次:
    # swipe(start_pt, end_pt, duration=0.3)
    # sleep(1)
    w, h = device().get_current_resolution()  # 获取手机分辨率

    swipe((0.5 * w, 0.8 * h), vector=(0, -0.2), duration=0.2)  # 在0.2s内上划0.3个屏幕


def find_element_with_swipe(poco, target_text, max_swipe_attempts=2):
    attempt = 0
    found = False

    while attempt < max_swipe_attempts and not found:
        try:
            while not poco(text=target_text).exists():
                poco.swipe([0, -0.5])  # 向下滑动页面
                sleep(1)  # 等待页面滑动完成

            # 找到元素后执行相应操作
            print(f"找到元素：{target_text}")
            found = True
            # 在这里可以添加需要执行的操作，比如点击找到的元素等

        except Exception as e:
            print(f"发生异常：{e}")
            attempt += 1
            if attempt < max_swipe_attempts:
                print(f"第 {attempt + 1} 次滑动...")
                poco.swipe([0, 0.5])  # 上滑页面
                sleep(1)  # 等待页面滑动完成
            else:
                raise Exception("未找到目标元素，达到最大尝试次数")


def check_element_color(poco, target, RGB=(0, 0, 0)):
    # 找到指定的元素
    element = poco(target)

    if element.exists():
        # 获取元素的位置和大小信息
        pos = element.get_position()
        size = element.get_size()

        # 计算元素所在位置的中心点
        center_x = pos[0] + size[0] // 2
        center_y = pos[1] + size[1] // 2

        # 获取该位置的像素颜色
        screenshot = snapshot(filename=None)

        if screenshot:
            color = screenshot.getpixel((center_x, center_y))
            print(color)
            # 检查颜色是否为红色（RGB为255, 0, 0）
            if color == RGB:
                print(f"元素'{target}'的颜色为{color},是目标颜色")
                return True
            else:
                print(f"元素'{target}'的颜色为{color},不是目标颜色")
                return False
        else:
            print("获取截图失败")
            return False
    else:
        print(f"未找到元素'{target}'")
        return False


def scroll_element_to_center(poco, element):
    # 获取屏幕尺寸
    screen_width, screen_height = poco.get_screen_size()

    # 定位到指定文本的元素

    if element.exists():
        # 获取元素的位置
        element_pos = element.get_position()

        # 计算元素居中的位置
        center_x = screen_width / 2
        center_y = screen_height / 2

        # 计算需要滑动的偏移量
        offset_x = center_x - element_pos[0]
        offset_y = center_y - element_pos[1]

        # 将元素滑动到屏幕中间
        element.swipe([-offset_x, -offset_y])
        return True
    else:
        return False  # 元素不存在


def scroll_element_to_top(poco, element):
    if element.exists():
        # 获取元素的位置
        element_pos = element.get_position()

        # 计算需要滑动的偏移量
        offset_y = element_pos[1]  # 将元素滑动到屏幕上方，Y 轴偏移量为元素当前位置的 Y 坐标

        # 将元素滑动到屏幕上方
        element.swipe([0, -offset_y])
        return True
    else:
        return False  # 元素不存在


def scroll_element_below_another_element(target_element, reference_element, swipe_element, timeout=300):
    # 获取目标元素和参考元素的位置
    target_pos = target_element.get_position()
    reference_pos = reference_element.get_position()
    print("target_pos", target_pos, reference_pos)
    target_height = target_element.get_size()[1]
    print("target_height", target_height)
    # 向上滑动，滑动一个目标元素的高度，直到达垂直距离小于目标元素高度的三倍
    start_time = time.time()  # 记录开始时间
    i = 0.1
    while time.time() - start_time < timeout:
        # 更新垂直距离
        if target_element.exists():
            target_element.refresh()

            target_pos = target_element.get_position()
            vertical_distance = target_pos[1] - reference_pos[1]
            if vertical_distance > target_height * 3:
                # 执行向上滑动的操作，这里使用你的操作方法
                # swipe((0.5 * w, 0.8 * h), vector=(0, -10), duration=0.2)
                # poco(text="更多").swipe([-0.009, -0.0609])
                swipe_element.refresh()
                swipe_element.swipe([-0.009, -0.0609])
                sleep(1)
                # i=i+0.01热
                print(i)
            else:
                break
        else:
            break

        print(f"vertical_distance{vertical_distance},target_height*3{target_height * 3}")


# 调用函数并指定要查找的元素文本和超时时间
def find_element_within_timeout(element, timeout=30):
    start_time = time.time()  # 记录开始时间
    while time.time() - start_time < timeout:
        if element.exists():
            return True  # 找到元素，返回 True

        w, h = device().get_current_resolution()
        swipe((0.5 * w, 0.8 * h), vector=(0, -0.2), duration=0.1)
        sleep(2)
        element.refresh()
    # 如果超时还未找到元素，抛出自定义异常
    raise TimeoutError(f"Element '{element}' not found within {timeout} seconds.")


def scroll_element_into_view(target_element, max_swipe_attempts=10):
    attempts = 0
    while not target_element.exists() and attempts < max_swipe_attempts:
        # 在这里进行上滑操作，使目标元素展示出来
        # 获取设备分辨率
        width, height = device().get_current_resolution()
        # 计算中心点
        center_x = width // 3
        center_y = height // 3
        # 计算新的目标点（偏下方）
        new_target_y = height // 3 + height // 10  # 假设向下滑动到距离顶部 60% 的位置
        # 执行滑动操作
        swipe((center_x, center_y), (center_x, new_target_y), duration=0.1, steps=1)
        sleep(2.0)
        attempts += 1


def check_attr_updated(element_id, attr_name, second=60):
    """
    检查元素属性在一定时间内是否发生变化(刷新)

    Args:
        poco: Poco对象
        element_id (str): 元素ID
        attr_name (str): 属性名称

    Raises:
        AssertionError: 如果属性在一分钟内未更新

    Example:
        check_attr_updated(poco, "com.hexin.plat.android:id/fenshi_headline_view", "desc")
    """
    # 获取初始的属性值
    initial_attr = element_id.attr(attr_name)

    # 等待1分钟
    time.sleep(second)

    # 获取1分钟后的属性值
    element_id.refresh()
    updated_attr = element_id.attr(attr_name)
    print(f"原始数据:{initial_attr}")
    print(f"更新后的数据:{updated_attr}")
    # 检查属性值是否发生变化
    if initial_attr == updated_attr:
        raise AssertionError(f"{element_id}的{attr_name}属性在一分钟内未更新")
    else:
        print(f"{element_id}的{attr_name}属性已更新")


def check_time_range():
    """
    检查当前时间是否在指定的时间段内。

    返回值:
        - True: 如果当前时间在指定时间段内
        - False: 如果当前时间不在指定时间段内
    """
    # 获取当前时间
    current_time = datetime.now().time()

    # 设置允许执行代码的时间段
    allowable_time_ranges = [
        (datetime.strptime('9:30', '%H:%M').time(), datetime.strptime('11:29:59', '%H:%M:%S').time()),
        (datetime.strptime('13:00', '%H:%M').time(), datetime.strptime('14:59:59', '%H:%M:%S').time())
    ]

    # 检查当前时间是否在允许的时间段内
    execute_code = False
    for start_time, end_time in allowable_time_ranges:
        if start_time <= current_time <= end_time:
            execute_code = True
            break

    # 返回布尔值，表示是否在允许的时间段内
    return execute_code


def validate_stock_navigation(poco, element_index_name, element_navi_title_text):
    """
    校验点击股票跳转分时后是否跳转对应分时，并验证返回上一级位置是否记忆

    入参:
        - element_stock: 股票元素对象，用于记录坐标和点击操作
        - element_back_button: 返回按钮元素对象，用于检查坐标点变化

    功能实现:
        - 记录股票元素对象的初始坐标
        - 获取当前的股票名称文本
        - 点击股票元素对象，跳转至对应的分时页面
        - 点击返回按钮
        - 检查返回按钮元素对象的坐标是否发生变化，若发生变化则抛出错误
    """
    # 记录初始坐标点
    initial_coordinates = element_index_name.get_position()

    # 获取当前股票名称
    current_index_name = element_index_name.get_text()

    # 点击股票名称
    element_index_name.click()

    # 获取跳转后的页面标题
    navi_title_text = element_navi_title_text.get_text()

    # 校验两个值是否一致
    if current_index_name != navi_title_text:
        print(f"跳转前股票名称:{initial_coordinates},分时页股票名称:{navi_title_text}")
        raise AssertionError("未跳转至对应的分时页")

    # 点击返回按钮
    element_back_button = poco("com.hexin.plat.android:id/backButton")
    element_back_button.click()

    # 检查坐标点是否变化
    back_button_coordinates = element_index_name.get_position()
    if initial_coordinates != back_button_coordinates:
        print(initial_coordinates, back_button_coordinates)
        raise AssertionError("点击返回按钮后，坐标点发生了变化")

    # 切换不同的返回方式：按钮点击、按键返回、手势返回
    actions = [

        lambda: keyevent('BACK')
    ]

    for action in actions:

        # 点击股票名称
        element_index_name.click()
        action()
        back_button_coordinates = element_index_name.get_position()
        if initial_coordinates != back_button_coordinates:
            raise AssertionError("返回操作后，坐标点发生了变化")
def swipe_until(btn, elem, dir):
    """
    上滑or下滑直到看到某元素
     Author :zwx
        :param :
            btn:需要校验是否存在的元素, dir:滑动坐标
    """
    while not btn.exists():
        try:
            elem.swipe(dir)
        except Exception as e:
            print('### 找不到该元素')
            break
def switch(num,poco):
        poco.num=num
        poco.arr = []
        # 第一次进分时页有提示小窗
        right = poco("com.hexin.plat.android:id/navi_right_icon")
        left = poco("com.hexin.plat.android:id/navi_left_icon")
        for i in range(num):
            guide = [poco("com.hexin.plat.android:id/bubble_guide_close"),
                     poco("com.hexin.plat.android:id/iknow"), poco(text="好的")]
            for i in guide:
                if i.exists():
                    i.click()
            stock_name0 = poco("com.hexin.plat.android:id/navi_title_text").get_text()
            print(stock_name0)
            refreshPage_find_to_elements(1, right)
            right.click()
            sleep(1)
            if stock_name0 not in poco.arr:
                poco.arr.append(stock_name0)

        for i in range(num):
            refreshPage_find_to_elements(1, left)
            left.click()
            sleep(1)
            poco.stock_name1 = poco("com.hexin.plat.android:id/navi_title_text").get_text()
            print(poco.stock_name1)

def switch_testify(poco):
        if (len(poco.arr) == poco.num+1):
            assert poco.stock_name1 == poco.arr[0]
# 计算坐标值
def calculate_coordinate(x_percent, y_percent):
    """
    根据屏幕宽高和输入的百分比计算坐标值

    参数:
    x_percent (int): x轴百分比，范围为0到100。
    y_percent (int): y轴百分比，范围为0到100。

    返回:
    tuple: 返回计算后的坐标值 (x, y)。
    """
    width, height = device().get_current_resolution()
    # 获取屏幕宽高
    # 计算坐标值
    x = int(width * x_percent / 100)
    y = int(height * y_percent / 100)

    return x, y


def find_elements_with_same_x_position(poco, text_pattern, attr_name='pos'):
    """
    封装代码以找到所有与第一个元素具有相同x位置的元素。

    参数:
    poco: 用于搜索元素的poco实例。
    text_pattern: 用于匹配元素文本的模式。
    attr_name: 要检查的属性名称，默认为'pos'。

    返回:
    一个包含具有相同x位置的元素的列表。
    """
    # 使用poco和文本模式查找所有匹配的元素
    elements_with_name = poco(textMatches=text_pattern)

    # 获取第一个元素的x位置
    if elements_with_name:
        element_first_x = elements_with_name.attr(attr_name)[0]
    else:
        return []  # 如果没有找到元素，则返回空列表

    # 筛选出所有x位置与第一个元素相同的元素
    elements = [element for element in elements_with_name if element.attr(attr_name)[0] == element_first_x]
    print(f"筛选出所有x位置与第一个元素相同的元素{elements}")
    return elements

