#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

Программа выводит шуточную песенку о пиве при помощи цикла for
'''
from time import sleep
for beer_num in range(99, 0, -1):
    word = ' бутылок'
    if (beer_num >= 11) and (beer_num <= 19):
        word = ' бутылок'
    else:
        if beer_num % 10 == 1:
            word = ' бутылка'
        elif beer_num % 10 in (2, 3, 4):
            word = ' бутылки'
        else:
            word = ' бутылок'
    print(beer_num, word, ' пива на стене,')
    print(beer_num, word, ' пива')
    print('Одну стянули мы,')
    print('Пустив по кругу.')
    if beer_num == 1:
        print('Нет больше пива на стене,')
        print('Нет больше пива!')
    else:
        new_num = beer_num - 1
        if new_num >= 11 and new_num <= 19:
            word = ' бутылок'
        else:
            if new_num % 10 == 1:
                word = ' бутылка'
            elif new_num % 10 in (2, 3, 4):
                word = ' бутылки'
            else:
                word = ' бутылок'
            print(new_num, word, ' пива на стене,')
        print()
