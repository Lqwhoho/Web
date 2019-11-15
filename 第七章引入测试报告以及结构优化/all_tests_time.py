# coding=utf-8
import unittest
import HTMLTestRunner_cn
import time
import os

test_case_path = os.path.abspath('.\\test_case')  # 定义测试集所在文件夹
print(test_case_path)
# test_case_path = "E:\\Python脚本\\Web\\第七章引入测试报告以及结构优化\\test_case"    # 定义测试集所在文件夹
# pattern='start*.py' 规定测试集文件开头命名为start，也可以是pattern='start*.py'
# discover方法找到path 目录下所有文件到的测试用例组装到测试套件
# 因此可以直接通过run()方法执行discover
discover = unittest.defaultTestLoader.discover(test_case_path, pattern='start_*.py', top_level_dir=None)
runner = unittest.TextTestRunner

'''
def creatsuitel():
    testunit = unittest.TestSuite()
    # discover方法定义
    discover = unittest.defaultTestLoader.discover(test_case_path,
                                                   pattern='start_*.py',
                                                   top_level_dir=None
                                                   )
    # discover方法筛选出来的用例，循环添加到测试套件中
    print(discover)
    for test_suite in discover:
        print(test_suite)
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit
    
# 获取数组方法


alltestnames = creatsuitel()
'''


# 获取时间
now = time.strftime("\\%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))

# 定义报告存放路径，支持相对路径,把当前时间加到报告中
d = os.path.abspath('..\\Report')
print(d)
# report_path = "E:\\Python脚本\\Web\\Report\\"+now+'result.html'
report_path = d + now + 'result.html'
print(report_path)
fp = open(report_path, 'wb')

# 定义测试报告
runner = HTMLTestRunner_cn.HTMLTestRunner(
    stream=fp,
    title=u'主机屋登录+百度+有道翻译测试报告',
    description=u'用例执行情况:',
    verbosity=2,
    retry=1,    # 失败脚本重试次数
    save_last_try=True  # 如果save_last_try 为True ，一个用例仅显示最后一次测试的结果，如果save_last_try为False，则显示所有重试的结果
)
runner.run(discover)

'''
# 控制脚本执行时间
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


