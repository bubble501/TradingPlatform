# -*- coding: utf-8 -*-
"""
Created on 2018/1/8 0:13

@author: JERRY
"""
import json
from time import sleep
from threading import Thread
import websocket
from datapool.api_config import okex_ws
from utilPool.wsUtil import wsUtilfunc
from utilPool.generalUtil import myThread

########################################################################
class OkexApi(wsUtilfunc):
    """基于Websocket的API对象"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wsUtilfunc.__init__(self)
        self.apiKey = ''  # 用户名
        self.secretKey = ''  # 密码
        self.host = okex_ws  # 服务器地址
        self.thread = None
        self.ws = None  # websocket应用对象

    # ----------------------------------------------------------------------
    def onMessage(self, ws, evt):
        """信息推送"""
        if json.loads(evt)[0]['data'].get('asks'):
            self.res.append(json.dumps(json.loads(evt)[0]['data']))
        print('onMessage中全局变量长度为'+str(len(self.res)))

    # ----------------------------------------------------------------------
    def connect(self, trace=False):
        """连接服务器"""

        websocket.enableTrace(trace)
        self.ws = websocket.WebSocketApp(url=self.host,
                                         on_message=self.onMessage,
                                         on_error=self.onError,
                                         on_close=self.onClose,
                                         on_open=self.onOpen)

        self.thread = myThread('connect',self.ws.run_forever)
        self.thread.go()

        # while not self.ws.sock.connected:
        #     print('正在连接...')
        #     sleep(1)

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

        self.thread = myThread('reconnect', self.ws.run_forever)
        self.thread.go()

        while not self.ws.sock.connected:
            print('正在连接...')
            sleep(1)

    # ----------------------------------------------------------------------
    def sendMarketDataRequest(self, symbol=None):
        """发送行情请求"""
        # 生成请求
        for i in list(symbol):
            try:
                d = {}
                d['event'] = symbol[i]['event']
                d['channel'] = symbol[i]['channel']
            except IndexError:
                raise Exception('参数配置错误，请重新配置')

            msg = json.dumps(d)
            try:
                self.ws.send(msg)
            except websocket.WebSocketConnectionClosedException:
                pass
