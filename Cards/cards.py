#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Пример из книги Лучано Ромальо,
    демонастрирующий создание колоды из 52-х карт
    @author Luciano Romalho
"""
import collections

Card = collections.namedtuple('Card', ['rank', 'suit']) #каждая карта имеет стоимость и масть
#класс - колода карт
class FrenchDeck:
    """
    Класс FrenchDeck - представляет колоду карт
    """
    #карты от 2 до 10, плюс Валет, Дама, Король, Туз
    ranks = [str(n) for n in range(2, 11)] + list('ВДКТ')
    #масти = список разделённый пробелом
    suits = 'пики бубны трефы червы'.split()

    def __init__(self):
        """
        Конструктор класса, встроенный метод
        """
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        """
        Встроенный метод, который отаёт нам размер колоды
        """
        return len(self._cards)

    def __getitem__(self, position):
        """
        Встроенный метод, возвращает нам карту из колоды
        """
        return self._cards[position]
