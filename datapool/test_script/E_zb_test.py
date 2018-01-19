import pymysql as ps
from sqlalchemy import create_engine
from datapool.E_zb.E_zb_ws.E_zb_api import ZbApi
from utilPool.generalUtil import myThread

ps.install_as_MySQLdb()

proxy = {'http_proxy_host':'220.249.185.178',
         'http_proxy_port':'9999'}

tableName = 'zb'
conn = create_engine('mysql://root:1qaz@WSX@192.168.8.203/zzmf_trading?charset=utf8', echo=False)

threadList = []
test = ZbApi()
param = {'depth':{'event':'addChannel',
                  'channel':'btcusdt_depth'}
         }


threadList.append(myThread(name='monitor', target=test.isDisconn))
threadList.append(myThread(name='keepConnect', target=test.keepconnect,kwargs=proxy))
threadList.append(myThread(name='refreshCommand', target=test.refreshCommand, args=(param,)))
threadList.append(myThread(name='saveData',target=test.saveData,args=(conn,tableName)))
for i in threadList:
    i.start()


