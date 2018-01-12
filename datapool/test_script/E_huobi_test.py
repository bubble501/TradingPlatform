# -*- coding: utf-8 -*-
"""
Created on 2018/1/12 11:53 

@author: JERRY
"""

import pymysql as ps
from sqlalchemy import create_engine
from datapool.E_huobi.E_huobi_ws.E_huobi_api import HuobiApi
from utilPool.generalUtil import myThread

ps.install_as_MySQLdb()

proxy = {'http_proxy_host':'125.210.121.113',
         'http_proxy_port':'3128'}

tableName = 'huobi'
conn = create_engine('mysql://root:1qaz@WSX@192.168.8.203/zzmf_trading?charset=utf8',echo = False)

threadList = []
test = HuobiApi()
param = {'depth':{'sub':'market.btcusdt.depth.step5',
                  'id':'id1'}
         }

threadList.append(myThread(name='monitor', target=test.isDisconn))
threadList.append(myThread(name='keepConnect', target=test.keepconnect,kwargs=proxy))
threadList.append(myThread(name='refreshCommand', target=test.refreshCommand, args=(param,)))
threadList.append(myThread(name='saveData',target=test.saveData,args=(conn,tableName)))
for i in threadList:
    i.start()

