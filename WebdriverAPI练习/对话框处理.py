#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.baidu.com/")
time.sleep(3)

#点击登录按钮
driver.find_element_by_link_text("登录").click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()

#通过二次定位找到用户名输入框和密码框
driver.find_element_by_name("userName").send_keys("15918860373")
driver.find_element_by_name("password").send_keys("LQW45266347")

#点击登录
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()

time.sleep(5)

driver.quit()