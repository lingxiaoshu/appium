# 
# -*- coding: utf-8 -*-
# ---
# @Project: appium
# @Software: PyCharm
# @File: mixture_app.py
# @Author: lxs
# @Time: 2023/3/27 14:02
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
    caps["udid"] = "127.0.0.1:62001"
    caps["app"] = "E:\\packages\\tools\\apk\\shop.apk"
    # 默认false，appium要对app做重签名，安装解析的时候签名校验失败，app就没有办法用了
    caps['noSign'] = True
    caps["unicodeKeyboard"] = True
    caps["resetKeyboard"] = True
    caps["newCommandTimeout"] = 600
    # 执行器 webview  h5--->chromedriver,如何确定版本？？模拟器--设置--应用--全部（拖拽可见）--android system webview
    # 如果未配置环境变量，可以手动指定
    caps['chromedriverExecutable']='E:\programdata\chrome\chromedriver74.exe'
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(30)
    return driver

def run_webview(driver:WebDriver):
    # 想要操作webview中的元素，需要先切换对应的webview的context（上下文）
    # 原生app的控件是有context，webview也是有context
    # 在安卓上webview的context名称都是在包名前面加上webview_xxx
    # 获取所有的上下文context
    contexts = driver.contexts
    print(contexts)
    # 切换上下文
    driver.switch_to.context('WEBVIEW_com.ask.android')
    time.sleep(10)
    # 定位，切换到webview中，需要用webui的定位方式进行定位即可
    driver.find_element(By.XPATH, '//*[text()="分类"]').click()



if __name__ == '__main__':
    driver=init_driver()
    run_webview(driver)