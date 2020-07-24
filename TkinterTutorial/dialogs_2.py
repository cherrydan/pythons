#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Диалоговые окна на Tkinter часть 1.


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


root = Tk()


root.title('Викторина')

#  для обработчика используем анонимную функцию
button_1 = Button(root, text='Ask Question', font=('Ubuntu', 20), width=12)

button_1.configure(bg='green', activebackground='green', fg='white',
                   activeforeground='white')

button_1.grid(row=0, column=0, sticky='EW')

label_1 = Label(root, font=('Ubuntu', 16), width=12)
label_1.grid(row=0, column=1)

button_1.bind('<Button-1>', ask_question)

root.mainloop()
