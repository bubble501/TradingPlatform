# -*- coding: utf-8 -*-
"""
Created on 2018/1/3 19:57 

@author: JERRY
"""

import hashlib
import zlib
import json
from time import sleep
from threading import Thread
import ssl
import websocket
from datapool.general_config import bitmex_ws

basehost = bitmex_ws

########################################################################
class BitmexApi(object):
    """基于Websocket的API对象"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.apiKey = ''  # 用户名
        self.secretKey = ''  # 密码
        self.host = ''  # 服务器地址
        self.currency = ''  # 货币类型（usd或者cny）
        self.ws = None  # websocket应用对象
        self.thread = None  # 工作线程
        global x

    #######################
    ## 通用函数
    #######################

    # ----------------------------------------------------------------------
    def readData(self, evt):
        """解压缩推送收到的数据"""
        # 创建解压器
        decompress = zlib.decompressobj(-zlib.MAX_WBITS)

        # 将原始数据解压成字符串
        inflated = decompress.decompress(evt) + decompress.flush()

        # 通过json解析字符串
        data = json.loads(inflated)

        return data

    # ----------------------------------------------------------------------
    def generateSign(self, params):
        """生成签名"""
        l = []
        for key in sorted(params.keys()):
            l.append('%s=%s' % (key, params[key]))
        l.append('secret_key=%s' % self.secretKey)
        sign = '&'.join(l)
        return hashlib.md5(sign.encode('utf-8')).hexdigest().upper()

    # ----------------------------------------------------------------------
    def onMessage(self, ws, evt):
        """信息推送"""
        print('onMessage')
        data = json.loads(evt)

        print(data)

    # ----------------------------------------------------------------------
    def onError(self, ws, evt):
        """错误推送"""
        print('onError')
        print(evt)

    # ----------------------------------------------------------------------
    def onClose(self, ws):
        """接口断开"""
        print('onClose')

    # ----------------------------------------------------------------------
    def onOpen(self, ws):
        """接口打开"""
        print('onOpen')

    # ----------------------------------------------------------------------
    def connect(self, trace=False):
        """连接服务器"""
        self.host = 'wss://www.bitmex.com/realtime'
        websocket.enableTrace(trace)
        self.ws = websocket.WebSocketApp(url = self.host,
                                         on_message=self.onMessage,
                                         on_error=self.onError,
                                         on_close=self.onClose,
                                         on_open=self.onOpen)

        self.thread = Thread(target=self.ws.run_forever)
        self.thread.start()

    # ----------------------------------------------------------------------
    def reconnect(self):
        """重新连接"""
        # 首先关闭之前的连接
        self.close()

        # 再执行重连任务
        self.ws = websocket.WebSocketApp(self.host,
                                         on_message=self.onMessage,
                                         on_error=self.onError,
                                         on_close=self.onClose,
                                         on_open=self.onOpen)

        self.thread = Thread(target=self.ws.run_forever(sslopt={"cert_reqs": False}))
        self.thread.start()

    # ----------------------------------------------------------------------
    def close(self):
        """关闭接口"""
        if self.thread and self.thread.isAlive:
            self.ws.close()
            self.thread.join()

    # ----------------------------------------------------------------------
    def sendMarketDataRequest(self, arglist):
        """发送行情请求"""
        # 生成请求
        d = {}
        d['op'] = 'subscribe'
        d['args'] = arglist

        # 使用json打包并发送
        j = json.dumps(d)

        # 若触发异常则重连
        try:
            self.ws.send(j)
        except websocket.WebSocketConnectionClosedException:
            pass
