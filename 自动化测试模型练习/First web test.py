#coding=utf-8
from selenium import webdriver
import webbrowser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains    #引入ActionChains类
import  time

driver = webdriver.Firefox()    #打开浏览器
# webbrowser = webdriver.Firefox()
driver.maximize_window()        #最大化浏览器窗口
# driver.set_window_size(480,800)  #设置浏览器宽480，高800显示
# driver.implicitly_wait(8)       #设置隐式时间等待

driver.get("https://www.baidu.com/")                                    #地址栏输入百度地址
# time.sleep(5)



'''
#遍历‘百度一下’首页功能
driver.find_element_by_link_text("新闻").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.find_element_by_link_text("hao123").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.find_element_by_link_text("地图").click()
time.sleep(5)
driver.back()
time.sleep(3)
driver.find_element_by_link_text("贴吧").click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.find_element_by_link_text("学术").click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.find_element_by_link_text("设置").click()
time.sleep(5)
driver.back()
time.sleep(5)
size = driver.find_element_by_id("kw").size
print(size)
# text = driver.find_element_by_id("cp").text
# print(text)
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)
'''


'''
#百度一下搜索"selenium"
driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")     #搜索输入框输入Selenium
driver.find_element_by_xpath("//*[@id='su']").click()                   #点击百度一下按钮
right = driver.find_element_by_xpath("//*[@id='su']")
ActionChains(driver).context_click(right).perform()
time.sleep(5)
'''


'''
#键盘事件
driver.find_element_by_xpath("//*[@id='kw']").send_keys("seleniumm")     #搜索输入框输入Selenium
#删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(3)

#输入空格键+‘教程’
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
time.sleep(3)

#crtl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)

#ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)

#输入框重新输入内容，搜索
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
time.sleep(2)

#通过回车键盘来代替点击操作
driver.find_element_by_id("su").send_keys((Keys.ENTER))
time.sleep(5)
'''



'''
#设置隐性等待事件
#webdriverwait()使用方法
element = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id("kw"))
element.send_keys("selenium")

#添加智能等待
driver.implcitly_wait(30)
driver.find_element_by_id("su").click()

#添加固定休眠时间
time.sleep(5)
'''

driver.quit()                                                           #退出浏览器
