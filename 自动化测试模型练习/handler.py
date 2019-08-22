#coding=utf-8
import time
'''
try:
    open('abc.txt', 'r')
except IOError:
    pass
'''

'''
try:
    print(aa)
except NameError as msg:
    print(msg)
'''

try:
    f = open('D:\selenium练习数据\poem.txt')
    while True:                                         # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print(line)

finally:
    f.close()
    print('Cleaning up...closed the file')

