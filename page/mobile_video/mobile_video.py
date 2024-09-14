from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from page.main_page import MainPage
class MobileVideo:
    poco=AndroidUiautomationPoco()
    #返回按钮
    back_button=poco("com.hexin.plat.android:id/back_icon")
    #切换横屏
    land_screen = poco("com.hexin.plat.android:id/land_screen")
    #作者头像
    author_icon=poco("com.hexin.plat.android:id/author_icon")
    #头像关注按钮
    author_state=poco("com.hexin.plat.android:id/author_state")
    #点赞按钮
    like_icon = poco("com.hexin.plat.android:id/like_icon")
    #已点赞按钮
    has_agree_icon=poco("com.hexin.plat.android:id/hsa_agree_icon")
    #评论按钮
    short_video_comment_icon=poco("com.hexin.plat.android:id/short_video_comment_icon")
    #评论数量
    comment_number=poco("com.hexin.plat.android:id/comment_number")
    #视频分享按钮
    video_traffic_share_icon=poco("com.hexin.plat.android:id/video_traffic_share_icon")
    #播放按钮
    play_center=poco("com.hexin.plat.android:id/play_center")
    #视频播放窗口
    ijkplayer=poco("com.starnet.livestream.ijkplayer.video.TextureRenderView")
    #作者名称
    author_name=poco("com.hexin.plat.android:id/author_name")
    #创作日期
    video_date=poco("com.hexin.plat.android:id/video_date")
    #视频简介
    video_des=poco("com.hexin.plat.android:id/video_des")
    #视频须知
    need_to_know=poco("com.hexin.plat.android:id/need_to_know")
    #小窗按钮
    float_box=poco("com.hexin.plat.android:id/float_box")