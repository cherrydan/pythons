#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 27 апр. 2018 г.

@author: danny
'''
if __name__ == '__main__':
    #вложенный словарь
    ALL_GUESTS = {'Alice':{'apples':5, 'pretzels':12},
                  'Bob':{'ham sandwiches':3, 'apples':2, 'vodka':1},
                  'Carol':{'cups':3, 'apple pies':1},
                  'Nicky':{'juice':4}}


    def total_brought(guests, item):
        """
            Функция подсчитывает, сколько всего продуктов должны купить участники пикника
        """
        num_brought = 0 #счетчик товаров
        for key, val in guests.items():
            num_brought = num_brought + val.get(item, 0)
        return num_brought

    print('Number of things being brought: ')
    print(' -Apples         \t' + str(total_brought(ALL_GUESTS, 'apples')))
    print(' -Cups           \t' + str(total_brought(ALL_GUESTS, 'cups')))
    print(' -Cakes          \t' + str(total_brought(ALL_GUESTS, 'cakes')))
    print(' -Ham Sandwiches \t' + str(total_brought(ALL_GUESTS, 'ham sandwiches')))
    print(' -Apple Pies     \t' + str(total_brought(ALL_GUESTS, 'apple pies')))
    print(' -Pretzels       \t' + str(total_brought(ALL_GUESTS, 'pretzels')))
    print(' -Vodka          \t' + str(total_brought(ALL_GUESTS, 'vodka')))
    print(' -Juice          \t' + str(total_brought(ALL_GUESTS, 'juice')))
