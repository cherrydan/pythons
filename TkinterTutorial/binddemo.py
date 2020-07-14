#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Метод bind()

    Добавляем функционал в наши виджеты

 (c) https://www.youtube.com/watch?v=mm-J9pYBcQ0&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=2
"""

from tkinter import *


def output(event):
    txt = entry_1.get()

    try:
        if int(txt) < 18:
            label_1['text'] = 'Вам ещё рано сюда'
        else:
            label_1['text'] = 'Добро пожаловать!'
    except ValueError:
        label_1['text'] = 'Введите корректное число'


root = Tk()
root.title('Сколько Вам лет?')

entry_1 = Entry(root, width=3, font=15)

button_1 = Button(root, text='Проверить')

label_1 = Label(root, width=27, font=15, )

entry_1.grid(row=0, column=0)
button_1.grid(row=0, column=1)
label_1.grid(row=0, column=2)

button_1.bind('<Button-1>', output)

root.mainloop()
