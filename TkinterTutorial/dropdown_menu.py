#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    Выпадающее меню на Tkinter

"""

from tkinter import *


def new_win():
    win = Toplevel(root)  # Создаём новое окно уровнем выше
    label_1 = Label(win, text='Текст в окне верхнего уровня', font=20)
    label_1.pack()


def exit_app():
    root.destroy()  # закрытие всех окон


root = Tk()

root.title('Main menu')

# создаем главное меню
main_menu = Menu(root)

root.configure(menu=main_menu)

# создаём подменю
first_item = Menu(main_menu)
main_menu.add_cascade(label='File', menu=first_item)

first_item.add_command(label='New', command=new_win)
first_item.add_command(label='Exit', command=exit_app)

# tearoff - запрещает отрывание меню от окна
second_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Edit', menu=second_item)

second_item.add_command(label='Item1')
second_item.add_command(label='Item2')
second_item.add_command(label='Item3')
second_item.add_separator()  # сепаратор
second_item.add_command(label='Item4')
second_item.add_command(label='Item5')

root.mainloop()
