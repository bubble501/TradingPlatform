# -*- coding: utf-8 -*-
"""
Created on 2018/1/8 16:52

@author: JERRY
"""

import threading
from time import sleep
import queue


con = threading.Condition
status = 0 #0 表示未连接，1 表示已连接， 2 表示重连接

class test:
    def __init__(self, status):
        self.status = status

    def connect(self):
        con.acquire()
        print('start connecting')
        sleep(5)
        self.status = 2
        print('on connection...')
        con.release()

    def reconnect(self):
        while True:
            if status == 0:
                print('reconnecting...')
                self.connect()
            sleep(1)

    def sendMsg(self):
        print('开始发送信息')
        while True:
            if self.status == 2:
                print('is sending msg...')
                self.status = 1
            sleep(1)

    def saveData(self):
        print('开始储存数据')
        while self.status > 0:
            print('saving data...')
            sleep(15)

    def earning(self):
        print('开始赚钱')
        while self.status > 0:
            print('earning monney...')
            sleep(5)


t1 = test(0)

namelist = [t1.connect, t1.reconnect, t1.sendMsg, t1.saveData, t1.earning]
task = []
for i in range(5):
    task.append(threading.Thread(target = namelist[i]))

for i in task:
    i.start()

# while not q.empty():
#     task = q.get()
#     task.start()
