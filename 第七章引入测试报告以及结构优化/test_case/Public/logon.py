#-*- coding:utf-8 -*-
import time
from data import userinfo

'''
source = open("D:\\username.txt",'r')  #用户名文件
us = source.read()
source.close()

source1 = open("D:\\password.txt",'r')  #登录密码文件
pw = source1.read()
source1.close()
'''

#通过两个变量，来接收调用函数获得用户名&密码
us,pw = userinfo.fun()
#打印两个变量
print(us,pw)



#登录模块(函数)
def logon(self):
    driver = self.driver
    driver.maximize_window()
    driver.find_element_by_id('userName').clear()  # 清空输入框的内容
    self.add_img()
    driver.find_element_by_id('userName').send_keys(us)  # 输入账号
    self.add_img()
    driver.find_element_by_id('passwordInput').clear()
    self.add_img()
    driver.find_element_by_id('passwordInput').send_keys(pw)  # 输入密码
    self.add_img()
    driver.find_element_by_id('loginSubmit').click()  # 点击登录
    time.sleep(5)
    self.add_img()