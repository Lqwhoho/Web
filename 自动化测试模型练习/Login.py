#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
import  unittest,time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()    #打开浏览器
driver.maximize_window()        #最大化浏览器窗口
driver.implicitly_wait(8)       #设置隐式时间等待

driver.get("http://www.zhujiwu.com/login/")  #输入要访问的地址
time.sleep(15)
driver.find_element_by_id('userName').clear()                       #清空输入框的内容
driver.find_element_by_id('userName').send_keys('15918860373')      #输入账号
driver.find_element_by_id('passwordInput').clear()
driver.find_element_by_id('passwordInput').send_keys('www07142026') #输入密码
driver.find_element_by_id('loginSubmit').click()                    #点击登录

time.sleep(15)

# cn = driver.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small' and text()='关闭通知']")
# if not cn:
#     print('不存在弹窗')
# else:
#     driver.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small' and text()='关闭通知']").click()

# cn = driver.find_element_by_xpath("//button[@class='el-button el-button--primary el-button--small'").text()
# if (cn == u"立即充值"):
#     print ("测试成功，结果和预期结果匹配！")



#打印信息
#获取页面title，打印
title = driver.title
print(title)

#拿当前页面title与预期title作对比
if title == u"主机屋-控制台":
    print("登录成功!")
else:
    print("登录失败")

#获取当前页面URL
now_url = driver.current_url
print(now_url)

#拿当前URL与预期URL作对比
if now_url == "http://www.zhujiwu.com/control/#/user":
    print("跳转页面正确!")
else:
    print("跳转页面失败!")

#获取登录成功的用户
now_user = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[5]/span").text

#判断用户名是否为预期的结果，不是的话将抛出异常
if now_user=='您好，159****0373':
    print('登录成功')
else:
    raise NameError('user name error!')

out = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[5]/span")
ActionChains(driver).move_to_element(out).perform()
driver.find_element_by_partial_link_text("安全退出").click()
time.sleep(2)

driver.quit()                                                       #退出浏览器