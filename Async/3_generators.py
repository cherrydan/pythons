#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Уроки асинхронности
Кооперативная многозадачность в Python,
на генераторах и событийном цикле Round Robin.
@author: Олег Молчанов
"""
from time import time


def gen_filename():
    """
    генератор это функция, а не последовательность данных
    генератор не столько генерирует что-либо, сколько позволяет
    из функции-генератора передать управление в то место, где
    была вызывана функция next(), которая запускает функцию-генератор
    снова.
    """
    while True:
        pattern = 'file-{}.jpg'
        t = int(time() * 1000)
        yield pattern.format(str(t))  # yield это как-бы return


def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


# round-Robin
g1 = gen1('danil')
g2 = gen2(5)

tasks = [g1, g2]  # создаём очередь

while tasks:
    task = tasks.pop(0)  # вытаскиваем из очереди первое задание
    try:
        i = next(task)  # выполняем задание
        print(i)
        tasks.append(task)  # прокручиваем задание

    except StopIteration:
        pass
