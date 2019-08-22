#coding=utf-8
from selenium import webdriver
import os               #os模块包含普通的操作系统功能，此处主要用于操作本地目录文件
import time

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('checkbox.html')       #path.abspath()方法用于获取当前路径下的文件
driver.get(file_path)

#选择页面上所有的tag name为input的元素
inputs = driver.find_elements_by_tag_name('input')
print(inputs)

#从中过滤出type为checkbox的元素，单击勾选
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()



# #选择所有的type为CheckBox的元素并单击勾选
# checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
# for checkbox in checkboxes:
#     checkbox.click()
#
# #打印当前页面上type为checkbox的个数
# print (len(driver.find_elements_by_css_selector('input[type=checkbox]')))     #返回一个对象的长度
#
# #把页面上最后1个checkbox的勾去掉
# driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()    #删除指定位置的元素，pop()为空默认选择最后一个


time.sleep(3)
driver.quit()