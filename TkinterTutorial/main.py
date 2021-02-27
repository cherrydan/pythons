#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Учебник по Tkinter
    https://younglinux.info/tkinter/tkinter.php

    Практическая работа: написать калькулятор
    (с) danny, 2020

    Главный файл, запускающий приложение
"""

from tkinter import *
from calc import *


def main():
    root = Tk()
    calc = Calc(root)
    calc.setFunc('add')
    calc.setFunc('sub')
    calc.setFunc('div')
    calc.setFunc('mul')
    root.mainloop()

if __name__ == '__main__':
    main()
