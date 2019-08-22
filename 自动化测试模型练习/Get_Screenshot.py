#coding=utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")

#捕捉百度输入框异常
try:
    browser.find_element_by_id("kss").send_keys("selenium")
    browser.find_element_by_id("su").click()
except:
    browser.get_screenshot_as_file("D:\selenium练习数据\error_png.png")

browser.quit()