#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    Панель инструментов и статус-бар на Tkinter

"""

from tkinter import *
from PIL import ImageTk


def new_win():
    win = Toplevel(root)  # Создаём новое окно уровнем выше
    label_1 = Label(win, text='Текст в окне верхнего уровня', font=20)
    label_1.pack()


def exit_app():
    root.destroy()  # закрытие всех окон


def tlb_copy():
    status_bar.configure(text='Selected text copied!')


def tlb_cut():
    status_bar.configure(text='Selected text cut!')


def tlb_insert():
    status_bar.configure(text='Selected text inserted!')


root = Tk()

root.title('Toolbar & Status Bar')
root.geometry('640x320')


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

#  создаём ToolBar на базе Frame
tool_bar = Frame(root, bg='#A1A1A1')
tool_bar.pack(side=TOP, fill=X)

# приделываем к кнопкам изображение
cut_image = ImageTk.PhotoImage(file='cut.png')
button_1 = Button(tool_bar, image=cut_image, text='Cut', command=tlb_cut)
button_1.grid(row=0, column=0, padx=2, pady=2)

copy_image = ImageTk.PhotoImage(file='copy.png')
button_2 = Button(tool_bar, image=copy_image, text='Copy', command=tlb_copy)
button_2.grid(row=0, column=1, padx=2, pady=2)

insert_image = ImageTk.PhotoImage(file='insert.png')
button_3 = Button(tool_bar, image=insert_image, text='Paste',
                  command=tlb_insert)
button_3.grid(row=0, column=2, padx=2, pady=2)

# создаём статус-бар на базе класса Label
# relief - описывает тип рамки
status_bar = Label(root, relief=SUNKEN, anchor=W, text='Working...')
status_bar.pack(side=BOTTOM, fill=X)


root.mainloop()
