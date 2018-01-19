# -*- coding: utf-8 -*-
"""
Created on 2018/1/16 17:41 

@author: Ji
"""

from datapool.E_bitfinex.E_bitfinex_rest.E_bitfinex_api import BitfinexRest
import pymysql as ps
from sqlalchemy import create_engine
from utilPool.generalUtil import myThread

ps.install_as_MySQLdb()

proxy = {'host': '127.0.0.1',
         'port': 1080}

tableName = 'bitfinex_rest'
conn = create_engine('mysql://root:1qaz@WSX@192.168.8.203/zzmf_trading?charset=utf8', echo=False)

threadList = []
test = BitfinexRest(proxy)

# 测试币种
param = 'btcusd'

threadList.append(myThread(name='getOrderBook', target=test.callback, args=(test.getOrderBook, param)))
threadList.append(myThread(name='saveData', target=test.saveData, args=(conn, tableName)))

for i in threadList:
    i.start()

# import pymysql as ps
# from sqlalchemy import create_engine
# from datapool.E_bitfinex.E_bitfinex_ws.E_bitfinex_api import BitfinexWs
# from utilPool.generalUtil import myThread
#
# ps.install_as_MySQLdb()
#
# proxy = {'http_proxy_host': '118.114.77.47',
#          'http_proxy_port': '8080'}
#
# tableName = 'bitfinex_ws'
# conn = create_engine('mysql://root:1qaz@WSX@192.168.8.203/zzmf_trading?charset=utf8', echo=False)
#
# threadList = []
# test = BitfinexWs()
# param = {'orderbook':
#              {'event': 'subscribe', 'channel': 'book', 'pair': 'BTCUSD', 'prec': 'P0', 'freq': 'F0', 'len': '25'}
#          }
#
# threadList.append(myThread(name='monitor', target=test.isDisconn))
# threadList.append(myThread(name='keepConnect', target=test.keepconnect, kwargs=proxy))
# threadList.append(myThread(name='refreshCommand', target=test.refreshCommand, args=(param,)))
# threadList.append(myThread(name='savedata', target=test.saveData, args=(conn, tableName)))
# for i in threadList:
#     i.start()
