# -*- coding: utf-8 -*-
"""
Created on 2018/1/15 10:51 

@author: JERRY
"""

import gzip
from datetime import datetime
import pandas as pd
from time import sleep

import time
import json
import pymysql as ps
from sqlalchemy import create_engine
import pandas as pd
ps.install_as_MySQLdb()
from datetime import datetime
import numpy as np
import math
import copy


class dataUtilfunc:

    def __init__(self):
        self.status = 0
        self.refreshSend = 0
        self.ws = None  # websocket应用对象
        self.res = []

    def readData(self, evt):
        """解压缩推送收到的数据"""
        data = gzip.decompress(evt).decode('utf-8')
        return data

    def saveData(self, conn, tableName):
        """保存数据"""
        while True:
            if self.status:
                sleep(10)
                tmp_ = pd.DataFrame(self.res, columns=['data'])
                self.res = []
                tmp_.to_sql(tableName, conn, if_exists='append')
                print('当前时间为' + str(datetime.now()) + ',数据长度为' + str(len(tmp_)) + ',正在储存数据...')

    def isDisconn(self):
        """返回状态"""
        while True:
            if self.ws:
                try:
                    if self.ws.sock.connected:
                        self.status = 1
                except Exception as e:
                    self.status = 0
                    self.refreshSend = 0
                finally:
                    pass
            sleep(1)


class plat_clean:
      def __init__(self,platform):
            if platform=='okex':
               conn = create_engine('mysql://root:1qaz@WSX@192.168.8.203/zzmf_trading?charset=utf8', echo=False)
               sql = 'select * from okex'
               df = pd.read_sql(sql, conn)
               df_0 = [json.loads(x) for x in df['data']]
               sorted_df = pd.DataFrame(df_0).sort(['timestamp'], ascending=True)
               sorted_df['ts'] = sorted_df['timestamp'].map(lambda x: math.floor(x / 1000))
               sorted_df = sorted_df.drop(['timestamp'], axis=1)
               sorted_df = sorted_df.drop_duplicates('ts', keep='last')
               time_list = sorted_df.iloc[:, 2].tolist()
               asks_list = self.ok_string_float(sorted_df.iloc[:, 0].tolist())
               asks_list_reverse = []
               for i in range(len(asks_list)):
                   asks_list_reverse.append(list(reversed(asks_list[i])))

               bids_list = self.ok_string_float(sorted_df.iloc[:, 1].tolist())
               whole = list(zip(time_list, bids_list, asks_list_reverse))
               start_time = whole[0][0]
               end_time = whole[-1][0]
               new_time = list([i for i in range(start_time, end_time)])
               sorted_df.index = range(len(sorted_df))
               okex_list = []
               old_index = 0
               for seconds in range(start_time, end_time):

                 if (sorted_df.loc[old_index, 'ts'] <= seconds) &(seconds<= sorted_df.loc[old_index + 1, 'ts']):
                    okex_list.append(list([seconds, whole[old_index][1], whole[old_index][2]]))
                 else:
                    old_index = old_index + 1
                    okex_list.append(list([seconds, whole[old_index][1], whole[old_index][2]]))

               self.market_depth = okex_list


            elif platform=='huobi':
                 conn = create_engine('mysql://root:1qaz@WSX@192.168.8.203/zzmf_trading?charset=utf8', echo=False)
                 sql = 'select * from huobi'
                 df = pd.read_sql(sql, conn)
                 df_0 = [json.loads(x) for x in df['data']]
                 df_t = pd.DataFrame(df_0)

                 df_t['currency'] = 'BTC/USDT'
                 df_t['time_quote'] = df_t['ts'].map(lambda x: math.floor(x / 1000))
                 df = df_t.drop_duplicates('time_quote', keep='last')
                 df.index = range(len(df))
                 df_new = df.drop(['ch', 'ts'], axis=1)
                 ask_list = []
                 bid_list = []
                 for i in range(len(df_new)):
                     ask_list.append(df_new['tick'][i]['asks'])
                     bid_list.append(df_new['tick'][i]['bids'])

                 time_list = []
                 for i in range(len(df_0)):
                     time = df_0[i]['ts']
                     time_list.append(math.floor(time / 1000))

                 whole = list(zip(time_list, bid_list, ask_list))
                 start_time = whole[0][0]
                 end_time = whole[-1][0]
                 new_time = list([i for i in range(start_time, end_time)])
                 df_new.index = range(len(df_new))
                 huobi_list = []
                 old_index = 0

                 for seconds in range(start_time, end_time):

                     if (df_new.loc[old_index, 'time_quote'] <= seconds <= df_new.loc[old_index + 1, 'time_quote']):
                         huobi_list.append(list([seconds, whole[old_index][1], whole[old_index][2]]))
                     else:
                         old_index = old_index + 1
                         huobi_list.append(list([seconds, whole[old_index][1], whole[old_index][2]]))

                 self.market_depth= huobi_list

            else:
               print('platform undefined!');


      def ok_string_float(self, x):
         xx = copy.deepcopy(x)
         for i in range(len(x)):
             first_l = x[i]
             for j in range(len(first_l)):
                 second_l = first_l[j]
                 for k in range(len(second_l)):
                     xx[i][j][k] = float(x[i][j][k])
         return xx


if __name__ == '__main__':
     huobi=plat_clean('huobi')
     huobi_list=huobi.market_depth