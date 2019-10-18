from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
# 开启静默模式
browser = webdriver.Firefox(options=options)
url = 'https://www.csdn.net/'
browser.get(url)
print(browser.title)

browser.close()
