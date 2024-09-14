# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """
# -------------------------------------------------
#    File Name：    test_zixuan_xinwen
#    Description :
#    Author : chenqiyue
#    CreateDate：2024/02/28  用例id:
# -------------------------------------------------
# """
# from PIL.Image import Image
# from airtest.core.api import sleep
#
# from common.common_image import take_screenshot, crop_element, get_non_excluded_color, get_element_position_and_size
#
#
# def test_zixuan_xinwen(poco):
#     """
#     用例名称
#     TC_自选_二级页面新闻_点击跳转（已实现自动化）
#     用例id
#     1270255
#     """
#     poco("com.hexin.plat.android:id/xinwen").click()
#     poco("com.hexin.plat.android:id/tv_content").click()
#     poco("com.hexin.plat.android:id/title_bar_img").click()
#     sleep(2.0)
#     element = poco("com.hexin.plat.android:id/tv_content")
#     #
#     # # 截取整个屏幕的截图
#     # screenshot_path = take_screenshot()
#     #
#     # # 获取元素的位置和大小信息
#     # element_position, element_size = get_element_position_and_size(element)
#     # print(element_position,element_size)
#     # # 根据元素的位置和大小信息裁剪出元素的截图
#     # element_image = crop_element(screenshot_path, element_position, element_size)
#     #
#     # # 保存元素的截图
#     # element_image.save("element_screenshot.png")
#     # excluded_color = [255, 255, 255]
#     # non_excluded_colors = get_non_excluded_color("element_screenshot.png", excluded_color)
#     # print("非排除颜色的 RGB 值:", non_excluded_colors)
#     # 使用 Airtest 获取截图
#     screenshot_image = poco.snapshot()
#
#     # 将截图转换为 Pillow 的 Image 对象
#     pil_image = Image.frombytes("RGB", screenshot_image.size, screenshot_image.tostring())
#
#     # 获取特定位置的像素颜色
#     pixel_color = pil_image.getpixel((981, 771))  # (x, y) 为像素的坐标
#
#     # 检查像素颜色是否符合预期
#     expected_color = (255, 0, 0)  # 期望的颜色为红色
#     if pixel_color == expected_color:
#         print("Pixel color matches expected color.")
#     else:
#         print("Pixel color does not match expected color.")