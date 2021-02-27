#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Задание 27 ЕГЭ по информатике, демо-вариант 2018 года
@author: Тимофей Хирьянов (С)
применены принципы комбинаторики
Переписано на Питон мной
Задание звучало так: найти все пары чисел, произведение 
которые делятся на 26.
Числа задавать, предварительно взяв у пользователя их количество
"""

k26 = k13 = k2 = k1 = 0
N = int(input('Введите количество чисел: '))
for i in range(N):
    x = int(input())
    if x % 26 == 0:
        k26 += 1
    elif x % 13 == 0:
        k13 += 1
    elif x % 2 == 0:
        k2 += 1
    else:
        k1 += 1

m = k26*(k26-1)/2 + k26*(k1+k2+k13)+k2*k13
print('Подходящих пар {} шт.'.format(m))

