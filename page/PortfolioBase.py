# -*- encoding=utf8 -*-
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

class PortfolioPage:
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


    # 组合基础信息
    product_name = poco(text="创建组合032的")
    unsubscribed_button = poco(text="已订阅")
    subscribed_button = poco(text="订阅")
    product_slogan = poco(text="累计抓涨停20次")
    product_labels = poco(text="长线抓涨停准")

    # 组合分享按钮
    share_button = poco("android.view.ViewGroup").click()
    cancel_btn = poco("com.hexin.plat.android:id/cancel_btn").click()

    # 投顾信息以及群信息
    avater = product_labels.parent().child()[5]
    principal_info = product_labels.parent().child()[6]
    principalchildren = principal_info.children()

    channelName = principalchildren[0]
    verifyType = principalchildren[1]
    description = principalchildren[2]

    group_info = product_labels.parent().child()[7]
    groupchildren = group_info.children()
    group_name = groupchildren[1]
    group_text = groupchildren[3]
    print(group_text.get_text())

    # 滑动屏幕
    poco.swipe([0.5, 0.5], [0.5, 0.3], duration=0.5)

    # 组合简介以及业绩走势
    introduce = poco(text="组合简介")
    productDesc = introduce.parent().child()[1]

    createAt = introduce.parent().child()[3]
    totalIncomeRate = introduce.parent().child()[5]
    dailyIncomeRate = introduce.parent().child()[7]
    maxDrawdownRate = introduce.parent().child()[9]
    PortfolioIncomeInfo = introduce.sibling()[12]
    change_Income = poco(text="近半年")

    # 滑动屏幕
    poco.swipe([0.5, 0.5], [0.5, 0.3], duration=0.5)

    #  组合持仓
    Relocatelist = poco(textMatches="查看全部.*只")
    Relocatelist1 = Relocatelist.parent().parent().child()[18]
    print(Relocatelist1.get_text())
    industry_info_chart = Relocatelist.parent().parent().child()[19]
    industry_info_data = Relocatelist.parent().parent().child()[20]
    bestRelocate = Relocatelist.parent().parent().child()[21]

    # 滑动屏幕
    poco.swipe([0.5, 0.5], [0.5, 0.2], duration=0.5)

    # 组合历史调仓
    histoty_relocate_list = poco(text="历史调仓")
    newest_relocate_post = poco(text="最近调仓")

    # 滑动屏幕
    poco.swipe([0.5, 0.5], [0.5, 0.2], duration=0.5)

    # 组合数据分析模块
    portfolio_profit_probability = poco(text="盈利概率")
    portfolio_profitability = poco(text="收益能力")



    