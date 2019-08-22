#coding=utf-8
import os,datetime,time

result_dir = 'E:\\Python脚本\\Web\\Report'

lists = os.listdir(result_dir)  #os.listdir用于获取目录下的所有文件列表
lists.sort(key = lambda  fn:
    os.path.getmtime(result_dir+"\\"+fn) #返回文件列表中最新文件的时间
    if not os.path.isdir(result_dir+"\\"+ fn)   #判断某一路径是否为目录
    else 0)
print('最新的文件为:'+lists[-1])  #lists[-1] -1表示取文件列表中的最大值
file = os.path.join(result_dir,lists[-1]) #
print(file)