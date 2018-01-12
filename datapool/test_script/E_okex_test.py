
import pymysql as ps
from sqlalchemy import create_engine
# from threading import Thread
from datapool.E_okex.E_okex_ws.E_okex_api import OkexApi
from utilPool.generalUtil import myThread

ps.install_as_MySQLdb()

proxy = {'http_proxy_host':'118.114.77.47',
         'http_proxy_port':'8080'}

tableName = 'okex'
conn = create_engine( 'mysql://Jerry:Eli19890908@localhost/datapool?charset=utf8',echo = False)

threadList = []
test = OkexApi()
param = {'depth':{'event':'addChannel',
                  'channel':'ok_sub_spot_btc_usdt_depth_5'}
         }

threadList.append(myThread(name='monitor', target=test.isDisconn))
threadList.append(myThread(name='keepConnect', target=test.keepconnect,kwargs=proxy))
threadList.append(myThread(name='refreshCommand', target=test.refreshCommand, args=(param,)))
# threadList.append(myThread(name='savedata',target=test.saveData,args=(conn,tableName)))
for i in threadList:
    i.start()
# test.sendMarketDataRequest(param)
# t1 = test.saveData(conn,tablename)
