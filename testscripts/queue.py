# -*- coding: utf-8 -*-
"""
Created on 2018/1/10 14:14 

@author: JERRY
"""
from threading import Thread
from time import sleep

def test(x,y):
    print(x+y)

class myThread(Thread):
    def __init__(self,name,func,kwargs = None):
        Thread.__init__(self)
        self.name = name
        self._callback = func
        self._callParam = kwargs
        self.start()

    def run(self):
        if self._callback:
            try:
                self.callback()
            except Exception as e:
                print(e)

    def callback(self):
        if self._callParam is None:
            self._callback()
        try:
            expression = "self._callback("
            for i in list(self._callParam):
                expression+=str(i) + '=' + str(self._callParam[i]) + ','
            return eval(expression[:-1]+')')
        except Exception as e:
            print(e)






