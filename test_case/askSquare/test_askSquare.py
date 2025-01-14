from time import sleep
from common.open_product import Open_product
import re



# 进入问答广场
def test_indexofpage(poco):
    Open_product(poco, "https://t.10jqka.com.cn/askfront/askSquare.html")
    sleep(5)
    assert poco(text="问答广场").exists()


# 区分新版问答/旧版问答
def test_ask_head_element(poco):
    try:
        poco(text="投顾会员免费问答").wait_for_appearance(timeout=20)
    except Exception as e:
        print(e, "目前是旧版问答广场")
    else:
        # 找到即点击进入
        # 会员入口
        assert poco(name="app").child()[1]
        global vip_enter
        vip_enter=poco(name="app").child()[1]

        label=poco(text="问")
        parent_label=label.parent()
        question=parent_label.child()[0].child()
        global question_text
        question_text=question.get_text()
        # 投顾昵称
        assert parent_label.child()[3].exists()
        global advisorName
        advisorName=parent_label.child()[3].get_text()
        # 投顾标签
        assert parent_label.child()[4].exists()
        # 投顾擅长
        assert poco(text="擅长：").exists()
        # 投顾擅长标签
        assert parent_label.child()[6].child().exists()
        global description
        description="擅长："+parent_label.child()[6].child().get_text()

        # 评价
        assert poco(text="评价").exists()
        # 评价分数
        assert parent_label.child()[8].exists()
        global score
        score=parent_label.child()[8].get_text()
        # 回答问题数量
        assert poco(text="回答问题").exists()
        assert parent_label.child()[10].exists()
        # 平均响应时长
        assert poco(text="平均响应").exists()
        assert poco(textMatches="\d+分钟").exists()

# 进入会员中心
def test_vipenter(poco):
    try:
        vip_enter.wait_for_appearance(timeout=20)
    except Exception as e:
        print(e, "未找到会员入口")
    else:
        vipname=vip_enter.get_text()
        poco(text=vipname).click()
        sleep(3)
        assert poco(name="com.hexin.plat.android:id/title_bar_middle").get_text()=="投顾会员"
        poco(name="com.hexin.plat.android:id/title_bar_left_container").click()
        sleep(3)


# 问答头部定向提问
def test_targeted_question(poco):
    try:
        poco(text="问").wait_for_appearance(timeout=20)
    except Exception as e:
        print(e, "未找到定向提问入口")
    else:
        poco(text="问").click()
        sleep(3)
        assert poco(text=advisorName).exists()
        assert poco(text=score).exists()
        assert poco(text=description).exists()
        assert poco(name="android.widget.EditText").get_text()==question_text
        poco(name="com.hexin.plat.android:id/title_bar_left_container").click()
        sleep(3)


# 去提问列表
def test_question_enterance(poco):
    try:
        poco(textMatches="\d+位在线").wait_for_appearance(timeout=20)
    except Exception as e:
        print(e,"未找到普通提问入口")
    else:
        assert poco(text="去提问").exists()
        poco(text="去提问").click()
        sleep(3)
        assert poco(name="com.hexin.plat.android:id/title_bar_middle").get_text()=="提问"
        assert poco(name="android.widget.EditText").exists()
        poco(name="com.hexin.plat.android:id/title_bar_left_container").click()
        sleep(3)

# 我的问题
def test_MyQuestion(poco):
    try:
        poco(text="我的问题").wait_for_appearance(timeout=20)
    except Exception as e:
        print(e,"未找到我的提问入口")
    else:
        assert poco(text="我的问题").exists()
        poco(text="我的问题").click()
        sleep(3)
        assert poco(name="com.hexin.plat.android:id/title_bar_middle").get_text()=="我的"
        assert poco(text="我的提问").exists()
        assert poco(text="付费解锁").exists()
        poco(name="com.hexin.plat.android:id/title_bar_left_container").click()
        sleep(3)







# 问答列表，调试到这里！！！！！！！！！！！！！！！！！！！

def test_questionlist(poco):
    try:
        questionlist = poco(name="android.widget.ListView").wait_for_appearance(timeout=20)
    except Exception as e:
        print(e,"不存在问答列表")
    else:
        # 问题
        assert questionlist.child()[0].child()[0].child()[0].exists()
        question=questionlist.child()[0].child()[0].child()[0]
        # 问题对应的股票
        assert questionlist.child()[0].child()[0].child()[1].child().exists()
        stock = questionlist.child()[0].child()[0].child()[1].child()
        # 申明全局变量
        global stockinfo
        stockinfo=stock.get_text()

        # 投顾提问入口
        assert poco(text="向他提问").exists()
        # 投顾相关信息
        advisorlist=poco(text="向他提问").parent().sibling()
        # 投顾头像
        assert advisorlist.child(name="android.widget.Image").exists()
        # 投顾昵称
        assert advisorlist.child()[1].exists()
        global advisorname
        advisorname = advisorlist.child()[1].get_text()

        assert poco(text="回答").exists()
        assert poco(textMatches="\d+分钟前").exists()

# 进入问答底层页



# 进入分时新闻
def test_enterfenshi(poco):
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    stockname = pattern.findall(stockinfo)
    try:
        stockinfo.click()
    except Exception as e:
        print(e, "问答下不存在匹配股票信息")
    else:
        sleep(3)
        assert poco(text=stockname).exists()
        poco("com.hexin.plat.android:id/backButton").click()
        sleep(3)

# 进入投顾个人主页
def test_enter_userpage(poco):
    try:
        advisorname.click()
    except Exception as e:
        print(e, "问答下不存在投顾信息")
    else:
        sleep(3)
        assert poco(text="同花顺-个人主页").exists()
        assert poco(text=advisorname).exists()
        poco(name="user-navigation").child()[1].child()[0].click()
        sleep(3)

# 进入问答定向提问页
def test_enter_questionpage(poco):
    try:
        poco(text="向他提问").wait_for_appearance(timeout=20)
    except Exception as e:
        print(e, "问答下不存在投顾定向提问入口")
    else:
        poco(text="向他提问").click()
        sleep(3)
        assert poco(text=advisorname).exists()
        assert poco(name="android.widget.EditText").exists()
        poco(name="com.hexin.plat.android:id/title_bar_left_container").click()
        sleep(3)









