# -*- coding: utf-8 -*-
"""
Created on 2018/1/12 11:53 

@author: JERRY
"""
from datapool.E_hitbtc.E_hitbtc_rest.E_hitbtc_api import HitBtc
import pymysql as ps
from sqlalchemy import create_engine
from utilPool.generalUtil import myThread

ps.install_as_MySQLdb()

proxy = {'http_proxy_host':'119.27.177.169',
         'http_proxy_port':'80'}

tableName = 'hitbtc'
conn = create_engine('mysql://root:1qaz@WSX@192.168.8.203/zzmf_trading?charset=utf8', echo=False)

threadList = []
test = HitBtc(proxy)
param = 'BTCUSD'

threadList.append(myThread(name='depth', target=test.callback, args=(test.orderBook, param)))
threadList.append(myThread(name='saveData', target=test.saveData, args=(conn, tableName)))


for i in threadList:
    i.start()