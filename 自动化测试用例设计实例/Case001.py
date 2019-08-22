#coding=utf-8
#百度网盘登录-判断用户名是否正确-退出登录流程
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Firefox()
browser.get("https://pan.baidu.com/")
browser.maximize_window()
time.sleep(8)

browser.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn").click()
browser.find_element_by_name("userName").clear()
browser.find_element_by_name("userName").send_keys("15918860373")
browser.find_element_by_name("password").clear()
browser.find_element_by_name("password").send_keys("LQW45266347")
browser.find_element_by_name("memberPass").click()
browser.find_element_by_id("TANGRAM__PSP_4__submit").click()
time.sleep(7)
browser.find_element_by_class_name("know-button").click()
time.sleep(2)

#获取用户名
username = browser.find_element_by_class_name("user-name").text

#判断用户名是否正确
if username == 'lqw15918860373':
    print('登录成功')
else:
    raise NameError('user name error')

#退出登录
logout = browser.find_element_by_class_name("user-name")
ActionChains(browser).move_to_element(logout).perform()
browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/dl/dd[2]/span/dl/dd/ul/li[4]/a").click()
time.sleep(2)
browser.find_element_by_id("_disk_id_4").click()
time.sleep(2)

#判断是否成功退出登录，返回至登录界面
reg = browser.find_element_by_link_text("立即注册").text
if reg == u'立即注册':
    print('成功退出登录')
else:
    raise NameError('退出登录失败')
time.sleep(2)
browser.quit()


