#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Диалоговые окна на Tkinter часть 2.


Диалоговые окна

"""

from tkinter import *
from tkinter.messagebox import *


def ask_question(event):
    answer = askquestion('Ask Question', 'Вам есть 18 лет?')
    if answer == 'yes':
        label_1.configure(text='Sex!')
    else:
        label_1.configure(text='No sex!')


def ask_ok(event):
    answer = askokcancel('Ask OK', 'Закрыть окно?')
    label_2.configure(text=answer)


def ask_yes(event):
    answer = askyesno('Ask YES', 'Всегда говори ДА!')
    label_3.configure(text=answer)


def ask_retry(event):
    answer = askretrycancel('Ask RETRY',
                            'Произошла ошибка.\nПовторить запись?')
    label_4.configure(text=answer)


root = Tk()


root.title('Виды диалогов')

# первая кнопка будет запрашивать у нас Да или Нет
button_1 = Button(root, text='Ask Question', font=('Ubuntu', 20), width=12)

button_1.configure(bg='green', activebackground='green', fg='white',
                   activeforeground='white')

button_1.grid(row=0, column=0, sticky='EW')

label_1 = Label(root, font=('Ubuntu', 16), width=12)
label_1.grid(row=0, column=1)

button_1.bind('<Button-1>', ask_question)

# вторая кнопка будет у нас спрашивать OK или CANCEL
button_2 = Button(root, text='Ask OК-CANCEL', font=('Ubuntu', 20), width=12)

button_2.configure(bg='blue', activebackground='blue', fg='white',
                   activeforeground='white')

button_2.grid(row=1, column=0, sticky='EW')

label_2 = Label(root, font=('Ubuntu', 16), width=12)
label_2.grid(row=1, column=1)

button_2.bind('<Button-1>', ask_ok)

# третья кнопка будет у нас спрашивать YES или NO
button_3 = Button(root, text='Ask YES-NO', font=('Ubuntu', 20), width=12)

button_3.configure(bg='orange', activebackground='orange', fg='white',
                   activeforeground='white')

button_3.grid(row=2, column=0, sticky='EW')

label_3 = Label(root, font=('Ubuntu', 16), width=12)
label_3.grid(row=2, column=1)

button_3.bind('<Button-1>', ask_yes)

# четвёртая кнопка будет у нас спрашивать RETRY или CANCEL
button_4 = Button(root, text='Ask RETRY', font=('Ubuntu', 20), width=12)

button_4.configure(bg='red', activebackground='red', fg='white',
                   activeforeground='white')

button_4.grid(row=3, column=0, sticky='EW')

label_4 = Label(root, font=('Ubuntu', 16), width=12)
label_4.grid(row=3, column=1)


button_4.bind('<Button-1>', ask_retry)

root.mainloop()
