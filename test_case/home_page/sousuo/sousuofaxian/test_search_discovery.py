import pytest

# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_search_discovery
   Description：   
   Author：      chenqiyue
   CreateDate：   2024/7/16  
   CaseID：       1898175
-------------------------------------------------
"""
from airtest.core.api import touch, keyevent, sleep
from airtest.core.cv import Template
from common.app_operation import stop_app_open_app, back_findelement


def test_search_discovery(poco):
    """
       CaseID：       1898175
        用例名称  TC_搜索发现_功能校验（回归用例）
    """

    # 如果搜索发现元素不存在，则点击隐藏按钮
    if not poco("com.hexin.plat.android:id/sentence").exists():
        touch(Template(r"tpl1721115597267.png", record_pos=(0.434, -0.282), resolution=(1080, 2400)))

    # 点击四个搜索发现的内容，并记录点击的text值
    sentence_texts = []
    for i in range(4):
        sentences = poco("com.hexin.plat.android:id/sentence")
        if len(sentences) > i:
            sentence = sentences[i]
            sentence_texts.append(sentence.get_text())
            sentence.click()
            if poco("com.hexin.plat.android:id/close_image").exists():

                poco("com.hexin.plat.android:id/close_image").click()
            else:
                back_findelement(poco(text="综合"))

    # 校验历史记录是否按照点击顺序的倒序展示
    history_texts = [ele.get_text() for ele in poco("com.hexin.plat.android:id/name")][:4]
    # 检查历史记录是否有与点击文本倒序一致的情况
    match_found = False
    for i in history_texts[i:i + len(sentence_texts)]:
        print(i)

        print(sentence_texts[::-1])
        if i in sentence_texts[::-1]:
            match_found = True
            break
    assert match_found, "历史记录展示顺序错误"

    # 重复点击四个搜索发现的内容后点击换一换按钮，并校验历史记录是否变化
    for _ in range(4):
        sentences = poco("com.hexin.plat.android:id/sentence")
        if len(sentences) > 0:
            sentence = sentences[0]
            sentence.click()
            if poco("com.hexin.plat.android:id/close_image").exists():

                poco("com.hexin.plat.android:id/close_image").click()
            else:
                keyevent("BACK")

    poco("com.hexin.plat.android:id/refresh_btn").click()
    new_history_texts = [ele.get_text() for ele in poco("com.hexin.plat.android:id/name")]
    assert new_history_texts != history_texts, "历史记录未随换一换按钮变化"

    # 点击隐藏按钮，校验搜索发现模块是否消失
    poco("com.hexin.plat.android:id/dissmiss_btn").click()
    assert not poco("com.hexin.plat.android:id/sentence").exists(), "搜索发现模块未隐藏"

    # 切换股票tab和综合tab，校验搜索发现模块是否消失
    poco(text="股票").click()
    poco(text="综合").click()
    assert not poco("com.hexin.plat.android:id/sentence").exists(), "搜索发现模块在tab切换后未隐藏"

    # 重启App后校验搜索发现模块是否消失
    stop_app_open_app("com.hexin.plat.android")
    sleep(5.0)
    poco("com.hexin.plat.android:id/text_switcher").click()
    assert not poco("com.hexin.plat.android:id/sentence").exists(), "重启App后搜索发现模块未隐藏"
