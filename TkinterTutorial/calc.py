# -*- coding: utf-8 -*-
"""
    Учебник по Tkinter
    https://younglinux.info/tkinter/tkinter.php

    Практическая работа: написать калькулятор
    (c) danny, 2020

    Модуль описывает класс Calc
"""

from tkinter import *

class Calc:
    def __init__(self, master):
        self.val_1 = Entry(master, width=20)
        self.val_2 = Entry(master, width=20)
        self.b_plus = Button(master, text='+')
        self.b_minus = Button(master, text='-')
        self.b_mult = Button(master, text='*')
        self.b_div = Button(master, text='/')
        self.l = Label(master, bg='black', fg='green', width=20)
        self.val_1.pack(side=LEFT, padx = 5, pady = 5)
        self.val_2.pack(side = RIGHT, padx = 5, pady = 5)
        self.b_plus.pack(side = BOTTOM, padx = 5, pady = 5)
        self.b_minus.pack(side = BOTTOM, padx = 5, pady = 5)
        self.b_mult.pack(side = BOTTOM, padx = 5, pady = 5)
        self.b_div.pack(side = BOTTOM, padx = 5, pady = 5)
        self.l.pack(side=TOP, padx = 5, pady = 5, expand = True)

        # устанавливаем кнопку на обработчик
    def setFunc(self, func):
        if func == 'add':
            self.b_plus['command'] = eval('self.' + func)
        elif func == 'sub':
            self.b_minus['command'] = eval('self.' + func)
        elif func == 'mul':
            self.b_mult['command'] = eval('self.' + func)
        elif func == 'div':
            self.b_div['command'] = eval('self.' + func)

    def add(self):
        try:
            res = float(self.val_1.get()) + float(self.val_2.get())
            self.l['text'] = str(res)
        except ValueError:
            self.l['text'] = 'Error!'

    def sub(self):
        try:
            res = float(self.val_1.get()) - float(self.val_2.get())
            self.l['text'] = str(res)
        except ValueError:
            self.l['text'] = 'Error!'


    def mul(self):
        try:
            res = float(self.val_1.get()) * float(self.val_2.get())
            self.l['text'] = str(res)
        except ValueError:
            self.l['text'] = 'Error!'


    def div(self):
        try:
            res = float(self.val_1.get()) / float(self.val_2.get())
            self.l['text'] = str(res)
        except ValueError:
            self.l['text'] = 'Error!'

        except ZeroDivisionError:
            self.l['text'] = 'Divizion by Zero!'



