#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchAttributeException
import unittest,time,re

class Youdao(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://www.youdao.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    #有道搜索用例
    def test_youdao_search(self):
        u"""中译英：成功"""
        driver = self.driver
        driver.get(self.base_url + "/")

        driver.find_element_by_id("translateContent").send_keys(u"成功")
        driver.find_element_by_xpath("/html/body/div[5]/div/form/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[7]/i/a[1]").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

