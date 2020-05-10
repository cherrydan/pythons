'''
Created on 10 мая 2018 г.

@author: danny
'''
#lastrowid() = возвращает индекс последней добавленной записи при помощи запроса INSERT и метода execute()


# -*- coding:utf-8 -*-

import sqlite3


con = sqlite3.connect("catalog.db")
cur = con.cursor()

try:
    cur.execute("""INSERT INTO rubr (name_rubr) VALUES('Кино')""")

except sqlite3.DatabaseError as err:
    print("Ошибка: ",err)
else:
    con.commit()
    print("Запрос успешно выполнен!")
    print("Индекс последнего добавленного элемента: ", cur.lastrowid)

    cur.close()
    con.close()

    input('Нажмите любую клавишу...') 
    

