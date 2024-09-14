#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    swipe_operations.py 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/07  用例id:
-------------------------------------------------
"""
import time
from airtest.core.api import swipe, sleep, snapshot, device


def swipe_up():
    w, h = device().get_current_resolution()
    swipe((0.5 * w, 0.8 * h), vector=(0, -0.2), duration=0.2)


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


def check_element_color(poco, target):
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

            # 检查颜色是否为红色（RGB为255, 0, 0）
            if color == (255, 0, 0):
                print(f"元素'{target}'的颜色为红色")
                return True
            else:
                print(f"元素'{target}'的颜色不是红色")
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


def scroll_element_below_another_element(target_element, reference_element):
    # 定位到目标元素和参考元素

    if target_element.exists() and reference_element.exists():
        # 获取目标元素和参考元素的位置
        target_pos = target_element.get_position()
        reference_pos = reference_element.get_position()

        # 计算目标元素需要滑动的偏移量
        target_offset_y = reference_pos[1] + reference_element.get_size()[1] / 2 - target_pos[1] + \
                          target_element.get_size()[1]

        # 将目标元素滑动到参考元素下方
        target_element.swipe([0, target_offset_y])
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

    while time.time() - start_time < timeout:
        # 更新垂直距离
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
        sleep(1)

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


def horizontal_swipe_until_element_found(target_element, reference_element, max_swipes=30):
    attempts = 0
    # w, h = device().get_current_resolution()
    while attempts < max_swipes:
        # 查找目标元素
        target_element.refresh()
        if target_element.exists():
            # 找到了目标元素
            print(f"横滑找到了目标元素{target_element}")
            return True  # 返回 True 表示找到了并点击了目标元素
        else:  # 横向滑动
            print(f"横滑没有找到了目标元素{target_element}")
            # yuan:[-0.0985, -0.0047]
            reference_element.swipe([-0.4143, 0.0059])
            # sleep(1.0)
            attempts += 1
    # 未找到目标元素，抛出异常或返回 False
    raise ValueError(f"未找到指定元素{target_element}")
    # return False


def right_swipe_until_element_found(poco, target_element, reference_element, max_swipes=30):
    attempts = 0

    while attempts < max_swipes:
        # 查找目标元素

        if target_element.exists():
            # 找到了目标元素
            print(f"右横滑找到了目标元素{target_element}")
            return True  # 返回 True 表示找到了并点击了目标元素
        else:  # 横向滑动
            print(f"右横滑没有找到了目标元素{target_element}")
            reference_element.swipe([0.1717, 0.0])
            reference_element.refresh()
            attempts += 1
    # 未找到目标元素，抛出异常或返回 False
    raise ValueError(f"未找到指定元素{target_element}")
    # return False


def swipe_until_element_found_element_width(target_element, reference_element, max_swipes=30):
    """
    Description:
    横向滑动直到找到目标元素，每次滑动距离为参考元素的宽度

    Args:
    - target_element: 待查找的目标元素
    - reference_element: 作为参考的滑动元素，用于计算滑动距离（宽度）
    - max_swipes: 最大尝试滑动次数，默认为30

    Returns:
    - True: 找到目标元素
    - ValueError: 未找到目标元素，抛出异常
    """
    attempts = 0
    element_width = reference_element.get_position()[0]

    while attempts < max_swipes:
        if target_element.exists():
            return True  # 找到了目标元素

        # 横向滑动，滑动距离为参考元素的宽度
        reference_element.swipe([-element_width, 0])
        sleep(3.0)
        attempts += 1

    raise ValueError(f"未找到指定元素{target_element}")