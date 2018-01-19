from datapool.E_livecoin.E_livecoin_rest.E_livecoin_api import LiveCoin
import pymysql as ps
from sqlalchemy import create_engine
from utilPool.generalUtil import myThread
import urllib
from collections import OrderedDict

ps.install_as_MySQLdb()

proxy = {'http_proxy_host':'119.27.177.169',
         'http_proxy_port':'80'}

tableName = 'livecoin'
conn = create_engine('mysql://root:1qaz@WSX@192.168.8.203/zzmf_trading?charset=utf8', echo=False)

threadList = []
test = LiveCoin(proxy)
data = OrderedDict([('currencyPair', 'BTC/EUR')])
param = urllib.parse.urlencode(data)


threadList.append(myThread(name='depth', target=test.callback, args=(test.orderBook, param)))
threadList.append(myThread(name='saveData', target=test.saveData, args=(conn, tableName)))


for i in threadList:
    i.start()

