#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Организация главного окна в Tkinter

    (c) https://www.youtube.com/watch?v=mm-J9pYBcQ0&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=2

"""

from tkinter import *


def main():
    root = Tk()
    # создаём верхнюю область
    top_frame = Frame(root)
    top_frame.pack()

    # создаём нижнюю область
    bottom_frame = Frame(root)
    bottom_frame.pack(side=BOTTOM)

    # создаём кнопки и помещаем их в контейнер вверху и внизу
    button_1 = Button(top_frame, text='Кнопка1', fg='red')
    button_2 = Button(top_frame, text='Кнопка2', fg='blue')
    button_3 = Button(top_frame, text='Кнопка3', fg='green')
    button_4 = Button(bottom_frame, text='Кнопка4', fg='gray')

    # отображаем кнопки
    button_1.pack(side=LEFT)
    button_2.pack(side=LEFT)
    button_3.pack(side=LEFT)
    button_4.pack(side=BOTTOM)

    root.mainloop()


if __name__ == '__main__':
    main()
