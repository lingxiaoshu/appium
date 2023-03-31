# 
# -*- coding: utf-8 -*-
# ---
# @Project: appium
# @Software: PyCharm
# @File: douban_luzhi.py
# @Author: lxs
# @Time: 2023/3/12 0:34
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

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

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(30)
el1 = driver.find_element_by_id("com.douban.frodo:id/confirm")
el1.click()
driver.implicitly_wait(30)
el2 = driver.find_element_by_id("com.douban.frodo:id/tvAction")
el2.click()
el3 = driver.find_element_by_id("com.douban.frodo:id/entire_password_login_text")
el3.click()
el4 = driver.find_element_by_id("com.douban.frodo:id/input_user_name")
el4.send_keys("18811536608")
el5 = driver.find_element_by_id("com.douban.frodo:id/input_password")
el5.send_keys("q1w2e3r4@@")
el6 = driver.find_element_by_id("com.douban.frodo:id/sign_in_douban")
el6.click()
try:
    el7 = driver.find_element_by_id("android:id/button2")
    el7.click()
except:
    print("NoSuchElementException")
driver.quit()