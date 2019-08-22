#coding=utf-8
from selenium import webdriver
import time
import threading
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

lists = ['Chrome','Firefox']

for broswer in lists:
    print(broswer)
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={
            'platform':broswer,
            'version':'',
            # 'javascriptEnabled':True
        }
    )

    driver.get("http://www.baidu.com")
    time.sleep(3)

    driver.quit()

'''
def StartBrowser(name):
    # 打开浏览器函数,‘Firefox’，‘Chrome’，‘IE’
    try:
        if name == "Firefox" or name == "firefox" or name == "ff":
            print("Start Browser Name:Firefox")
            driver = webdriver.Firfox()
            return driver
        elif name == "Chrome" or name == "chrome":
            print("Start Browser Name:Chrome")
            driver = webdriver.Chrome()
            return driver
        elif name == "ie" or name == "IE":
            print("Start Browser Name:IE")
            driver = webdriver.Ie()
            return driver
        else:
            print("Not found this browser,You can use 'Firefox','Chrome'or 'IE'")
    except Exception as msg:
        print("启动浏览器出现异常：%s"%str(msg))

@threading(5)
def run_case(name):
    driver = StartBrowser(name)
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    time.sleep(3)
    print(driver.title)
    driver.quit()

if __name__=="__main__":
    names = ["Chrome","Firefox"]
    for i in names:
        run_case(i).
'''