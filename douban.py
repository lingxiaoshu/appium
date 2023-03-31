# 
# -*- coding: utf-8 -*-
# ---
# @Project: appium
# @Software: PyCharm
# @File: douban.py
# @Author: lxs
# @Time: 2023/3/26 17:25
import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from init_driver import init_driver


def douban_login(driver):
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
# 整个屏幕的滑动
def swipe_on_screen(driver:WebDriver, direction = 'up'):
    '''
    整个屏幕的滑动：上下左右
    向上滑动up：y轴减少
    向下滑动down：y轴增大
    向左滑动left：x轴减少
    向右滑动right：x轴增大
    :return:
    '''
    # 获取手机分辨率
    size = driver.get_window_size()
    print('屏幕的分辨率是{}'.format(size))
    width = size['width']
    height = size['height']
    if direction == 'up':
        driver.swipe(start_x=0.5*width, start_y=0.5 * height, end_x=0.5*width, end_y=0.25*height)
    elif direction == 'down':
        driver.swipe(start_x=0.5*width, start_y=0.25 * height, end_x=0.5*width, end_y=0.75*height)
    elif direction == 'left':
        driver.swipe(start_x=0.75*width, start_y=0.5 * height, end_x=0.25*width, end_y=0.5*height)
    elif direction == 'right':
        driver.swipe(start_x=0.25*width, start_y=0.5 * height, end_x=0.75*width, end_y=0.05*height)
    else:
        raise Exception('您输入的方向不支持滑动')

# 单个元素的滑动
def birthday(driver:WebDriver):
    # 我
    driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("我")').click()
    # 云卷
    driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("云卷")').click()
    # 编辑
    driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("编辑")').click()
    # 设置个人资料
    driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("设置个人资料")').click()
    # 生日
    driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("生日")').click()
    # 选择生日框
    els = driver.find_elements(By.CLASS_NAME, 'android.widget.NumberPicker')
    # 年
    year = els[0]
    # 月
    month = els[1]
    # 日
    day = els[2]
    # 滑动
    swipe_on_element(driver, year)
    time.sleep(2)
    swipe_on_element(driver, month)
    time.sleep(2)
    swipe_on_element(driver, day)

# 单个元素的滑动
def swipe_on_element(driver:WebDriver, el, direction = 'up'):
    # 获取元素的坐标
    x1 = el.location['x']
    y1 = el.location['y']
    # 获取元素的size
    w = el.size['width']
    h = el.size['height']
    if direction == 'up':
        # 向上滑动
        driver.swipe(start_x=x1 + 0.5 * w, start_y=y1 + 0.75 * h, end_x=x1 + 0.5 * w, end_y=y1 + 0.25 * h)
    elif direction == 'down':
        driver.swipe(start_x=x1 + 0.5 * w, start_y=y1 + 0.25 * h, end_x=x1 + 0.5 * w, end_y=y1 + 0.75 * h)
    elif direction == 'left':
        driver.swipe(start_x=x1 + 0.75 * w, start_y=y1 + 0.5 * h, end_x=x1 + 0.25 * w, end_y=y1 + 0.5 * h)
    elif direction == 'right':
        driver.swipe(start_x=x1 + 0.25 * w, start_y=y1 + 0.5 * h, end_x=x1 + 0.75 * w, end_y=y1 + 0.5 * h)
    else:
        raise('输入的方向不支持滑动')

# 手势解锁滑动,调用手势方法，应用场景：设置-安全-屏幕锁定方式-图案
def gesture_unlock(driver:WebDriver):
    # 获取整个元素
    el = driver.find_element(By.ID,'com.android.settings:id/lockPattern')
    # # 获取元素的坐标
    # x1 = el.location['x']
    # y1 = el.location['y']
    # # 获取元素的size
    # w = el.size['width']
    # h = el.size['height']
    # # 滑动
    # action = TouchAction(driver)
    # action.press(x=x1+1/6*w,y=y1+1/6*h).move_to(x=x1+1/2*w,y=y1+1/6*h).\
    #         move_to(x=x1+1/2*w,y=y1+1/2*h).\
    #         move_to(x=x1+1/2*w,y=y1+5/6*h).\
    #         move_to(x=x1+5/6*w,y=y1+5/6*h).\
    #         release().perform()

    swipe_on_gesture(driver, el, pwd='01378')

def swipe_on_gesture(driver:WebDriver, el, pwd=''):
    '''
    
    :param driver: 
    :param el: 密码解锁的整个区域的元素
    :param pwd: 想要连接的点，从0开始，eg：pwd='13678'
    :return: 
    '''
    # 获取元素的坐标
    x1 = el.location['x']
    y1 = el.location['y']
    # 获取元素的size
    w = el.size['width']
    h = el.size['height']
    # 滑动
    action = TouchAction(driver)
    # 每个点的坐标列表
    gesture_list = [{'x':x1+1/6*w,'y':y1+1/6*h},{'x':x1+1/2*w,'y':y1+1/6*h},{'x':x1+5/6*w,'y':y1+1/6*h},
                    {'x':x1+1/6*w,'y':y1+1/2*h},{'x':x1+1/2*w,'y':y1+1/2*h},{'x':x1+5/6*w,'y':y1+1/2*h},
                    {'x':x1+1/6*w,'y':y1+5/6*h},{'x':x1+1/2*w,'y':y1+5/6*h},{'x':x1+5/6*w,'y':y1+5/6*h}]
    action = action.press(x=gesture_list[int(pwd[0])]['x'],y=gesture_list[int(pwd[0])]['y'])
    for i in pwd[1:]:
        action.move_to(x=gesture_list[int(i)]['x'],y=gesture_list[int(i)]['y'])
    action.release().perform()

if __name__ == '__main__':
    # 豆瓣driver
    driver = init_driver()
    # douban_login(driver)
    # time.sleep(3)
    # swipe_on_screen(driver)
    # swipe_on_screen(driver,direction='left')
    # birthday(driver)
    time.sleep(8)
    # 启动指定的包名和界面名
    driver.start_activity('com.android.settings', 'com.android.settings.ChooseLockPattern')
    gesture_unlock(driver)