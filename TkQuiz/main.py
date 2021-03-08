# -*- coding: utf-8 -*-
from tkinter import *

from tkinter import messagebox

root = Tk()

root.title('Викторина')

root.geometry('300x300')


def que_one():
    question = Label(root, text='Висит груша, нельзя скушать :)')
    answer = Entry()
    btn = Button(root, text='Ответить!', command=lambda: game_1(que_two))
    question.grid(row=0)
    answer.grid(row=1)
    btn.grid(row=2)

    def game_1(fn):
        if answer.get().lower() == 'лампочка':
            fn()
        else:
            messagebox.showerror('Ошибка!', 'попробуй еще раз!!')


def que_two():
    question_2 = Label(root, text='Зимой и летом - одним цветом :)')
    answer_2 = Entry()
    btn_2 = Button(root, text='Ответить!', command=lambda: game_2(que_two))
    question_2.grid()
    answer_2.grid()
    btn_2.grid()

    def game_2(fn):
        if answer_2.get().lower() == 'ёлка':
            messagebox.showinfo('Победа!', 'Два верных ответа, ты молодец!')
        else:
            messagebox.showerror('Ошибка!', 'попробуй еще раз!!')



if __name__ == '__main__':
    que_one()
    root.mainloop()
