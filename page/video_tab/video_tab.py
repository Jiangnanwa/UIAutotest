from poco.drivers.android.uiautomation import AndroidUiautomationPoco
class video_tab:
    poco=AndroidUiautomationPoco()
    video=poco("android.widget.LinearLayout").offspring("android.widget.RelativeLayout").child("android.webkit.WebView").offspring("vueWaterfall").child("android.view.View")[1]
    medlive=poco("android.widget.LinearLayout").offspring("android.widget.RelativeLayout").child("android.webkit.WebView").offspring("vueWaterfall").child("android.view.View")[0]