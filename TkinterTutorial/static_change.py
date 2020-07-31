#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Геометрические примитивы на Tkinter
Статическое изменение фигур.

"""
from tkinter import *


def create_outline(event):
    c_1.itemconfigure(oval_1, outline='blue', width=3)


def change_fill(event):
    c_1.itemconfigure(oval_2, fill='orange')
    c_1.coords(oval_2, 250, 10, 390, 90)


def move_ovals(event):
    c_1.move('ovals', 0, 230)


def clear_canvas(event):
    c_1.delete('all')


root = Tk()
c_1 = Canvas(root, width=400, height=400, bg='white')
c_1.pack()

oval_1 = c_1.create_oval(10, 10, 90, 90, fill='red', width=0, tag='ovals')
oval_2 = c_1.create_oval(310, 10, 390, 90, fill='blue', width=0, tag='ovals')
triangle_1 = c_1.create_polygon(200, 200, 10, 390, 390, 390, fill='green')

# привязка событий к фигурам
c_1.tag_bind(oval_1, '<Button-1>', create_outline)
c_1.tag_bind(oval_2, '<Button-1>', change_fill)
c_1.tag_bind(triangle_1, '<Button-1>', move_ovals)


# при нажатии на правую кнопку мыши, очищаем весь холст
root.bind('<Button-3>', clear_canvas)

root.mainloop()
