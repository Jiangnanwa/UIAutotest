#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    network_operations.py 
   Description :
   Author : chenqiyue,zengwenxin
   CreateDate：2023/12/07  用例id:
-------------------------------------------------
"""
import subprocess

from airtest.core.api import stop_app, start_app, sleep, swipe


def goto_network_settings(poco):
    stop_app("com.android.settings")
    start_app("com.android.settings")
    poco(text="WLAN").wait().click()


def connect_to_10jqka(poco):
    if poco(nameMatches="10JQKA,已连接.*").exists():
        pass
    else:
        poco(text="10JQKA").wait().click()
        poco(text="连接").wait().click()


def network_switch_10jqka(poco):
    goto_network_settings(poco)
    connect_to_10jqka(poco)
def is_wifi_connected(poco):#判断wifi是否连接
    network_status = poco.device.shell("dumpsys connectivity")
    # 提取 NetworkAgentInfo 部分
    start_index = network_status.find("NetworkAgentInfo")
    end_index = network_status.find("Nat464Xlat")
    network_agent_info= network_status[start_index:end_index]

    print(network_agent_info)
    """
    判断 Wi-Fi 是否连接
    """
    # 检查是否包含 "WIFI CONNECTED" 字符串
    if "WIFI CONNECTED" in network_agent_info:
        return True
    else:
        return False
def disable_wifi(poco):#关闭Wi-Fi连接
    global network_agent_info
    poco.device.shell("svc wifi disable")
    sleep(3)
    info=is_wifi_connected(poco)
    print(info)
def enable_wifi(poco):#打开Wi-Fi连接
    poco.device.shell("svc wifi enable")
    sleep(3)
    info = is_wifi_connected(poco)
    print(info)


def lockunlock_screen(poco):
    poco.device.shell("input keyevent 26")
    sleep(3)
    poco.device.shell("input keyevent 26")
    swipe((300, 2000), (300, 300))
    # def connect_to_wifi(poco,ssid):#连接到指定wifi，ssid为Wi-Fi名称，eg：connect_to_wifi("3015")
#     # enable_wifi(poco)
#     # sleep(10)
#     # 构造连接到指定 Wi-Fi 网络的命令
#     cmd = "adb shell am start -n com.android.settings/.wifi.WifiSettings -e ssid \"3015\""
#
#     # 执行ADB命令，并捕获标准输出和标准错误信息
#     result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
#
#     # 输出命令执行结果
#     print("标准输出：", result.stdout)
#     print("标准错误：", result.stderr)
