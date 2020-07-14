#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Работа с упаковщиком grid()

 (c) https://www.youtube.com/watch?v=mm-J9pYBcQ0&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=2
"""

from tkinter import *


def main():
    root = Tk()
    label_1 = Label(root, text="Имя")
    label_2 = Label(root, text="Пароль")

    entry_1 = Entry(root)
    entry_2 = Entry(root)

    # выравниваем элементы по сетке
    # принцип как в таблице = ряд, колонка
    # skicky = привязка элементов по стороне света N, W, S, E
    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1)

    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)

    # Создаём виджет, который будет захватывать облаcть двух колонок
    c = Checkbutton(root, text='Остаться в системе')
    c.grid(columnspan=2)

    # кнопки
    ok_button = Button(text="OK")
    ok_button['activeforeground'] = 'white'
    ok_button['activebackground'] = 'green'
    ok_button.grid(row=3, column=0, sticky=W)

    cancel_button = Button(text='Отменить')
    cancel_button['activebackground'] = 'red'
    cancel_button['activeforeground'] = 'white'
    cancel_button.grid(row=3, column=1, sticky=W)

    root.mainloop()


if __name__ == '__main__':
    main()
