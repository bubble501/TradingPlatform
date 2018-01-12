# -*- coding: utf-8 -*-
"""
Created on 2018/1/11 16:31

@author: JERRY
"""

from datapool.E_okex.E_okex_ws.E_okex_api import okex_ws


class exManager:
    def __init__(self):
        self.exdict = {}
        self.tasknamelist = ['connect', 'sendMsg', 'tsaveData', 'earning']

    def addExchanges(self, exchangeNames):
        self.exdict[exchangeNames] = None

    def run(self):

