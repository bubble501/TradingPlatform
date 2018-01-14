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

proxy = {'http_proxy_host':'101.201.79.172',
         'http_proxy_port':'808'}

tableName = 'huobi'
conn = create_engine( 'mysql://Jerry:Eli19890908@localhost/datapool?charset=utf8',echo = False)

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

