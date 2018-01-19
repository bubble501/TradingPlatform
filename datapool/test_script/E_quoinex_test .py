import pymysql as ps
from sqlalchemy import create_engine
from datapool.E_quoinex.E_quoinex_ws.E_quoinex_api import QuoinexApi
from utilPool.generalUtil import myThread

ps.install_as_MySQLdb()

proxy = {'http_proxy_host':'220.249.185.178',
         'http_proxy_port':'9999'}

tableName = 'quoinex'
conn = create_engine('mysql://root:1qaz@WSX@192.168.8.203/zzmf_trading?charset=utf8', echo=False)

threadList = []
test = QuoinexApi()
param = {'depth':{'EVENT':'updated',
                  'CHANNEL':'product_cash_btcusd_1'}
         }



threadList.append(myThread(name='monitor', target=test.isDisconn))
threadList.append(myThread(name='keepConnect', target=test.keepconnect,kwargs=proxy))
threadList.append(myThread(name='refreshCommand', target=test.refreshCommand, args=(param,)))
threadList.append(myThread(name='saveData',target=test.saveData,args=(conn,tableName)))
for i in threadList:
    i.start()


