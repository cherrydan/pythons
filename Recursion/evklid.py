#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Рекурсивные алгоритмы
(Тимофей Хирьянов С)
Алгоритм Евклида
Переписано на Питон мной
"""

def gcd(a, b):
    """
    greater common divider (Наибольший общий делитель)
    gcd(int, int)
    """
    if b == 0:
        return a 
    else:
        return gcd(b, a % b)


def main():
    a = int(input())
    b = int(input())
    print('НОД', a, b, '=', gcd(a,b))


if __name__ == '__main__':
    main()
