#coding=utf-8
from selenium import webdriver
import os

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("brower.helperApps.neverAsk.saveToDisk", "application/octet-stream")

browser = webdriver.Firefox(firefox_profile = fp)

browser.get("http://pypi.python.org/pypi/selenium")
browser.find_element_by_partial_link_text("selenium-2").click()