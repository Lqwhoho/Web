#!C:\Users\liuquanwei\AppData\Local\Programs\Python\Python37
# -*- coding:utf-8 -*-
# @Author：liuquanwei
# @Time：2019/10/18 08:55
# @Filename：Reissue_application.py
# @Desc：====================================================
"""
OA办公平台补签申请自动化脚本
公司局域网环境
需要填写的信息：登录账号、密码，证明人，补签时间，审批意见
"""
# @Software：PyCharm
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 开启会话，启动浏览器
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# 全屏展示
driver.maximize_window()

# 打开测试网站
URL = 'http://10.1.125.188:8080/jsaas/login.jsp'
driver.get(URL)

"""登录OA系统"""
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('liuquanwei@zsgr.cn')
driver.find_element_by_id('password').send_keys('1')
time.sleep(2)
driver.find_element_by_class_name('btn').click()
time.sleep(5)

# 点击【个人办公】
driver.find_element_by_name('个人办公').click()
time.sleep(1)

# 点击【流程事项申请】
driver.find_element_by_name('流程事项申请').click()
time.sleep(3)

# 等待iframe出现并切换到iframe所在的HTML页面
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it('mini-iframe-9'))
# driver.switch_to.frame("mini-iframe-9")
# time.sleep(1)

# 点击【补签申请】
# driver.find_element_by_xpath("//a[text()='补签申请']").click()
driver.find_element_by_partial_link_text(u'补签申请').click()
time.sleep(3)

# 返回最外层frame
driver.switch_to.default_content()

# 点击【选择证明人-人像按钮】
driver.switch_to.frame("mini-iframe-11")
# driver.find_element_by_css_selector("[class='mini-buttonedit-button mini-buttonedit-trigger']").click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="form-panel"]/table/tbody/tr[3]/td[2]/span/span/span/span[2]/span').click()
time.sleep(2)

# 返回最外层frame
driver.switch_to.default_content()

# 输入姓名
driver.switch_to.frame("mini-iframe-13")
driver.find_element_by_xpath("//*[@id='fullname$text']").send_keys("刘权威")
time.sleep(1)

# 点击【查询】
driver.find_element_by_xpath("//*[@id='toolbarBody']/a[1]/span").click()
time.sleep(3)

# 选择用户
driver.find_element_by_xpath("//div[text()='刘权威']").click()

# 点击【确定】
driver.find_element_by_xpath("//*[@id='south']/div[2]/div/a[1]/span/span").click()
time.sleep(2)

# 返回最外层frame，如果查找的元素不在当前iframe，脚本运行会报错“TypeError: can't access dead object”
driver.switch_to.default_content()
driver.switch_to.frame("mini-iframe-11")

# 输入日期
driver.find_element_by_xpath("//*[@id='supplementTime$text']").send_keys("2019-10-17 17:12:55")
time.sleep(1)

# 输入补签事由
driver.find_element_by_xpath("//*[@id='form-panel']/table/tbody/tr[4]/td[2]/span/span[1]/textarea").\
    send_keys("指纹打卡失败，申请补签")

# 退出浏览器
driver.quit()
