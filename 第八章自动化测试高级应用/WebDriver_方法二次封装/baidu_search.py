#coding=utf-8
from selenium import webdriver
import time
import sys
sys.path.append('\PK')
from PK import location

#调用location.py文件的定位方法
we = location

dr = webdriver.Firefox()
dr.get("http://www.baidu.com")

time.sleep(3)

#调用findId()方法
we.findId(dr,"kw").send_keys('selenium')
time.sleep(1)
we.findId(dr,"su").click()
time.sleep(2)

dr.quit()