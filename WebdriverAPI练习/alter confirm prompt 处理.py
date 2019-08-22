#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#ActionChains用于生成用户的行为，所有的行为都存储在Actionchains对象。通过perform()执行存储的行为
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://www.baidu.com")
time.sleep(3)

#点击打开搜索设置(鼠标移动到设置按钮)
attrible = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(attrible).perform()

#点击搜索设置
driver.find_element_by_class_name("setpref").click()

#点击保存设置
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(5)

if EC.alert_is_present:
    print("Alert exists")
    alert = driver.switch_to_alert()
    print(alert.text)
    alert.accept()
    print("Alert accepted")
else:
    print("No alert exists")

# al = driver.switch_to_alert()
# print(al.text)
# al.accept()
time.sleep(2)
driver.quit()