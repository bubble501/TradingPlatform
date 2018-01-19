# -*- coding: utf-8 -*-
"""
Created on 2018/1/14 17:48

@author: JERRY
"""

from datapool.general_config import bit_z_rest
from utilPool.restUtil import rsUtilfunc

class BitZ(rsUtilfunc):

    def __init__(self,proxy = {}):
        rsUtilfunc.__init__(self)
        self.__url = bit_z_rest
        self.proxy = proxy

    #所有交易对
    def pairs(self):
        URL = "/api2/1/pairs"
        params=''
        return rsUtilfunc.httpGet(self.__url,URL,params)


    #市场订单参数
    def marketinfo(self):
        URL = "/api2/1/marketinfo"
        params=''
        return rsUtilfunc.httpGet(self.__url,URL,params,self.proxy)

    #交易市场详细行情
    def marketlist(self):
        URL = "/api2/1/marketlist"
        params=''
        return rsUtilfunc.httpGet(self.__url,URL,params,self.proxy)

    #所有交易行情
    def tickers(self):
        URL = "/api2/1/tickers"
        params=''
        return rsUtilfunc.httpGet(self.__url,URL,params,self.proxy)

    #单项交易行情
    def ticker(self,param):
        URL = "/api2/1/ticker"
        return rsUtilfunc.httpGet(self.__url,URL,param,self.proxy)


    # 所有交易对市场深度
    def orderBooks(self):
        URL = "/api2/1/orderBooks"
        param=''
        return rsUtilfunc.httpGet(self.__url, URL, param,self.proxy)


    # 单项交易对市场深度
    def orderBook(self,param):
        URL = "/api2/1/orderBook"
        return rsUtilfunc.httpGet(self.__url, URL, param,self.proxy)


    # 历史成交记录
    def tradeHistory(self, param):
        URL = "/api2/1/tradeHistory"
        return rsUtilfunc.httpGet(self.__url, URL, param,self.proxy)

    # #获取帐号资金余额
    # def balances(self):
    #     URL = "/api2/1/private/balances"
    #     param = {}
    #     return rsUtilfunc.httpPost(self.__url,URL,param,self.__apikey,self.__secretkey)
    #
    #
    # # 获取充值地址
    # def depositAddres(self,param):
    #     URL = "/api2/1/private/depositAddress"
    #     params = {'currency':param}
    #     return rsUtilfunc.httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)
    #
    #
    # # 获取充值提现历史
    # def depositsWithdrawals(self, start,end):
    #     URL = "/api2/1/private/depositsWithdrawals"
    #     params = {'start': start,'end':end}
    #     return rsUtilfunc.httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)
    #
    #
    # # 买入
    # def buy(self, currencyPair,rate, amount):
    #     URL = "/api2/1/private/buy"
    #     params = {'currencyPair': currencyPair,'rate':rate,'amount':amount}
    #     return rsUtilfunc.httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)
    #
    # # 卖出
    # def sell(self, currencyPair, rate, amount):
    #     URL = "/api2/1/private/sell"
    #     params = {'currencyPair': currencyPair, 'rate': rate, 'amount': amount}
    #     return rsUtilfunc.httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)
    #
    # # 取消订单
    # def cancelOrder(self, orderNumber, currencyPair):
    #     URL = "/api2/1/private/cancelOrder"
    #     params = {'orderNumber': orderNumber, 'currencyPair': currencyPair}
    #     return rsUtilfunc.httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)
    #
    #
    # # 取消所有订单
    # def cancelAllOrders(self, type, currencyPair):
    #     URL = "/api2/1/private/cancelAllOrders"
    #     params = {'type': type, 'currencyPair': currencyPair}
    #     return rsUtilfunc.httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)
    #
    #
    # # 获取下单状态
    # def getOrder(self, orderNumber, currencyPair):
    #     URL = "/api2/1/private/getOrder"
    #     params={}
    #     return rsUtilfunc.httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)
    #
    #
    # # 获取我的当前挂单列表
    # def openOrders(self):
    #     URL = "/api2/1/private/openOrders"
    #     params = {}
    #     return rsUtilfunc.httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)
    #
    #
    # # 获取我的24小时内成交记录
    # def mytradeHistory(self,currencyPair,orderNumber):
    #     URL = "/api2/1/private/tradeHistory"
    #     params = {'currencyPair': currencyPair, 'orderNumber': orderNumber}
    #     return rsUtilfunc.httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)
    #
    # # 提现
    # def withdraw(self,currency,amount,address):
    #     URL = "/api2/1/private/withdraw"
    #     params = {'currency': currency, 'amount': amount,'address':address}
    #     return rsUtilfunc.httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)