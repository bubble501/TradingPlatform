# -*- coding: utf-8 -*-
"""
Created on 2018/1/9 20:34

@author: JERRY
"""

def test(x = 0, y = 0, z = 0):
    print(x+y+z)
t1 = test
arg = {"y":1, "z":2}
t1(**arg)