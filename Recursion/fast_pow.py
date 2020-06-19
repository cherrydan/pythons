#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
Рекурсивные алгоритмы.
Возведение в степень (быстрая)
(Тимофей Хирьянов)
"""
def fast_power(a, n):
    """
    fast_power(float a, int n)
    a - число
    n - степень
    """
    if n == 0:
        return 1
    if n % 2 == 1:
        return a*fast_power(a, n-1)
    else:
        return fast_power(a*a, n/2)


def main():
    try:
        a = float(input())
        n = int(input())
        print(a, 'в степени', n, '=', fast_power(a,n))
    except ValueError:
        print('Неправильный ввод числа')


if __name__ == '__main__':
    main()

