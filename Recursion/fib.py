#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Рекурсивные алгоритмы
Числа Фибоначчи.
(Тимофей Хирьянов)
"""
def fib(n):
    """
    fib(n)
    возвращает n-тое число из ряда Фибоначчи
    """
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def main():
    n = int(input())
    print('fib({}) = {}'.format(n,fib(n)))



if __name__ == '__main__':
    main()
