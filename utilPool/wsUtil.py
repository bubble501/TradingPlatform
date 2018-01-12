# -*- coding: utf-8 -*-
"""
Created on 2018/1/7

@author: JERRY
"""
import zlib
from datetime import datetime
import pandas as pd
import json
from time import sleep


class wsUtilfunc(object):
    def __init__(self):
        self.status = 0
        self.refreshSend = 0
        self.ws = None  # websocket应用对象
        self.res = []

    def readData(self, evt):
        """解压缩推送收到的数据"""
        # 创建解压器
        decompress = zlib.decompressobj(-zlib.MAX_WBITS)
        # 将原始数据解压成字符串
        inflated = decompress.decompress(evt) + decompress.flush()
        # 通过json解析字符串
        data = json.loads(inflated)
        return data

    def onMessage(self, ws, evt):
        """信息推送"""
        if json.loads(evt)[0]['data'].get('asks'):
            self.res.append(json.dumps(json.loads(evt)[0]['data']))
        print('onMessage中全局变量长度为'+str(len(self.res)))
        # print(evt)

    def onError(self, ws, evt):
        """错误推送"""
        print(evt)

    def getData(self):
        pass

    def saveData(self, conn, tableName):
        """保存数据"""
        while True:
            if self.status:
                tmp_ = pd.DataFrame([],columns=['data'])
                sleep(10)
                tmp_.append(pd.DataFrame.from_dict(self.res))
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
                if not self.ws.sock:
                    self.status = 0
                    self.refreshSend = 0
                else:
                    self.status = 1
            sleep(1)
