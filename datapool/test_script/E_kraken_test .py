# -*- coding: utf-8 -*-
"""
Created on 2018/1/14 18:14

@author: JERRY
"""

from datapool.E_kraken.E_kraken_rest.E_kraken_api import Kraken
import pymysql as ps
from sqlalchemy import create_engine
from utilPool.generalUtil import myThread

ps.install_as_MySQLdb()

proxy = {'http_proxy_host':'119.27.177.169',
         'http_proxy_port':'80'}

tableName = 'kraken'
conn = create_engine('mysql://root:1qaz@WSX@192.168.8.203/zzmf_trading?charset=utf8', echo=False)

threadList = []
test = Kraken(proxy)
param = {'pair': 'XXBTZUSD', 'count': '10'}

threadList.append(myThread(name='depth', target=test.callback, args=(test.orderBook, param)))
threadList.append(myThread(name='saveData', target=test.saveData, args=(conn, tableName)))


for i in threadList:
    i.start()
















