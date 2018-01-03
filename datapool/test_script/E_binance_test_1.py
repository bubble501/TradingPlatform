# -*- coding: utf-8 -*-
"""
Created on 2018/1/3 13:36 

@author: JERRY
"""

import websocket
import json
from threading import Thread


class eyeThread(Thread):

    def __init__(self, pair):
        Thread.__init__(self)
        self.pair0 = pair[0]
        self.pair1 = pair[1]
        self.pair = pair[0] + pair[1]
        print('[' + self.pair + ']: EYE started')

    def run(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp('wss://stream.binance.com:9443/ws/' + self.pair + '@kline_1m',
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever(sslopt={"cert_reqs": False})

    def on_message(self, ws, data):
        global pairs
        data = json.loads(data)
        pairs[data['s']] = {'open': data['k']['o'],
                            'close': data['k']['c'],
                            'high': data['k']['h'],
                            'low': data['k']['l']}
        print('[' + self.pair + ']: 1 ' + self.pair0 + ' = ' + str(pairs[data['s']]['close']) + ' ' + self.pair1)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print('Websocket OFF')

    def on_open(self, ws):
        print('Websocket ON')


# Live candle handling
global pairs
pairs = {}
thread = {}
pair = ['bnb', 'usdt']
pairName = pair[0] + pair[1]
thread[pairName] = eyeThread(pair)
thread[pairName].start()
thread[pairName].join()