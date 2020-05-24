#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Уроки асинхронности,
делаем асинхронность на корутинах
(сопрограммах).
Делегирующие генераторы и подгенераторы
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


class BlaBlaException(Exception):
    pass


# @corutine
# вызываемый генератор
def subgen():
    while True:
        try:
            message = yield

        except BlaBlaException:
            print('Kuku!!!')
        else:
            print('...............', message)


@corutine
# вызывающий генератор, принимает вызываемый генератор
def delegator(g):
    """  while True:
        try:
            data = yield
            g.send(data)
        except BlaBlaException as e:
            g.throw(e) """
    yield from g  # эта конструкция заменяет ВЕСЬ приведенный выше код
