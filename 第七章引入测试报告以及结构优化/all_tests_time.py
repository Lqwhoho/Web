#coding=utf-8
import unittest
import HTMLTestRunner_cn
import time

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

#获取数组方法
alltestnames = creatsuitel()

#获取时间
now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))

#定义报告存放路径，支持相对路径,把当前时间加到报告中
report_path = "E:\\Python脚本\\Web\\Report\\"+now+'result.html'
fp = open(report_path,'wb')

#定义测试报告
runner = HTMLTestRunner_cn.HTMLTestRunner(
    stream = fp,
    title = u'主机屋登录+百度+有道翻译测试报告',
    description = u'用例执行情况:',
    verbosity = 2,
    retry=1, #失败脚本重试次数
    save_last_try=True #如果save_last_try 为True ，一个用例仅显示最后一次测试的结果，如果save_last_try为False，则显示所有重试的结果
)
runner.run(alltestnames)

'''
#控制脚本执行时间
k = 1
while k<2:
    timing = time.strftime("%H_%M",time.localtime(time.time()))
    if timing == '16_42':
        print(u"开始运行脚本：")
        runner.run(alltestnames)
        print(u"运行完成退出")
        break
    else:
        time.sleep(10)
        print(timing)
'''


