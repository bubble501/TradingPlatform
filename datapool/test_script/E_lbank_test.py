
import pymysql as ps
from sqlalchemy import create_engine
from datapool.E_lbank.E_lbank_ws.E_lbank_api import Lbank
from utilPool.generalUtil import myThread

ps.install_as_MySQLdb()

proxy = {'http_proxy_host':'101.201.79.172',
         'http_proxy_port':'808'}

tableName = 'lbank'
conn = create_engine( 'mysql://Jerry:Eli19890908@localhost/datapool?charset=utf8',echo = False)

threadList = []
test = Lbank()
param = {'depth':{
    "event" : 'addChannel',
    "channel" : 'lh_sub_spot_eth_btc_depth_20',
}
         }

threadList.append(myThread(name='monitor', target=test.isDisconn))
threadList.append(myThread(name='keepConnect', target=test.keepconnect,kwargs=proxy))
threadList.append(myThread(name='refreshCommand', target=test.refreshCommand, args=(param,)))
threadList.append(myThread(name='saveData',target=test.saveData, args=(conn, tableName)))
for i in threadList:
    i.start()



