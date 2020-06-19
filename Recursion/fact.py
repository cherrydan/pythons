#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Рекурсивные алгоритмы. Факториал
(Тимофей Хирьянов С)
"""

def factorial(n):
    """
    factorial(int)
    возвращает факториал числа n
    """
    if n == 0:
        return 1
    return factorial(n - 1) * n

def main():
    try:
        n = int(input('-> '))
        if( n <= 20):
            print('Factorial', n, '=', factorial(n))
        else:
            raise ValueError
    except ValueError:
        print('Допустимое значение должно быть не больше 20')


if __name__ == "__main__":
    main()
