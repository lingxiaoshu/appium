# 
# -*- coding: utf-8 -*-
# ---
# @Project: appium
# @Software: PyCharm
# @File: init_driver.py
# @Author: lxs
# @Time: 2023/3/26 17:24
from appium import webdriver
def init_driver():


    # 启动项
    caps = {}
    # 平台名字：android ios
    caps["platformName"] = "android"
    # 设备名字：安卓任写非空
    caps["deviceName"] = "xxx"
    caps["udid"] = "127.0.0.1:62001"
    caps["app"] = "E:\\packages\\tools\\apk\\douban_7.0.apk"
    # 默认false，appium要对app做重签名，安装解析的时候签名校验失败，app就没有办法用了
    caps['noSign'] = True
    caps["unicodeKeyboard"] = True
    caps["resetKeyboard"] = True
    caps["newCommandTimeout"] = 600
    # 自动授权
    caps['autoGrantPermissions'] = True

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(30)
    return driver