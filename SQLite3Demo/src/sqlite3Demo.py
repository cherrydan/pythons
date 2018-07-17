'''
Created on 2 мая 2018 г.

@author: danny

СОЗДАНИЕ БАЗЫ ДАННЫХ SQLITE3
'''
#-*- codnig: utf-8 -*-

import sqlite3

con = sqlite3.connect('catalog.db') #соединение с базой
cur = con.cursor() #создание курсора

#запрос на создание базы

sql = """\
        CREATE TABLE user (
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        passw TEXT
        );

        CREATE TABLE rubr (
        id_rubr INTEGER PRIMARY KEY AUTOINCREMENT,
        name_rubr TEXT
        );

        CREATE TABLE site (
        id_site INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user INTEGER,
        id_rubr INTEGER,
        url TEXT,
        title TEXT,
        msg TEXT,
        iq INTEGER
        );
     """

try:
    cur.executescript(sql)

except sqlite3.DatabaseError as err:
    print('Ошибка: ', err)

else:
    print('Запрос успешно выполнен!')

cur.close() #закрываем объект-курсор
con.close() #закрываем соединение

input('Нажмите любую клавишу... ')

