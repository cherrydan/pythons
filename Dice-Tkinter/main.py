#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Игра в кости в графическом варианте,
используя tkinter
"""
from tkinter import *
import random
import time


def bros():
    """
    Функция бросает кость,
    выкидывая картинку с заданным числом
    возвращает имя файла
    """
    x = random.choice(['b.png', 'b2.png', 'b3.png', 'b4.png',
                       'b5.png', 'b6.png'])
    return x


def img(event):
    """
    Запускается с кнопки
    """
    global b1, b2
    for i in range(10):
        b1 = PhotoImage(file=bros())
        b2 = PhotoImage(file=bros())
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.12)


root = Tk()
root.geometry('400x200')
root.title('Игра в кости')
root.resizable(0, 0)

root.iconphoto(True, PhotoImage(file='iconka.png'))

font = PhotoImage(file='holst.png')
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)

lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)

root.bind('<1>', img)
img('event')

if __name__ == '__main__':
    root.mainloop()
