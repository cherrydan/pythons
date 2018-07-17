'''
Created on 2 мая 2018 г.

@author: danny

Добавление записи в базу данных SQLITE3
'''
#-*- coding:utf-8 -*-

import sqlite3

con = sqlite3.connect('catalog.db')
cur = con.cursor()

sql = """\
INSERT INTO user(email, passw)
VALUES('unicross@mail.ru','password1')
"""

try:
    cur.execute(sql)
except sqlite3.DatabaseError as err:
    print('Ошибка ', err)

else:
    print('Запрос успешно выполнен')
    con.commit()

cur.close()
con.close()

input('Нажмите любую клавишу...')



