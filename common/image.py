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
import base64
import collections
import json
import tempfile

import requests
from PIL import Image
from airtest.aircv import *
from airtest.core.api import *


def getColorList():
    """
    颜色范围初始化
    Returns:

    """
    dict = collections.defaultdict(list)

    # 黑色
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 46])
    color_list = []
    color_list.append(lower_black)
    color_list.append(upper_black)
    dict['black'] = color_list

    # 灰色
    lower_gray = np.array([0, 0, 46])
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
    # tmp_num = random.randint(0, 99)
    color_dict_len = len(color_dict)
    same_pic = 0
    for d in color_dict:
        mask = cv2.inRange(hsv, color_dict[d][0], color_dict[d][1])
        # cv2.imwrite(os.path.join(tempfile.gettempdir(), f"{d}_{tmp_num}.jpg"), mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        binary = cv2.dilate(binary, None, iterations=2)
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


def get_device_full_screenshot():
    """
    获取设备完整截图
    """
    # 先截取整个屏幕，存储至系统临时目录下

    TEMP_FILE = os.path.join(tempfile.gettempdir(), f"temp_screen_{int(time.time() * 1000)}.png")
    screen = G.DEVICE.snapshot()
    aircv.imwrite(TEMP_FILE, screen, ST.SNAPSHOT_QUALITY, max_size=ST.IMAGE_MAXSIZE)
    return TEMP_FILE


def get_screenshot_by_element(poco_element):
    """
    获取指定元素的截图(android)
    Args:
        poco_element: 要获取截图的元素

    Returns:

    """
    TEMP_FILE = get_device_full_screenshot()

    # 获取元素四角坐标
    height = G.DEVICE.display_info['height']
    width = G.DEVICE.display_info['width']
    bound = poco_element.get_bounds()
    y1 = bound[0] * height  # 右上
    x2 = bound[1] * width  # 右下
    y2 = bound[2] * height  # 左下
    x1 = bound[3] * width  # 左上

    # 截取图片
    TEMP_FILE_2 = os.path.join(tempfile.gettempdir(), f"temp_screen_{int(time.time() * 1000)}.png")
    cut_image(TEMP_FILE, x1, y1, x2, y2,
              TEMP_FILE_2)

    return TEMP_FILE_2


def get_screenshot_by_element2(poco_element, element_name,image_dir):
    """
    获取指定元素的截图(android)并保存到指定文件下
    Args:
        poco_element: 要获取截图的元素
        element_name：保存文件名
        image_dir:保存路径

    Returns:

    """
    TEMP_FILE = get_device_full_screenshot()

    # 获取元素四角坐标
    height = G.DEVICE.display_info['height']
    width = G.DEVICE.display_info['width']
    bound = poco_element.get_bounds()
    y1 = bound[0] * height  # 右上
    x2 = bound[1] * width  # 右下
    y2 = bound[2] * height  # 左下
    x1 = bound[3] * width  # 左上
    # D:\android_airtest\test_case\ceshi_tuxiangshibie
    # 截取图片
    #current_dir = os.path.dirname(__file__)
    #image_dir = os.path.join(current_dir, "..", "image")
    TEMP_FILE_2 = os.path.join(image_dir, f"{element_name}.png")
    cut_image(TEMP_FILE, x1, y1, x2, y2,
              TEMP_FILE_2)
    return TEMP_FILE_2


# def assert_color(driver, element):
#     image_path = get_screenshot_by_element(driver, element)
#     res = get_color(cv2.imread(image_path))
#     if res == 'red' or res == 'red2':
#         return 'red'
#     elif res == 'green':
#         return 'green'

from PIL import Image


def pil_resize(img, size=(256, 256)):
    """
    调整输入的图像大小并将其转换为RGB模式。

    Args:
        img (PIL.Image): 输入的图像。
        size (tuple): 指定图像的目标大小的元组。默认为(256, 256)。

    Returns:
        PIL.Image: 调整大小并转换后的图像。
    """
    return img.resize(size).convert("RGB")


def cal_hist_confidence(im_source: Image, im_search: Image):
    """
    计算两个图像之间的直方图相似度置信度。

    Args:
        im_source (PIL.Image): 源图像。
        im_search (PIL.Image): 搜索图像。

    Returns:
        float: 直方图相似度置信度。
    """

    # 切割图片
    def _split_image(img, part_size=(64, 64)):
        """
        将图像分割成多个小部分。

        Args:
            img (PIL.Image): 输入的图像。
            part_size (tuple): 每个部分的大小。默认为(64, 64)。

        Returns:
            list: 包含分割后小图像的列表。
        """
        w, h = img.size
        pw, ph = part_size
        assert w % pw == h % ph == 0
        return [
            img.crop((i, j, i + pw, j + ph)).copy()
            for i in range(0, w, pw)
            for j in range(0, h, ph)
        ]

    # 计算直方图相似度
    def _hist_similar(lh, rh):
        """
        计算两个直方图之间的相似度。

        Args:
            lh (list): 左边直方图的像素值列表。
            rh (list): 右边直方图的像素值列表。

        Returns:
            float: 直方图相似度。
        """
        return sum(
            1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)
        ) / len(lh)

    return (
            sum(
                _hist_similar(l.histogram(), r.histogram())
                for l, r in zip(_split_image(im_source), _split_image(im_search))
            )
            / 16.0
    )


def get_screenshot_by_percent(out_image_path=None, x1=0, y1=0, x2=1, y2=1):
    """
    根据百分比截取屏幕截图
    Args:
        out_image_path: 截图结果输出路径
        x1: 所要截取区域左上角坐标的横坐标占屏幕宽度的百分比。0<=x1<=1
        y1: 所要截取区域左上角坐标的纵坐标占屏幕宽度的百分比。0<=y1<=1
        x2: 所要截取区域右上角坐标的横坐标占屏幕宽度的百分比。0<=x2<=1
        y2: 所要截取区域右下角坐标的纵坐标占屏幕宽度的百分比。0<=y2<=1

    Returns:截图结果存放路径

    """
    TEMP_FILE = get_device_full_screenshot()

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


def get_color_by_element(poco_element, shield_list=None):
    """
    获取指定元素的主体颜色
    Args:
        poco_element: 要获取颜色的元素
        shield_list: 要屏蔽的颜色列表
    Returns:

    """
    return get_color(get_screenshot_by_element(poco_element), shield_list)


def ths_ocr(image_str):
    """
    ocr服务接口封装
    Args:
        image_str: 需要识别的图片对应的base64字符串
    Returns:
    """
    params = {
        "pic": image_str,
        "q": "screenshot-ocr",
        "info": '{"key_id":"05c21752547743ca9edd7d7395d9086a", "type":"general"}',
    }

    url = "http://172.19.80.109/ircommon"
    headers = {"Host": "stock-ocr.wencai", "X-Arsenal-Auth": "ifind_autotest"}

    try:
        result = requests.post(url, data=params, headers=headers)
        res = json.loads(result.content)
        return res["response"]["Rlt"]
    except:
        res = {"data": [], "text": ""}
    return res


def image_to_base64(image_path):
    """
    图片转base64字符串
    Args:
        image_path: 需要转换的图片对应的路径
    Returns:
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string


def get_text_by_ocr(poco_ele):
    """
    通过ocr获取元素文本内容
    Args:
        poco_ele: 需要获取文本的元素
    Returns:
    """
    temp_png = get_screenshot_by_element(poco_ele)
    image_str = image_to_base64(temp_png)
    results = ths_ocr(image_str)
    return results["text"]


def cal_hist_confidence(im_source: Image, im_search: Image):
    # 切割图片
    def _split_image(img, part_size=(64, 64)):
        w, h = img.size
        pw, ph = part_size
        assert w % pw == h % ph == 0
        return [
            img.crop((i, j, i + pw, j + ph)).copy()
            for i in range(0, w, pw)
            for j in range(0, h, ph)
        ]

    # HIST相似度
    def _hist_similar(lh, rh):
        return sum(
            1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)
        ) / len(lh)

    return (
            sum(
                _hist_similar(l.histogram(), r.histogram())
                for l, r in zip(_split_image(im_source), _split_image(im_search))
            )
            / 16.0
    )




if __name__ == '__main__':
    # filename = 'ios_h.png'
    # filename = 'C:\\Users\\viruser.v-desktop\\Desktop\\tmp\\white.png'
    import time

    filename1 = 'D:\\picres\\test.png'
    s_time = time.time_ns()
    # filename = 'ios_l.png'
    # filename = 'and_h.png'
    # filename = 'and_l.png'
    colors = get_color(filename1, shield_list=['white'])
    # colors = colorgram.extract(filename1, 6)
    e_time = time.time_ns()
    print(colors)
    print(e_time - s_time)
    # file_list = ['ios_h.png', 'ios_l.png', 'and_h.png', 'and_l.png']
    # for i in file_list:
    #     frame = cv2.imread(i)
    #     print(get_color(frame))
