#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
import time

#退出登录
def logout(self):
    driver = self.driver
    driver.maximize_window()
    time.sleep(2)
    out = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[5]/span")
    ActionChains(driver).move_to_element(out).perform()
    self.add_img()
    driver.find_element_by_partial_link_text("安全退出").click()
    time.sleep(2)
    self.add_img()
