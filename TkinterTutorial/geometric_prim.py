#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Геометрические примитивы на Tkinter

"""

from tkinter import *

root = Tk()

c_1 = Canvas(root, width=500, height=500, cursor='pencil', bg='white')

c_1.create_line(250, 0, 250, 500, width=2, fill='red')
c_1.create_line(0, 250, 500, 250, width=2, fill='blue')

c_1.create_rectangle(10, 10, 240, 240, fill='green', outline='red')

c_1.create_polygon(260, 10, 490, 10, 400, 125, 490, 240, 260, 240, 350, 125,
                   fill='orange', smooth=1)
c_1.create_oval(10, 260, 240, 340, fill='yellow', outline='red')

#  сектор
c_1.create_arc(10, 350, 90, 430, start=0, extent=270, fill='#0000CC')

#  сегмент
c_1.create_arc(160, 350, 240, 430, start=0, extent=270, fill='#CC0099',
               style='chord')

#  дуга
c_1.create_arc(80, 410, 160, 490, start=0, extent=270, outline='#FF6600',
               style='arc', width=3)


c_1.create_text(275, 330,
                text='Tkinter - \nэто программы\nс оконным интерфейсом',
                font='Verdana 12', anchor='w', justify='center', fill='orange')

c_1.pack()

root.mainloop()
