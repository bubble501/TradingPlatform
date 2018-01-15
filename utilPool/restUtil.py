# -*- coding: utf-8 -*-
"""
Created on 2018/1/14 17:35

@author: JERRY
"""

import http.client
import urllib
from hashlib import sha512
import hmac
from time import sleep
import requests
from utilPool.dataUtil import dataUtilfunc


class rsUtilfunc(dataUtilfunc):
    def __init__(self):
        dataUtilfunc.__init__(self)

    @staticmethod
    def getSign(params, secretKey):
        sign = ''
        for key in (params.keys()):
            sign += key + '=' + str(params[key]) + '&'
        sign = sign[:-1]
        my_sign = hmac.new(bytes(secretKey, encoding='utf8'), bytes(sign, encoding='utf8'), sha512).hexdigest()
        return my_sign

    @staticmethod
    def httpGet(url, resource, params='', proxy={}):
        proxy = {'http':proxy.get('host')+':'+str(proxy.get('port'))}
        data = requests.get(url + resource + '/' + params, proxies=proxy)
        return data.json()

    # @staticmethod
    # def httpPost(url, resource, params, apikey, secretkey):
    #     headers = {
    #         "Content-type": "application/x-www-form-urlencoded",
    #         "KEY": apikey,
    #         "SIGN": rsUtilfunc.getSign(params, secretkey)
    #     }
    #     conn = http.client.HTTPSConnection(url, timeout=10)
    #     if params:
    #         temp_params = urllib.parse.urlencode(params)
    #     else:
    #         temp_params = ''
    #     print(temp_params)
    #     conn.request("POST", resource, temp_params, headers)
    #     response = conn.getresponse()
    #     data = response.read().decode('utf-8')
    #     params.clear()
    #     conn.close()
    #     return data

    @staticmethod
    def callback(callback, *args, **kwargs):
        if callback:
            while True:
                try:
                    print(callback(*args, **kwargs))
                except Exception as e:
                    raise e
                sleep(0.5)
