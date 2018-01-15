# -*- coding: utf-8 -*-
"""
Created on 2018/1/15 10:51 

@author: JERRY
"""

import gzip
from datetime import datetime
import pandas as pd
from time import sleep


class dataUtilfunc:

    def __init__(self):
        self.status = 0
        self.refreshSend = 0
        self.ws = None  # websocket应用对象
        self.res = []

    def readData(self, evt):
        """解压缩推送收到的数据"""
        data = gzip.decompress(evt).decode('utf-8')
        return data

    def saveData(self, conn, tableName):
        """保存数据"""
        while True:
            if self.status:
                sleep(10)
                tmp_ = pd.DataFrame(self.res,columns=['data'])
                self.res = []
                tmp_.to_sql(tableName, conn, if_exists='append')
                print('当前时间为' + str(datetime.now()) + ',数据长度为' + str(len(tmp_)) + ',正在储存数据...')

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