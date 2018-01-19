# -*- coding: utf-8 -*-
"""
Created on 2018/1/9 20:34

@author: JERRY
"""

import threading

con = threading.Condition()
from time import sleep
status = 0
stop = True

def connect():
    global status,stop
    while True:
        con.acquire()
        if not status:
            print('正在连接...')
            sleep(5)
            status = 1
            stop = False
            print('连接已通知其他线程')
            con.notify_all()
        con.release()
        sleep(1)

def monitor():
    global status,stop
    while True:
        con.acquire()
        if stop is True:
            status = 0
            print('监控等待连接')
            con.wait()
            print('监控继续进行')
        else:
            status = 1
        con.release()
        sleep(1)

def saving():
    while True:
        con.acquire()
        if not status:
            print('保存等待连接')
            con.wait()
            print('开始保存')
        print('saving data')
        con.release()
        sleep(1)

def change():
    global stop
    stop = True

tklist = []

tklist.append(threading.Thread(target=connect))
tklist.append(threading.Thread(target=saving))
tklist.append(threading.Thread(target=monitor))


for i in tklist:
    i.start()
