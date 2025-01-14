# -*- encoding=utf8 -*-
from time import sleep
from numpy.testing import assert_equal
from common.open_product import Open_product




# 进入投顾首页
def test_indexofpage(poco):
    Open_product(poco, "https://t.10jqka.com.cn/rankfront/rankHomepage/index.html")
    sleep(5)
    assert poco(text="投顾首页").exists()


# 会员中心入口
def test_vip_entrance(poco):
    try:
        poco(text="投顾会员中心").wait_for_appearance(timeout=20)
    except Exception as e:
        print(e, "未找到会员中心")
    else:
        # 找到即点击进入
        poco(text="投顾会员中心").click()
        sleep(5)
        assert poco(text="投顾会员").exists()
        poco("com.hexin.plat.android:id/title_bar_left_container").click()


# 用户关注头像
def test_follow_list(poco):
    try:
        assert poco(text="我的服务").exists()
        assert poco(text="avatar").exists()
        poco(text="我的服务").wait_for_appearance(timeout=20)
    except Exception as e:
        print(e, "未找到我的关注列表")
    else:
        # 找到即点击进入
        poco(text="我的服务").click()
        sleep(5)
        assert poco(text="我的订阅").exists()
        poco("com.hexin.plat.android:id/title_bar_left_container").click()


# 榜单主tab
def test_toptab(poco):
    existtablist=[]
    elements = [
        {"text": "精选组合"},
        {"text": "人气投顾"},
        {"text": "解盘"},
    ]
    for element in elements:
        try:
            assert poco(**element).exists(), f"元素'{element['text']}'不存在"
            existtablist.append(element['text'])
        except AssertionError as e:
            print(f"警告：{e}")
    try:
        assert len(existtablist)==2
    except AssertionError as e:
        print(e,"主tab个数错误")

# 精选组合子tab校验
def test_portfolio_subtab(poco):
    subtab_list=[]
    try:
        # 获取子tab的名称
        for c in poco("android.widget.TabWidget")[1].child("android.view.View"):
            subtab_list.append(c.get_text())
    except Exception as e:
        print(e, "不存在精选组合子tab")
    else:
        poco(text=subtab_list[1]).click()
        sleep(5)



# 切换收益率
def test_change_income(poco):
    try:
        poco(text="周收益").wait_for_appearance(timeout=20)
    except Exception as e:
        print(e,"不存在切换收益")
        poco(text="周收益").parent().click()
        sleep(5)
        poco(text="总收益").click()

# 精选组合列表校验
def test_portfolio_list(poco):
    try:
        cardindex = poco(text="2")
        cardUI = cardindex.sibling()
        # 记录不存在的元素
        missing_elements = []
        cardUIlength = len(cardUI.children())
        portfolio_name = cardUI.child()[0]
        label1 = cardUI.child()[1]
        label2 = cardUI.child()[2]
        user_name = cardUI.child()[3]
        portfolio_income = cardUI.child()[4]
        if cardUIlength > 6:
            operation = cardUI.child()[6]
            star = cardUI.child()[7]
            price = cardUI.child()[8]
            price_num = cardUI.child()[9]
            stock_income = cardUI.child()[10]
            stock_income_num = cardUI.child()[11]
    except Exception as e:
        print(e,"组合卡片元素缺少")


def test_portfolio_entrance(poco):
    try:
        poco(text="1").click()
        sleep(5)
        assert poco(text="产品详情").exists()
    except Exception as e:
        print(e,"进入组合失败")
    else:
        poco("com.hexin.plat.android:id/title_bar_left_container").click()


def test_popularity(poco):
    poco(text="人气投顾").click()
    sleep(5)
    try:
        first = poco(text="1")
        assert first.parent().child()[1].child()[0].exists()
        user_name = first.parent().child()[1].child()[0].get_text()
        assert poco(text=user_name).sibling().child(textMatches=".+万热度").exists()
        product = first.parent().child()[2].child()
        product_info = []
        for element in product.children():
            if element.get_text():
                product_info.append(element.get_text())
        print(product_info)
        assert len(product_info) == 2

    except Exception as e:
        print(e, "人气投顾页面异常")
    else:
        try:
            # 进入投顾主页
            poco(text=user_name).click()
            sleep(3)
            assert_equal(poco("userInfo").exists(), True, "判断进入了投顾个人主页")
        except Exception as e:
            print(e, "进入用户个人主页异常")
        else:
            poco("userInfo").child()[0].child()[0].click()
            sleep(3)

        # 进入产品详情页
        try:
            poco(text=product_info[0]).click()
            sleep(3)
            assert poco(text="产品详情").exists()
        except Exception as e:
            print(e, "进入产品详情页异常")
        else:
            poco("com.hexin.plat.android:id/title_bar_left_container").click()








