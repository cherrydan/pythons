#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Обработка событий от клавиатуры


 (c) https://www.youtube.com/watch?v=mm-J9pYBcQ0&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=2
"""


from tkinter import *

if __name__ == '__main__':

    def print_char(event):
        label_1.configure(text=event.char)  # передаём нажатую клавишу

    def print_su(event):
        label_1.configure(text='Shift+Up')

    def print_cd(event):
        label_1.configure(text='Ctrl+Down')

    root = Tk()

    label_1 = Label(root, width=12, font=('Ubuntu', 100))
    label_1.pack()

    #  обрабатываем символы от A до Z
    for i in range(65, 123):
        root.bind(chr(i), print_char)

    #  обрабатываем комбинации из нескольких клавиш
    root.bind('<Shift-Up>', print_su)
    root.bind('<Control-Down>', print_cd)

    root.mainloop()
