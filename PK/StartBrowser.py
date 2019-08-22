#coding=utf-8
from selenium import webdriver

def StartBrowser(name):
    '''
    打开浏览器函数,‘Firefox’，‘Chrome’，‘IE’
    '''
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
