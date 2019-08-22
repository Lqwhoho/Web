#conding=utf=8
from time import sleep,ctime

def loop0():
    print('start loop 0 at:',ctime())
    sleep(3)
    print('loop 0 done at:',ctime())

def loop1():
    print('start loop 1 at:',ctime())
    sleep(2)
    print('loop 1 done at:',ctime())

def main():
    print('start:',ctime())
    loop0()
    loop1()
    print('all end:',ctime())

if __name__ == '__main__':
    main()