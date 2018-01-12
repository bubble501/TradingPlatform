# -*- coding: utf-8 -*-
"""
Created on 2018/1/8 16:29

@author: JERRY
"""

import pymysql as ps
from sqlalchemy import create_engine
from datapool.E_huobi.E_huobi_ws.E_huobi_api import HuobiApi
from datapool.E_okex.E_okex_ws.E_okex_api import OkexApi
from utilPool.generalUtil import myThread
from datapool.general_config import *

ps.install_as_MySQLdb()



class exInitial():
    def __init__(self):
        pass
