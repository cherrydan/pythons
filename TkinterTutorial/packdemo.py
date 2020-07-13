#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

def main():
    root = Tk()

    one = Label(root, text='Один', bg='red', fg='yellow')
    one.pack()
    two = Label(root, text='Два', bg='blue', fg='white')
    two.pack(fill=X)
    three = Label(root, text='Три', bg='green', fg='purple')
    three.pack(side=LEFT, fill=Y)
    root.mainloop()


if __name__ == '__main__':
    main()

