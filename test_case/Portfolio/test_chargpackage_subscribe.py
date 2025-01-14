# -*- encoding=utf8 -*-

from time import sleep
from common.open_product import Open_product

# 下单成功
def test_subscribe(poco):
    Open_product(poco,"https://t.10jqka.com.cn/pkgfront/tgService.html?type=package&id=6404")
    try:
        poco(text="订阅").wait_for_appearance(timeout=20)
        poco(text="订阅").click()
    except Exception as e:
        print(e, "当前已订阅付费服务包，可以续费")

    # else块：如果try块中的代码没有引发任何异常，可以执行else块中的代码。
    else:
        try:
            poco(text="续费").wait_for_appearance(timeout=20)
            poco(text="续费").click()
        except Exception as e:
            print(e, "当前不可订阅")

    #无论是否发生异常，finally块中的代码都会被执行
    finally:
        # 实名风测可订阅
        if poco(text="投顾服务订阅").exists():
            poco(text="我已阅读并同意").click()
            sleep(2)
            if poco(text="存在待支付订单，是否继续完成支付?").exists():
                poco(text="重新下单").click()
            assert poco(textMatches="订阅服务包\d+个月").exists()
            poco(textMatches="支付-?\d+\.\d+元").click()
            sleep(3)
            if poco(text="已完成支付").exists():
                poco(text="已完成支付").click()
                if poco(text="放弃购买").exists():
                    poco(text="放弃购买").click()
            else:
                print("生成订单失败")

        # 所有人可订阅
        else:
            if poco(text="存在待支付订单，是否继续完成支付?").exists():
                poco(text="重新下单").click()
            assert poco(textMatches="订阅服务包\d+个月").exists()
            poco(textMatches="支付-?\d+\.\d+元").click()
            sleep(3)
            if poco(text="已完成支付").exists():
                poco(text="已完成支付").click()
                if poco(text="放弃购买").exists():
                    poco(text="放弃购买").click()
            else:
                print("生成订单失败")


# 使用历史订单继续支付
def test_Historical_order_subscribe(poco):
    try:
        poco(text="订阅").wait_for_appearance(timeout=20)
        poco(text="订阅").click()
    except Exception as e:
        print(e, "当前已订阅付费服务包，可以续费")
    else:
        try:
            poco(text="续费").wait_for_appearance(timeout=20)
            poco(text="续费").click()
        except Exception as e:
            print(e, "当前不可订阅")
    finally:
        if poco(text="存在待支付订单，是否继续完成支付?").exists():
            poco(text="继续支付").click()
        assert poco(textMatches="订阅服务包\d+个月").exists()
        poco(textMatches="支付-?\d+\.\d+元").click()
        sleep(3)
        if poco(text="已完成支付").exists():
            poco(text="已完成支付").click()
            if poco(text="放弃购买").exists():
                poco(text="放弃购买").click()




