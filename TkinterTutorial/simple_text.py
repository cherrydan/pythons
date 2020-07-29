#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Диалоговые окна на Tkinter часть 3.


Простейший текстовый редактор

"""
from tkinter.filedialog import *
from tkinter import *


def open_file():
    # открываем файл стандартными для Tkinter средствами
    of = askopenfilename()

    #  очищаем поле от предыдущего текста
    txt.delete(1.0, END)

    with open(of, 'r') as file:
        txt.insert(END, file.read())


def save_file():
    sf = asksaveasfilename()
    final_text = txt.get(1.0, END)

    with open(sf, 'w') as file:
        file.write(final_text)


def exit_app():
    root.quit()


root = Tk()

main_menu = Menu(root)
root.configure(menu=main_menu)
first_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=first_item)
first_item.add_command(label='Open...', command=open_file)
first_item.add_command(label='Save...', command=save_file)
first_item.add_command(label='Exit', command=exit_app)

txt = Text(root, height=15, width=40, font=13)
txt.pack(expand=YES, fill=BOTH)

root.mainloop()
