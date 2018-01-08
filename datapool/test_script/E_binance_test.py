# -*- coding: utf-8 -*-
"""
Created on 2018/1/3 13:21 

@author: JERRY
"""

from datapool.E_binance.E_binance_api import BinanceApi

# apikey = 'TcLgPRVt5ToBHGaXWffvqrG3ZTbwfaP9Rt4vJ4TgswB97hxbnizTXc8cdIYtCdyg'
# srtkey = 'CpVMbJrVZIExkt2ye1vAzZNLBuuxFRqmpLozTT15qD1Cgj3lrS5J3tiF9itg9CFF'

api = BinanceApi()
api.connect('btcusdt','depth')