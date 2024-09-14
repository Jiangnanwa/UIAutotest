from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time
from airtest.utils.logger import get_logger
from airtest.core.api import *

import yaml
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


class MainPage:
    poco = AndroidUiautomationPoco()
    sleep(0.5)
    if exists(Template(r"tpl1678354080160.png", record_pos=(0.201, 0.557), resolution=(1080, 2400))):
        touch(Template(r"tpl1678354142802.png", record_pos=(0.199, 0.556), resolution=(1080, 2400)))
    sleep(0.5)
    if exists(Template(r"tpl1678354274760.png", record_pos=(-0.025, -0.553), resolution=(1080, 2400))):
        touch(Template(r"tpl1678354274760.png", record_pos=(-0.025, -0.553), resolution=(1080, 2400)))
    sleep(0.5)
    if exists(Template(r"tpl1678354337696.png", record_pos=(0.008, -0.588), resolution=(1080, 2400))):
        touch(Template(r"tpl1678354337696.png", record_pos=(0.008, -0.588), resolution=(1080, 2400)))
    sleep(3)
    touch(Template(r"tpl1678354418691.png", record_pos=(0.347, -0.58), resolution=(1080, 2400)))
