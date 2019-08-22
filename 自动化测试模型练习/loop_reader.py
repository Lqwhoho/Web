#coding = utf-8
import csv #导入CSV包

'''
#获取字典类型
info  = userinfo.dict()

#通过items()循环读取元组(键/值对)
for us,pw in info.items():
    print(us)
    print(pw)

'''

'''
#读取本地CSV文件
my_file = 'D:\\selenium练习数据\\userinfo.csv'
data = csv.reader(open(my_file,'rb'))

#循环输出每一行信息
for user in data:
    print(user[0])
    
    
'''



with open('D:\\selenium练习数据\\userinfo.csv','rb',newline='') as csvfile:
    read = csv.reader(csvfile)
    for i in read:
        print(i)