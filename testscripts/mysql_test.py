# -*- coding: utf-8 -*-
"""
Created on 2018/1/3 13:21 

@author: JERRY
"""
import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.0.102', port=3306, user='Jerry', passwd='Eli19890908', db='datapool', charset='utf8')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from tb7")