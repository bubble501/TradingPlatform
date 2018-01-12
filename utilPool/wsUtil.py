# -*- coding: utf-8 -*-
"""
Created on 2018/1/7

@author: JERRY
"""
import gzip
from datetime import datetime
import pandas as pd
from time import sleep


class wsUtilfunc(object):
    def __init__(self):
        self.status = 0
        self.refreshSend = 0
        self.ws = None  # websocket应用对象
        self.res = []

    def readData(self, evt):
        """解压缩推送收到的数据"""
        data = gzip.decompress(evt).decode('utf-8')
        return data

    def onError(self, ws, evt):
        """错误推送"""
        print(evt)

    def getData(self):
        pass

    def saveData(self, conn, tableName):
        """保存数据"""
        while True:
            if self.status:
                sleep(10)
                tmp_ = pd.DataFrame(self.res,columns=['data'])
                self.res = []
                tmp_.to_sql(tableName, conn, if_exists='append')
                print('当前时间为' + str(datetime.now()) + ',数据长度为' + str(len(tmp_)) + ',正在储存数据...')


    def onClose(self, ws):
        """接口断开"""
        print('接口已关闭')

    def onOpen(self, ws):
        """接口打开"""
        print('接口已连接')

    def close(self):
        """关闭接口"""
        self.ws.close()

    def isDisconn(self):
        """返回状态"""
        while True:
            if self.ws:
                try:
                    if self.ws.sock.connected:
                        self.status = 1
                except Exception as e:
                    self.status = 0
                    self.refreshSend = 0
                finally:
                    pass
            sleep(1)
