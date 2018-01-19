# -*- coding: utf-8 -*-
"""
Created on 2018/1/8 16:52

@author: JERRY
"""

import threading
from time import sleep
import queue

con = threading.Condition()
status = 0  # 0 表示未连接，1 表示已连接， 2 表示重连接


class test:
    def __init__(self, status):
        self.status = status
        self.stop = True

    def connect(self):
        while True:
            con.acquire()
            if self.status == 0:
                print('start connecting')
                sleep(5)
                print('on connection...')
                self.status = 2

    def monitor(self):
        sleep(1)
        while True:
            if self.stop:
                con.acquire()
                self.status = 0
                con.wait()
                con.release()
            else:
                self.status = 1


    def sendMsg(self):
        sleep(1)
        print('开始发送信息')
        while True:
            if self.status == 2:
                print('is sending msg...')
                self.status = 1
            sleep(1)

    def saveData(self):
        sleep(1)
        print('开始储存数据')
        while True:
            if self.status == 1:
                print('saving data...')
                sleep(10)

    def earning(self):
        sleep(1)
        print('开始赚钱')
        while True:
            if self.status == 1:
                print('earning monney...')
                sleep(5)

    def changeStatus(self):
        self.status = 0


t1 = test(0)

funclist = [t1.connect, t1.sendMsg, t1.saveData, t1.earning]
namelist = ['connect', 'sendMsg', 'tsaveData', 'earning']
task = []
for i in range(4):
    task.append(threading.Thread(target=funclist[i],name=namelist[i]))

for i in task:
    i.start()

# while not q.empty():
#     task = q.get()
#     task.start()
