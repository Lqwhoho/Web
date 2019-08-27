# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
import time
import sys
sys.path.append("\Public")
from Public import logon, logout


class Logon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Firefox()  # 不开启静默模式
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        cls.driver = webdriver.Firefox(options=options)    # 开启静默模式
        cls.driver.implicitly_wait(30)
        cls.base_url = "http://www.zhujiwu.com"
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

    # 主机屋登录用例
    def test_logon(self):
        """主机屋网站登录-点击立即充值-退出登录"""
        driver = self.driver
        driver.get(self.base_url+"/login/")

        # 调用登录模块
        logon.logon(self)

        # 点击立即充值
        driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/button[1]").click()
        time.sleep(3)

        # 调用退出模块
        logout.logout(self)


if __name__ == '__main__':
    # 定义一个单元测试容器
    # testunit = unittest.TestSuite()
    #
    # 讲测试用例加入到测试容器中
    # testunit.addTest(Logon("test_logon"))

    # 定义报告存放路径，支持相对路径
    # report_path = "E:\\Python脚本\\Web\\Report\\result.html"
    # fp = open(report_path,"wb")
    #
    # 定义测试报告
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream = fp,
    #     title = u'主机屋网站登录测试报告',
    #     description=u'用例执行情况:'
    # )

    # 运行测试用例
    # runner.run(testunit)
    unittest.main()
