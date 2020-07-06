#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Демонстрация функций модуля pymysql
"""
from  pymysql import *

con = connect('localhost', 'root', '',
        'base')

with con:
    cur = con.cursor()
    cur.execute('SELECT VERSION()')

    version = cur.fetchone()
    print('Версия БД: {}'.format(version[0]))


