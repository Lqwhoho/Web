#coding=utf-8
from selenium import webdriver
import time
import os

driver = webdriver.Firefox()

file_path = 'file:///' + os.path.abspath('frame.html')
driver.get(file_path)

driver.implicitly_wait(30)
#先找到ifromel(ID == f1)
driver.switch_to.frame("f1")
#再找到其下面的ifromel(id == f2)
driver.switch_to.frame("f2")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

time.sleep(5)
driver.quit()