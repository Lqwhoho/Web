#coding = utf-8
import unittest,time,os,datetime
import sys
# import allcase_list #调用数组文件
import HTMLTestRunner
import smtplib
from email.mime.text import  MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#定义发送邮件
def sentmail(file_new):
    #发送邮箱
    mail_from = 'dansuper@126.com'
    #收信邮件
    mail_to = '45266347@qq.com'
    #定义正文
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['From'] = 'dansuper@163.com'
    msg['Subject'] = Header('私有云测试报告','utf-8')
    msg['To'] = "45266347@qq.com"
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg ['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    #连接SMTP服务器，此处用的是126的SMTP服务器
    smtp.connect('smtp.126.com')
    #用户名密码
    smtp.login('dansuper@126.com','qq07142026')   #此密码是客户端授权登录密码
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print('email has send out!')

#查找测试报告，调用发邮件功能
def sendreport():
    result_dir = 'E:\\Python脚本\\Web\\Report'

    lists = os.listdir(result_dir)  # os.listdir用于获取目录下的所有文件列表
    lists.sort(key=lambda fn:
    os.path.getmtime(result_dir + "\\" + fn)  # 返回文件列表中最新文件的时间
    if not os.path.isdir(result_dir + "\\" + fn)  # 判断某一路径是否为目录
    else 0)
    print('最新测试生成的报告:' + lists[-2])  # lists[-1] -1表示取文件列表中的最大值
    file_new = os.path.join(result_dir, lists[-2])  #
    print(file_new)
    #调用发邮件模块
    sentmail(file_new)

listaa = ("E:\\Python脚本\\Web\\第七章引入测试报告以及结构优化\\test_case")
def creatsuitel():
    testunit = unittest.TestSuite()
    #discover方法定义
    discover = unittest.defaultTestLoader.discover(listaa,
                       pattern = 'start_*.py',
                       top_level_dir=None
                                                   )
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit
from test_case import *


testunit = unittest.TestSuite()

#获取时间
now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))


# #将测试用例加入到测试容器(套件)中
# testunit.addTest(unittest.makeSuite(baidu.Baidu))
# testunit.addTest(unittest.makeSuite(youdao.Youdao))

# #执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)

#获取数组方法
alltestnames = creatsuitel()

# #循环读取数组中的用例
# for test in alltestnames:
#     testunit.addTest(unittest.makeSuite(test))

#定义报告存放路径，支持相对路径,把当前时间加到报告中
report_path = "E:\\Python脚本\\Web\\Report\\"+now+'result.html'
fp = open(report_path,'wb')

#定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title = u'测试报告',
    description = u'用例执行情况:')

#执行测试用例
runner.run(alltestnames)
#执行发邮件
sendreport()
