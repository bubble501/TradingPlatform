# -*- coding: utf-8 -*-
"""
Created on 2018/1/10 14:14 

@author: JERRY
"""
#coding=utf-8
__author__ = 'Bruce_Zhou'
import threading
import time
import datetime
num = 0
con = threading.Condition()

class Gov(threading.Thread):
    def __init__(self):
        super(Gov, self).__init__()

    def run(self):
        global num
        print('庄家获取锁')
        con.acquire()

        while True:
            print ("开始拉升股市")
            num += 1
            print ("拉升了" + str(num) + "个点")
            time.sleep(2)
            if num == 5:
                print ("暂时安全！")
                con.notify()
                con.wait()

        print('庄家释放锁')
        con.release()


class Consumers(threading.Thread):
    def __init__(self):
        super(Consumers, self).__init__()

    def run(self):
        global num
        print('散户获取锁')
        con.acquire()
        while True:
            if num > 0:
                print("开始打压股市")
                num -= 1
                print("打压了" + str(num) + "个点")
                time.sleep(2)
                if num == 0:
                    print("你妹的！天台在哪里！")
                    con.notify()
                    con.wait()
        print('散户获取锁')
        con.release()

if __name__ == '__main__':
    p = Gov()
    c = Consumers()
    p.start()
    c.start()






