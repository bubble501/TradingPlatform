# -*- coding: utf-8 -*-
"""
Created on 2018/1/12 11:47 

@author: JERRY
"""

import json
from time import sleep
from utilPool.generalUtil import myThread
import websocket
from datapool.general_config import hitbtc_ws
from utilPool.wsUtil import wsUtilfunc


class HitbtcApi(wsUtilfunc):
    """基于Websocket的API对象"""

    def __init__(self):
        """Constructor"""
        wsUtilfunc.__init__(self)
        self.apiKey = ''  # 用户名
        self.secretKey = ''  # 密码
        self.threadDict = {}
        self.host = hitbtc_ws  # 服务器地址

    def onMessage(self, ws, evt):
        """信息推送"""
        # data = self.readData(evt)
        # if json.loads(data).get('tick'):
        #     self.res.append(data)
        # print('onMessage中全局变量长度为'+str(len(self.res)))
        print(evt)

    def __connect(self, trace=False):
        """连接服务器"""
        websocket.enableTrace(trace)
        self.ws = websocket.WebSocketApp(url=self.host,
                                         on_message=self.onMessage,
                                         on_error=self.onError,
                                         on_close=self.onClose,
                                         on_open=self.onOpen)

    def keepconnect(self,*args, **kwargs):
        """保持连接器"""
        while True:
            if not self.status:
                self.__connect()
                print('正在连接...')
                self.threadDict['connect'] = myThread(target=self.ws.run_forever, args=args, kwargs=kwargs)
                self.threadDict['connect'].start()
                self.refreshSend = 1
                sleep(10)

    def sendMarketDataRequest(self, symbol):
        """发送行情请求"""
        for i in list(symbol):
            try:
                d = {'method': symbol[i]['method'], 'params': symbol[i]['params'], 'id': symbol[i]['id']}
            except IndexError:
                raise Exception('参数配置错误，请重新配置')

            msg = json.dumps(d)
            try:
                self.ws.send(msg)
            except websocket.WebSocketConnectionClosedException:
                pass


    def refreshCommand(self,symbol=None):
        while True:
            if self.refreshSend and self.status:
                self.sendMarketDataRequest(symbol)
                self.refreshSend = 0
                print('命令已发送')
            sleep(1)
