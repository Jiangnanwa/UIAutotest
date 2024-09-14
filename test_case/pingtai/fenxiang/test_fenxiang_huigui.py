# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """
# -------------------------------------------------
#    File Name：    fenxiang_huigui
#    Description :TC_29（分享）
#    Author : wangsutong
#    CreateDate：2024/03/18  用例id:732582
#
# -------------------------------------------------
# """
#
# # 1、首页feed中点击任意资讯进入底层页
# # 2、点击右下角分享按钮，选择微信分享
# # 3、打开分享内容，同花顺关闭情况下，进行回流
# # 4、打开分享内容，同花顺在后台情况下，进行回流
# def test_fenxiang_huigui_zixun(poco):
#     poco.swipe([0.5, 0.8], [0.5, 0.2])
#     # 获取屏幕的宽度和高度
#     screen_width, screen_height = poco.get_screen_size()
#
#     # 定位到屏幕高度的一半位置
#     # 这里我们假设宽度不变，仍然点击屏幕中央，因此x坐标是0.5（即屏幕宽度的一半）
#     # y坐标根据屏幕高度计算，假设点击屏幕高度的50%的位置
#     x = 0.5
#     y = 0.5  # 例如，屏幕高度的50%
#
#     # 执行点击操作
#     poco.click([x, y])
#     poco("android.view.ViewGroup").click()
#     poco(text="微信").click()
#     # poco("android.view.ViewGroup").click()
#     # poco("android:id/content").offspring("com.hexin.plat.android:id/first_line").child("android.view.ViewGroup")[
#     #     0].child("com.hexin.plat.android:id/share_icon").click()
#     poco(text="文件传输助手").click()
#     poco("com.tencent.mm:id/mm_alert_ok_btn").click()
#     poco("com.tencent.mm:id/mm_alert_ok_btn").click()
#     poco(text="文件传输助手").click()
#     poco("com.tencent.mm:id/bp0").click()
#     poco("backBanner").click()
#     poco("com.tencent.mm:id/fq").click()
#     poco(text="在浏览器打开").click()
#     #打开分享内容，同花顺在后台情况下，进行回流
#     poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.tencent.mm:id/ayy").child(
#         "com.tencent.mm:id/ayx")[0].child("com.tencent.mm:id/ayw").click()
#     poco("com.huawei.browser:id/tv_snack_bar_btn_text").click()
#     element_text=poco("com.hexin.plat.android:id/title_bar_middle").get_text()
#     if element_text not in ["同花顺资讯", "正文"]:
#         raise AssertionError("元素的文本内容既不是'同花顺资讯'也不是'正文'！")
# # 1、进入300033分时，选择公告tab，在tab内选择任一公告
# # 2、进入公告底层页点击分享按钮，选择qq分享
# # 3、打开分享内容，同花顺关闭情况下，进行回流
# # 4、打开分享内容，同花顺在后台情况下，进行回流
#     def test_fenshi_fengxiang():
#
#
