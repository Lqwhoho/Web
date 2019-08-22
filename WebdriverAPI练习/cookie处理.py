#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()    #打开浏览器
driver.maximize_window()        #最大化浏览器窗口
driver.implicitly_wait(8)       #设置隐式时间等待

driver.get("http://www.youdao.com/")  #输入要访问的地址
time.sleep(5)

#向cookies的name和value添加会话信息
driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbb'})

#向cookies中的name和value信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s"%(cookie['name'],cookie['value']))

#删除所有的cookie
driver.delete_all_cookies()

time.sleep(2)
driver.quit()