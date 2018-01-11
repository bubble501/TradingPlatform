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
        self.ws = None
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

    def onError(self, ws, evt):
        """错误推送"""
        print('接口发生错误')
        print(evt)

    def saveData(self, conn, tableName):
        tmp_ = pd.DataFrame.from_dict(self.res)
        self.res = []
        tmp_.to_sql(tableName, conn, if_exists='append')
        print('当前时间为' + str(datetime.now()) + ',数据长度为' + str(len(tmp_)) + ',正在储存数据...')

    def onClose(self, ws):
        """接口断开"""
        print('接口未连接')

    def onOpen(self, ws):
        """接口打开"""
        print('接口已连接')

    def close(self):
        """关闭接口"""
        self.ws.close()
        print('接口已关闭')

    def getStatus(self):
        """返回状态"""
        return self.ws.sock.connected
