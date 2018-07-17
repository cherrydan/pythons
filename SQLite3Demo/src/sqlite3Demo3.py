'''
Created on 2 мая 2018 г.

@author: danny
'''
# -*- coding:utf-8 -*-

import sqlite3

con = sqlite3.connect('catalog.db')
cur = con.cursor()

t1 = ("Программирование",) #кортеж
t2 = (2, "Музыка")

d = {"id":3, "name":"""Поисковые ' " порталы""" } #словарь

sql_t1 = "INSERT INTO rubr (name_rubr) VALUES(?)"
sql_t2 = "INSERT INTO rubr VALUES(?,?)"
sql_d = "INSERT INTO rubr VALUES(:id,:name)"

try:
    cur.execute(sql_t1, t1)
    cur.execute(sql_t2, t2)
    cur.execute(sql_d,d)

except sqlite3.DatabaseError as err:
    print('Ошибка: ', err)
else:
    print('Запрос успешно выполнен')

cur.close()
con.close()

input('Нажмите любую клавишу...')