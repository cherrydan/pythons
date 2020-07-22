#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    Использование ООП при работе с Tkinter

"""

from tkinter import *


class Question:
    def __init__(self, main):  # main - ссылка на главное окно
        self.entry_1 = Entry(main, width=3, font=15)
        self.button_1 = Button(main, text='Проверить')
        self.label_1 = Label(main, width=27, font=15)
        self.entry_1.grid(row=0, column=0)
        self.button_1.grid(row=0, column=1)
        self.label_1.grid(row=0, column=2)

        self.button_1.bind('<Button-1>', self.answer)

    def answer(self, event):
        txt = self.entry_1.get()
        try:
            if int(txt) < 18:
                self.label_1['text'] = 'Вам ещё рано сюда'
            else:
                self.label_1['text'] = 'Добро пожаловать!'
        except ValueError:
            self.label_1['text'] = 'Введите корректное число'


root = Tk()
root.title('Сколько Вам лет?')

q = Question(root)

root.mainloop()
