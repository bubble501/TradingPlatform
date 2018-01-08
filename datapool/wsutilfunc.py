# -*- coding: utf-8 -*-
"""
Created on 2018/1/7

@author: JERRY
"""
import zlib
import pandas as pd
import json
from time import sleep
from threading import Thread
import pymysql as ps
ps.install_as_MySQLdb()
import MySQLdb
from sqlalchemy import create_engine
conn = create_engine( 'mysql+mysqldb://Jerry:Eli19890908@localhost/datapool?charset=utf8',echo = False)

global res
res = []

class wsUtil(object):
    def __init__(self):
        pass

    def readData(self, evt):
        """解压缩推送收到的数据"""
        # 创建解压器
        decompress = zlib.decompressobj(-zlib.MAX_WBITS)

        # 将原始数据解压成字符串
        inflated = decompress.decompress(evt) + decompress.flush()

        # 通过json解析字符串
        data = json.loads(inflated)

        return data

    def onError(self, ws, evt):
        """错误推送"""
        print('接口发生错误')
        print(evt)

    def data2sql(self,conn,tableName):
        while True:
            sleep(10)
            print('正在储存数据...')
            global res
            tmp_ = pd.DataFrame.from_dict(res)
            tmp_.to_sql(tableName,conn,if_exists='append')
            res = []

    def saveData(self,tableName):
        t1 = Thread(target=self.data2sql(conn,tableName))
        t1.start()

    def onClose(self, ws):
        """接口断开"""
        print('接口未连接')

    def onOpen(self, ws):
        """接口打开"""
        print('接口已连接')

    def close(self):
        """关闭接口"""
        if self.thread and self.thread.isAlive:
            self.ws.close()
            self.thread.join()
            print('接口已关闭')