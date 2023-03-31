# 
# -*- coding: utf-8 -*-
# ---
# @Project: appium
# @Software: PyCharm
# @File: h5.py
# @Author: lxs
# @Time: 2023/3/27 14:56
import time

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


def init_driver():
    # 启动项
    caps = {}
    # 平台名字：android ios
    caps["platformName"] = "android"
    # 设备名字：安卓任写非空
    caps["deviceName"] = "xxx"
    caps["udid"] = "5AFBB18914515934"  # 真机
    caps["udid"] = "127.0.0.1:62001"
    # caps["app"] = "E:\\packages\\tools\\apk\\shop.apk"
    # 默认false，appium要对app做重签名，安装解析的时候签名校验失败，app就没有办法用了
    # caps['noSign'] = True
    caps["unicodeKeyboard"] = True
    caps["resetKeyboard"] = True
    caps["newCommandTimeout"] = 600
    # 原生h5 需要查看chrome的版本
    # 浏览器名称
    caps['browserName'] = 'chrome'
    # 谷歌浏览器的配置项
    caps['chromeOptions'] = {'w3c': False}
    # 浏览器驱动
    caps['chromedriverExecutable'] = 'E:\programdata\chrome\chromedriver81.exe'

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(30)
    return driver

if __name__ == '__main__':
    driver = init_driver()
    driver.get('http://www.baidu.com')
    driver.find_element(By.CSS_SELECTOR, 'input#index-kw').send_keys('赵丽颖')