# -*- coding: utf-8 -*-
"""
Created on 2018/1/17 17:03 

@author: Ji
"""

from datapool.general_config import bitfinex_rest
from utilPool.restUtil import rsUtilfunc
import json


class BitfinexRest(rsUtilfunc):
    def __init__(self, proxy={}):
        rsUtilfunc.__init__(self)
        self.__url = bitfinex_rest
        self.proxy = proxy
        self.status = True

    # 罗列所有可能的币种
    def findAllSymbol(self, param):
        URL = "/v1/symbols"
        msg = rsUtilfunc.httpGet(self.__url, URL, '', self.proxy)
        return msg

    # ticker
    def getTicker(self, param):
        URL = "/v1/pubticker/"
        msg = rsUtilfunc.httpGet(self.__url, URL, param, self.proxy)
        self.res.append(json.dumps(msg))
        return msg

    # orderbook
    def getOrderBook(self, param):
        URL = "/v1/book/"
        msg = rsUtilfunc.httpGet(self.__url, URL, param, self.proxy)
        self.res.append(json.dumps(msg))
        return msg