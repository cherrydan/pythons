#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Диалоговые окна на Tkinter часть 1.


Информационные окна

"""

from tkinter import *

from tkinter.messagebox import *

root = Tk()


root.title('Информационные окна')

#  для обработчика используем анонимную функцию
button_1 = Button(root, text='Info', font=('Ubuntu', 20),
                  command=lambda: showinfo('Showinfo', 'Анонимная функция'))

button_1.configure(bg='green', activebackground='green', fg='white',
                   activeforeground='white')

button_1.grid(row=0, column=0, sticky='EW')

button_2 = Button(root, text='Warning', font=('Ubuntu', 20),
                  command=lambda: showwarning('ShowWarning', 'Предупреждение'))

button_2.configure(bg='blue', activebackground='blue', fg='white',
                   activeforeground='white')


button_2.grid(row=1, column=0, sticky='EW')

button_3 = Button(root, text='Error', font=('Ubuntu', 20),
                  command=lambda: showerror('ShowError', 'Ошибка'))

button_3.configure(bg='red', activebackground='red', fg='white',
                   activeforeground='white')


button_3.grid(row=2, column=0, sticky='EW')


root.mainloop()
