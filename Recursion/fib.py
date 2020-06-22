#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Рекурсивные алгоритмы
Числа Фибоначчи.
(Тимофей Хирьянов)
Динамическое программирование сверху и снизу
"""
cache =[0]*50
# динамическое программирование сверху
def fib(n):
    """
    fib(int)
    возвращает n-тое число из ряда Фибоначчи
    Использована рекурсия с кешем
    """
    if n <= 1:
        return n
    if cache[n] == 0:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]


#динамическое программирование снизу
def fib_dynamic(n):
    """
    fib_dynamic(int)
    возвращает n-тое число Фибоначчи
    Не использует рекурсию
    """
    Fib = [0] * (n + 1)
    Fib[0] = 0
    Fib[1] = 1
    for i in range(2, len(Fib)):
        Fib[i] = Fib[i - 1] + Fib[i - 2]
    return Fib[n]

def main():
    for n in range(1,50):
        print('fib({}) = {}'.format(n,fib_dynamic(n)))



if __name__ == '__main__':
    main()
