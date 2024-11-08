# -*- encoding=utf8 -*-
# 华为mate40 pro
from time import sleep
from common.open_product import Open_product

def test_cancel_subscribe(poco):
    Open_product(poco,"https://t.10jqka.com.cn/pkgfront/tgService.html?type=package&packageid=5212")
    try:
        poco(text="已订阅").wait_for_appearance(timeout=20)
        poco(text="已订阅").click()
        poco(text="确定").click()
    except Exception as e:
        print(e, "未订阅")
    finally:
        sleep(3)
        assert poco(text="订阅").exists()

def test_subscribe(poco):
    try:
        poco(text="免费订阅").wait_for_appearance(timeout=20)
        poco(text="免费订阅").click()
    except Exception as e:
        print(e, "当前已订阅，不存在订阅按钮")
    else:
        try:
            poco(text="风险提示").wait_for_appearance(timeout=20)
            poco(text="同意并订阅").click()
        except Exception as e:
            print(e, "不存在签署协议弹窗")
    finally:
        sleep(3)
        assert poco(text="已订阅").exists()
