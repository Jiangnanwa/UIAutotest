#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    image
   Description :
   Author :       duanxufei
   CreateDate：   2020/3/24 10:17
-------------------------------------------------
"""
import subprocess

import cv2
import numpy as np
import collections
import tempfile
import os, random
import time

from PIL import Image


def getColorList():
    """
    颜色范围初始化
    Returns:

    """
    dict = collections.defaultdict(list)

    # 黑色
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 55])
    color_list = []
    color_list.append(lower_black)
    color_list.append(upper_black)
    dict['black'] = color_list

    # 灰色
    lower_gray = np.array([0, 0, 55])
    upper_gray = np.array([180, 43, 220])
    color_list = []
    color_list.append(lower_gray)
    color_list.append(upper_gray)
    dict['gray'] = color_list

    # 白色
    lower_white = np.array([0, 0, 221])
    upper_white = np.array([180, 30, 255])
    color_list = []
    color_list.append(lower_white)
    color_list.append(upper_white)
    dict['white'] = color_list

    # 红色
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red'] = color_list

    # 红色2
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red2'] = color_list

    # 橙色
    lower_orange = np.array([11, 43, 46])
    upper_orange = np.array([25, 255, 255])
    color_list = []
    color_list.append(lower_orange)
    color_list.append(upper_orange)
    dict['orange'] = color_list

    # 黄色
    lower_yellow = np.array([26, 43, 46])
    upper_yellow = np.array([34, 255, 255])
    color_list = []
    color_list.append(lower_yellow)
    color_list.append(upper_yellow)
    dict['yellow'] = color_list

    # 绿色
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    color_list = []
    color_list.append(lower_green)
    color_list.append(upper_green)
    dict['green'] = color_list

    # 青色
    lower_cyan = np.array([78, 43, 46])
    upper_cyan = np.array([99, 255, 255])
    color_list = []
    color_list.append(lower_cyan)
    color_list.append(upper_cyan)
    dict['cyan'] = color_list

    # 蓝色
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])
    color_list = []
    color_list.append(lower_blue)
    color_list.append(upper_blue)
    dict['blue'] = color_list

    # 紫色
    lower_purple = np.array([125, 43, 46])
    upper_purple = np.array([155, 255, 255])
    color_list = []
    color_list.append(lower_purple)
    color_list.append(upper_purple)
    dict['purple'] = color_list

    return dict


def get_color(image_path, shield_list=None):
    """
    获取指定图片的主体颜色，有且只会返回一种颜色
    Args:
        image_path:待处理的图片路径
        shield_list: 需要屏蔽掉的颜色列表。
                    可选参数有'black'(黑色),'gray'(灰色),'white'(白色),'red'(红色),'red2'(红色2),'orange'(橙色),'yellow'(黄色),
                    'green'(绿色),'cyan'(青色),'blue'(蓝色),'purple'(紫色)

    Returns:    返回指定图片的主体颜色的字符串，例如'black'。如果是纯色图片，且该颜色被屏蔽，则返回None

    """
    if shield_list is None:
        shield_list = []
    image_frame = cv2.imread(image_path)
    hsv = cv2.cvtColor(image_frame, cv2.COLOR_BGR2HSV)
    maxsum = -100
    color = None
    color_dict = getColorList()
    for black_color in shield_list:
        if black_color in color_dict:
            color_dict.pop(black_color)
    tmp_num = random.randint(0, 99)
    color_dict_len = len(color_dict)
    same_pic = 0
    for d in color_dict:
        mask = cv2.inRange(hsv, color_dict[d][0], color_dict[d][1])
        # cv2.imwrite(os.path.join(tempfile.gettempdir(), f"{d}_{tmp_num}.jpg"), mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        binary = cv2.dilate(binary, None, iterations=0)
        cnts, hiera = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        sum = 0
        for c in cnts:
            sum += cv2.contourArea(c)
        if sum > maxsum:
            maxsum = sum
            color = d
            same_pic = 1
        elif sum == maxsum:
            same_pic += 1
        if same_pic == color_dict_len:
            color = None

    return color


def get_screenshot_by_element(driver, element):
    """
    获取指定元素的截图(android)
    Args:
        driver: appium驱动
        element: 要获取截图的元素

    Returns:

    """
    # 先截取整个屏幕，存储至系统临时目录下

    TEMP_FILE = os.path.join(tempfile.gettempdir(), f"temp_screen_{int(time.time() * 1000)}.png")
    driver.get_screenshot_as_file(TEMP_FILE)

    # 获取元素四角坐标
    location = element.location
    size = element.size

    # 截取图片
    TEMP_FILE_2 = os.path.join(tempfile.gettempdir(), f"temp_screen_{int(time.time() * 1000)}.png")
    cut_image(TEMP_FILE, location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"],
              TEMP_FILE_2)
    return TEMP_FILE_2


def assert_color(driver, element):
    image_path = get_screenshot_by_element(driver, element)
    res = get_color(cv2.imread(image_path))
    if res == 'red' or res == 'red2':
        return 'red'
    elif res == 'green':
        return 'green'


def get_screenshot_by_percent(driver, out_image_path=None, x1=0, y1=0, x2=1, y2=1):
    """
    根据百分比截取屏幕截图
    Args:
        driver: appium驱动
        out_image_path: 截图结果输出路径
        x1: 所要截取区域左上角坐标的横坐标占屏幕宽度的百分比。0<=x1<=1
        y1: 所要截取区域左上角坐标的纵坐标占屏幕宽度的百分比。0<=y1<=1
        x2: 所要截取区域右上角坐标的横坐标占屏幕宽度的百分比。0<=x2<=1
        y2: 所要截取区域右下角坐标的纵坐标占屏幕宽度的百分比。0<=y2<=1

    Returns:截图结果存放路径

    """
    # 先截取整个屏幕，存储至系统临时目录下

    TEMP_FILE = os.path.join(tempfile.gettempdir(), f"temp_screen_{int(time.time() * 1000)}.png")
    driver.get_screenshot_as_file(TEMP_FILE)

    # 截取图片
    out_image_path = cut_image(TEMP_FILE, x1, y1, x2, y2, out_image_path, use_percent=True)
    return out_image_path


def cut_image(input_image_path, x1, y1, x2, y2, out_image_path, use_percent=False):
    """
    图片截取函数
    Args:
        input_image_path: 要处理的图片原始路径
        x1:要截取范围左上角的横坐标或百分比
        y1:要截取范围左上角的纵坐标或百分比
        x2:要截取范围右下角的横坐标或百分比
        y2:要截取范围右下角的纵坐标或百分比
        out_image_path: 结果输出的图片路径
        use_percent: 是否启用百分比模式，默认为不启用
    """
    if not out_image_path:
        out_image_path = os.path.join(tempfile.gettempdir(), f"temp_screen_{int(time.time() * 1000)}.png")
    image = Image.open(input_image_path)  # 读取原始图片
    if use_percent:
        size = image.size  # 获取图片的尺寸
        x1 = size[0] * x1
        y1 = size[1] * y1
        x2 = size[0] * x2
        y2 = size[1] * y2
    box = (x1, y1, x2, y2)  # 设定截取区域
    newImage = image.crop(box)  # 进行截取操作
    newImage.save(out_image_path)  # 保存截取结果
    return out_image_path


def get_color_by_element(driver, element, shield_list=None):
    """
    获取指定元素的主体颜色
    Args:
        driver: appium驱动
        element: 要获取颜色的元素
        shield_list: 要屏蔽的颜色列表
    Returns:

    """
    return get_color(get_screenshot_by_element(driver, element), shield_list)


if __name__ == '__main__':
    # filename = 'ios_h.png'
    # filename = 'C:\\Users\\viruser.v-desktop\\Desktop\\tmp\\white.png'
    filename = 'D:\\img\\323232.png'

    # filename = 'ios_l.png'
    # filename = 'and_h.png'
    # filename = 'and_l.png'
    print(get_color(filename, shield_list=['white']))
    # file_list = ['ios_h.png', 'ios_l.png', 'and_h.png', 'and_l.png']
    # for i in file_list:
    #     frame = cv2.imread(i)
    #     print(get_color(frame))


def baipingjianche(driver):
    """
    白屏检测简单版
    获取当前页面主要颜色，并判断是否是白色
    """
    TEMP_FILE = os.path.join(tempfile.gettempdir(), f"temp_screen_{int(time.time() * 1000)}.png")
    driver.get_screenshot_as_file(TEMP_FILE)
    color = get_color(TEMP_FILE, shield_list=None)
    if color == 'white' or color == 'white':
        return ("flase")
    else:
        return ("true")


def get_non_excluded_color(image_path, excluded_color):
    # 读取图像
    image = cv2.imread(image_path)

    # 将排除的颜色转换为 OpenCV 中的颜色空间格式
    excluded_color_np = np.array(excluded_color, dtype=np.uint8)

    # 创建掩码，将排除的颜色设为白色，其他颜色设为黑色
    mask = cv2.inRange(image, excluded_color_np, excluded_color_np)
    masked_image = cv2.bitwise_not(mask)

    # 统计非排除颜色的出现次数
    colors, counts = np.unique(image[masked_image != 0], axis=0, return_counts=True)

    # 找到出现次数最多的颜色
    max_count_index = np.argmax(counts)
    max_count_color = colors[max_count_index]

    return max_count_color


# 使用 adb 命令截取整个屏幕的截图
def take_screenshot():
    screenshot_path = "screenshot.png"
    subprocess.run(["adb", "shell", "screencap", "-p", "/sdcard/screenshot.png"])
    subprocess.run(["adb", "pull", "/sdcard/screenshot.png", screenshot_path])
    return screenshot_path


# 使用 poco 框架获取元素的绝对位置和大小信息
def get_element_position_and_size(element):
    # 获取元素相对于屏幕左上角的位置
    relative_position = element.get_position()

    # 获取屏幕大小
    screen_width, screen_height = poco.get_screen_size()

    # 计算元素的绝对位置
    absolute_x = relative_position[0]
    absolute_y = relative_position[1]

    # 返回元素的绝对位置
    return absolute_x, absolute_y


# 使用 PIL 库根据指定的位置和大小裁剪图像
def crop_element(screenshot_path, position, size):
    image = Image.open(screenshot_path)
    x, y = position
    width, height = size
    # 确保裁剪区域不会超出图像的边界
    image_width, image_height = image.size
    x = max(0, min(x, image_width - 1))
    y = max(0, min(y, image_height - 1))
    width = max(1, min(width, image_width - x))
    height = max(1, min(height, image_height - y))
    element_image = image.crop((x, y, x + width, y + height))
    return element_image
