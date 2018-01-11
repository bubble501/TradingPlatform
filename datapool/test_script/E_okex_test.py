
import pymysql as ps
from sqlalchemy import create_engine
from datapool.E_okex.E_okex_ws.E_okex_api import OkexApi
ps.install_as_MySQLdb()
import MySQLdb

stop = False
tablename = 'okex'
conn = create_engine( 'mysql://Jerry:Eli19890908@localhost/datapool?charset=utf8',echo = False)

test = OkexApi()
test.connect()

param = {'depth':{'event':'addChannel',
                  'channel':'ok_sub_spot_btc_usdt_depth_5'}
         }

test.sendMarketDataRequest(param)
# t1 = test.saveData(conn,tablename)
