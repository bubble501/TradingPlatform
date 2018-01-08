
import pandas as pd
from time import sleep
import json
from datapool.E_okex.E_okex_ws.E_okex_api import OkexApi


stop = False
tablename = 'okex'

test = OkexApi()
test.connect()

param = {'depth':{'event':'addChannel',
                  'channel':'ok_sub_spot_btc_usdt_depth_5'}
         }

while not stop:
    if test.ws.sock.connected:
        test.sendMarketDataRequest(param)
        # t1 = test.saveData(tablename)
        stop = True