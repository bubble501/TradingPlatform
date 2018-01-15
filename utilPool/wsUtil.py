# -*- coding: utf-8 -*-
"""
Created on 2018/1/7

@author: JERRY
"""
from utilPool.dataUtil import dataUtilfunc


class wsUtilfunc(dataUtilfunc):
    def __init__(self):
        dataUtilfunc.__init__(self)

    def onError(self, ws, evt):
        """错误推送"""
        print(evt)

    def onClose(self, ws):
        """接口断开"""
        print('接口已关闭')

    def onOpen(self, ws):
        """接口打开"""
        print('接口已连接')

    def close(self):
        """关闭接口"""
        self.ws.close()
