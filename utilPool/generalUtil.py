# -*- coding: utf-8 -*-
"""
Created on 2018/1/10 16:34 

@author: JERRY
"""
from threading import Thread
import ctypes
import inspect
from time import sleep


class myThread(Thread):

    def __init__(self, name = None, target=None, *args, **kwargs):
        Thread.__init__(self, name=name, target=target, *args, **kwargs)

    def _async_raise(self, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(self.ident)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    def close(self):
        self._async_raise(SystemExit)
        print(self.name + ' has been killed!')


if __name__ == '__main__':
    def t1(x = 0, y = 0, z = 0):
        while True:
            print(x+y+z)
            sleep(1)

    param = {'x':1,'z':2}

    test = myThread(name='test',target=t1,kwargs=param)
    test.start()
