#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.action_chains import ActionChains
import time,unittest,re

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    #百度搜索用例
    def test_baidu_search(self):
        u"""百度搜索"""
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    #百度设置用例
    def test_baidu_set(self):
        u"""设置页面搜索结果为50条"""
        driver = self.driver

        #进入搜索设置页
        driver.get(self.base_url+"/")
        sup = driver.find_element_by_link_text("设置")
        ActionChains(driver).move_to_element(sup).perform()
        driver.find_element_by_class_name("setpref").click()

        #设置每页搜索结果为50条
        m = driver.find_element_by_id("nr")
        m.find_element_by_xpath("//option[@value='50']").click()
        time.sleep(2)

        #保存设置信息
        driver.find_element_by_class_name("prefpanelgo").click()
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)

    #搜索恢复默认设置
    def test_baidu_reset(self):
        u"""恢复默认设置"""
        driver = self.driver
        driver.get(self.base_url+"/")
        sup = driver.find_element_by_link_text("设置")
        ActionChains(driver).move_to_element(sup).perform()
        driver.find_element_by_class_name("setpref").click()
        driver.find_element_by_class_name("prefpanelrestore").click()
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
    unittest.main()