# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('Викторина')

root.geometry('300x300')


def que_one():
    question = Label(root, text='Висит груша, нельзя скушать :)')
    answer = Entry()
    btn = Button(root, text='Ответить')
    question.grid(row=0)
    answer.grid(row=1)
    btn.grid(row=2)


if __name__ == '__main__':
    que_one()
    root.mainloop()
