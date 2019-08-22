#coding = utf-8
import sys
sys.path.append("\test_case")
from test_case import *

#用例文件列表
def caselist():
    alltestname = [
        baidu.Baidu,
        youdao.Youdao,
        Login_Module.Logon,
    ]
    print("success read case list!!!")

    return alltestname