# -*- coding: utf-8 -*-
"""
Created on 2018/1/3 13:36 

@author: JERRY
"""

from datapool.E_bitmex.E_bitmex_api import BitmexApi

# apikey = 'TcLgPRVt5ToBHGaXWffvqrG3ZTbwfaP9Rt4vJ4TgswB97hxbnizTXc8cdIYtCdyg'
# srtkey = 'CpVMbJrVZIExkt2ye1vAzZNLBuuxFRqmpLozTT15qD1Cgj3lrS5J3tiF9itg9CFF'

api = BitmexApi()
api.connect()
# api.sendMarketDataRequest(['orderBookL2:XBTUSD'])