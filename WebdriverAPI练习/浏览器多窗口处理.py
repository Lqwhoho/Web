#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
# driver.maximize_window()
driver.get("http://www.baidu.com/")

#获得当前窗口handle
nowhandle = driver.current_window_handle

#打开注册新窗口
driver.find_element_by_name("tj_rej").click()

#获取所有窗口
allhangdles = driver.window_handles

#循环判断窗口是否为当前窗口
for handle in allhandles:
    if handle != nowhandle:
        driver.switch_to.window(handle)
        print('now register window!')

        #切换到邮箱注册标签
