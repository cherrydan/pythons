#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    Работа с упаковщиком pack
  (c) https://www.youtube.com/watch?v=mm-J9pYBcQ0&list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar&index=2

"""

from tkinter import *


def main():
    root = Tk()

    one = Label(root, text='Один', bg='red', fg='yellow')
    one.pack()
    two = Label(root, text='Два', bg='blue', fg='white')
    two.pack(fill=X)  # при растягивании окна, будет заполняться по оси x
    three = Label(root, text='Три', bg='green', fg='purple')
    three.pack(side=LEFT, fill=Y)  # при растягивании окна будет заполняться по оси y
    root.mainloop()


if __name__ == '__main__':
    main()
