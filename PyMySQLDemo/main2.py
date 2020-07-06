#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Демонстрация функций модуля pymysql
"""
from  pymysql import *

con = connect('localhost', 'root', '',
        'base')

country = input('Enter a country name: ')

with con:
    cur = con.cursor()
    cur.execute('SELECT * FROM country_pop WHERE country=%s', country)
    rows = cur.fetchall()
    print('\nCountry\t\tYear\tPopulation')
    print()
    for row in rows:
        print("{0}\t{1}\t{2}".format(row[1], row[2], row[3]))

