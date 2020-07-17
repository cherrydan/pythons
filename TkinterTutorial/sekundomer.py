#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    Реализация секундомера на Tkinter

"""

from tkinter import *

from datetime import datetime

temp = 0  # глоб
after_id = ''


def tick():
    global temp, after_id
    # функция after выполняет заданную аргументом функцию,
    # через заданное аргументом время
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label_1.configure(text=str(f_temp))
    temp += 1


def start_sw():
    #  удаляем виджет
    btn_1.grid_forget()
    btn_2.grid(row=1, columnspan=2, sticky='EW')
    tick()


def stop_sw():
    btn_2.grid_forget()
    btn_3.grid(row=1, column=0, sticky='EW')
    btn_4.grid(row=1, column=1, sticky='EW')
    # останавливаем внутренний цикл after
    root.after_cancel(after_id)


def continue_sw():
    btn_3.grid_forget()
    btn_4.grid_forget()
    btn_2.grid(row=1, columnspan=2, sticky='EW')
    tick()


def reset_sw():
    global temp
    temp = 0
    label_1.configure(text='00:00')
    btn_3.grid_forget()
    btn_4.grid_forget()
    btn_1.grid(row=1, columnspan=2, sticky='EW')


root = Tk()

root.title('Stopwatch')

label_1 = Label(root, width=5, font=('Ubuntu', 100), text='00:00')

label_1.grid(row=0, columnspan=2)

#  располагаем кнопки, делаем видимыми в зависимости от состояния секундомера
btn_1 = Button(root, text='Start', font=('Ubuntu', 30), command=start_sw)
btn_2 = Button(root, text='Stop', font=('Ubuntu', 30), command=stop_sw)
btn_3 = Button(root, text='Continue', font=('Ubuntu', 30), command=continue_sw)
btn_4 = Button(root, text='Reset', font=('Ubuntu', 30), command=reset_sw)

btn_1.grid(row=1, columnspan=2, sticky='EW')

root.mainloop()
