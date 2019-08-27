# coding=utf-8
from selenium import webdriver
import unittest
import time


class Youdao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Firefox()  # 不开启静默模式
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        cls.driver = webdriver.Firefox(options=options)  # 开启静默模式
        cls.driver.implicitly_wait(30)
        cls.base_url = "http://www.youdao.com"
        cls.verificationErrors = []
        cls.accept_next_alter = True
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass

    # 有道搜索用例
    def test_youdao_search(self):
        u"""中译英：成功"""
        driver = self.driver
        driver.get(self.base_url + "/")

        driver.find_element_by_id("translateContent").send_keys(u"成功")
        self.add_img()
        driver.find_element_by_xpath("/html/body/div[5]/div/form/button").click()
        time.sleep(2)
        self.add_img()
        driver.find_element_by_xpath("/html/body/div[7]/i/a[1]").click()
        self.add_img()


if __name__ == "__main__":
    unittest.main()

