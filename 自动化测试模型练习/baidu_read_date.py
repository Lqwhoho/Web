#coding = utf -8
from selenium import webdriver
import time

source = open("D:\\selenium练习数据\\date.txt","r")
values = source.readlines()
source.close()

#执行循环
for search in values:
    browser = webdriver.Firefox()
    browser.get("http://www.baidu.com")
    browser.find_element_by_id("kw").send_keys(search)
    browser.find_element_by_id("su").click()
    time.sleep(2)
    browser.quit()

