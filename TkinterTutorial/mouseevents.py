#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Обработка событий от мыши

    Добавляем функционал в наши виджеты

 (c) https://www.youtube.com/watch?v=mm-J9pYBcQ0&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=2
"""

from tkinter import *

if __name__ == '__main__':

    def left_click(event):
        frame_1.configure(bg='red')
        frame_2.configure(bg='white')
        frame_3.configure(bg='white')

    def middle_click(event):
        frame_1.configure(bg='white')
        frame_2.configure(bg='yellow')
        frame_3.configure(bg='white')

    def right_click(event):
        frame_1.configure(bg='white')
        frame_2.configure(bg='white')
        frame_3.configure(bg='green')

    root = Tk()

    # конфигурируем главный виджет
    root.configure(bg='black')

    # cоздаём три фрейма
    frame_1 = Frame(root, width=250, height=250, bg='white')
    frame_2 = Frame(root, width=250, height=250, bg='white')
    frame_3 = Frame(root, width=250, height=250, bg='white')

    frame_1.grid(row=0, column=0)
    # делаем разделительные линии
    frame_2.grid(row=0, column=1, padx=1)
    frame_3.grid(row=0, column=2)

    # ставим обработчик на главное окно, чтобы срабатывало по всему его периметру
    root.bind('<Button-1>', left_click)
    root.bind('<Button-2>', middle_click)
    root.bind('<Button-3>', right_click)

    root.mainloop()
