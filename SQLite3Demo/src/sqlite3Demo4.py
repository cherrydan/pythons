'''
Created on 3 мая 2018 г.

@author: danny
'''

#Передача данных при помощи запроса executemany()

#-*- coding:utf-8 -*-
import sqlite3

con = sqlite3.connect('catalog.db')
cur = con.cursor()

arr = [
        (1,1,"http://wwwadmin.","Название","",100),
        (1,2,"http://python.org","Python","",1000),
        (1,3,"http://google.com","Гугл","",3000)
    ]

sql = """\
        INSERT INTO site (id_user, id_rubr, url, title, msg, iq)
        VALUES (?,?,?,?,?,?)
      """

try:
    cur.executemany(sql,arr)

except sqlite3.DatabaseError as err:
    print('Ошибка: ', err)
else:
    print('Запрос успешно выполнен')
    con.commit()

cur.close()
con.close()

input('Нажмите любую клавишу...')
