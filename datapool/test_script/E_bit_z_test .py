# -*- coding: utf-8 -*-
"""
Created on 2018/1/14 18:14

@author: JERRY
"""

from datapool.E_bit_z.E_bit_z_rest.E_bit_z_api import BitZ
import pymysql as ps
from sqlalchemy import create_engine
from utilPool.generalUtil import myThread

ps.install_as_MySQLdb()

proxy = {'http_proxy_host':'119.27.177.169',
         'http_proxy_port':'80'}

tableName = 'bit_z'
conn = create_engine('mysql://root:1qaz@WSX@192.168.8.203/zzmf_trading?charset=utf8', echo=False)

threadList = []
test = BitZ(proxy)
param = 'btc_usdt'

threadList.append(myThread(name='depth', target=test.callback,args=(test.orderBook,param)))

for i in threadList:
    i.start()
