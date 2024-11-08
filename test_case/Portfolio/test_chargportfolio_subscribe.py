# -*- encoding=utf8 -*-

from time import sleep
from common.open_product import Open_product

# 下单成功
def test_subscribe(poco):
    Open_product(poco,"https://t.10jqka.com.cn/pkgfront/tgService.html?type=portfolio&id=1751")
    try:
        poco(text="订阅").wait_for_appearance(timeout=20)
        poco(text="订阅").click()
    except Exception as e:
        print(e, "当前已订阅付费组合，可以续费")
    else:
        try:
            poco(text="续费").wait_for_appearance(timeout=20)
            poco(text="续费").click()
        except Exception as e:
            print(e, "当前不可订阅")
    finally:
        if poco(text="投顾服务订阅").exists():
            poco(text="确认").click()
            if poco(text="评估结果").exists():
                poco(text="我已阅读并同意").click()
                sleep(2)
                if poco(text="存在待支付订单，是否继续完成支付?").exists():
                    poco(text="重新下单").click()
                assert poco(textMatches="订阅组合\d+个月").exists()
                poco(textMatches="支付-?\d+\.\d+元").click()
                sleep(3)
                if poco(text="已完成支付").exists():
                    poco(text="已完成支付").click()
                    if poco(text="放弃购买").exists():
                        poco(text="放弃购买").click()
                else:
                    print("生成订单失败")
            else:
                print("适当性匹配打开失败")
        else:
            print("进入风测确认页面失败")


# 使用历史订单继续支付
def test_Historical_order_subscribe(poco):
    try:
        poco(text="订阅").wait_for_appearance(timeout=20)
        poco(text="订阅").click()
    except Exception as e:
        print(e, "当前已订阅付费组合，可以续费")
    else:
        try:
            poco(text="续费").wait_for_appearance(timeout=20)
            poco(text="续费").click()
        except Exception as e:
            print(e, "当前不可订阅")
    finally:
        if poco(text="存在待支付订单，是否继续完成支付?").exists():
            poco(text="继续支付").click()
        assert poco(textMatches="订阅组合\d+个月").exists()
        poco(textMatches="支付-?\d+\.\d+元").click()
        sleep(3)
        if poco(text="已完成支付").exists():
            poco(text="已完成支付").click()
            if poco(text="放弃购买").exists():
                poco(text="放弃购买").click()




