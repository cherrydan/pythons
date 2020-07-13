#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()

b1 = Button(text='Change', width=15, height=3)
b1.pack()


# обработчик события
def change():
    b1['text'] = 'Changed!'
    b1['bg'] = '#000000'
    b1['activebackground'] = '#555555'
    b1['fg'] = '#FFFFFF'
    b1['activeforeground'] = '#FFFFFF'


b1.config(command=change)

if __name__ == '__main__':
    root.mainloop()
