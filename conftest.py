#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：conftest.py
   Description :
   Author : chenqiyue
   CreateDate：2023/04/03
   用例id:
------------------------------------------------
"""
import pytest

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


@pytest.fixture(scope="session", autouse=True)
def poco():
    print("连接安卓设备")
    connect_device("Android:///")
    poco_obj = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    yield poco_obj


def pytest_collection_modifyitems(items):
    for item in items:
        if 'test_' in item.nodeid:
            # 给每个测试用例添加重试装饰器
            item.add_marker(pytest.mark.flaky(reruns=3))
            print(f"Added flaky marker to test: {item.nodeid}")