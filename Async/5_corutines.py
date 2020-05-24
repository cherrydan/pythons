#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Уроки асинхронности,
делаем асинхронность на корутинах
(сопрограммах)
@author: Олег Молчанов
"""

"""
Создаём функцию-декоратор для автоматической
инициализации корутины
"""


def corutine(func):
    """
    Получает функцию-генератор
    """
    def inner(*args, **kwargs):
        """
        Внутренняя функция, которая получает аргументы,
        именованные аргументы, и делает инициализацию
        """
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


@corutine
def average():
    count = 0
    sum = 0
    average = None
    while True:
        try:
            x = yield average

        except StopIteration:
            print('Done')
            break
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)
    return average
