#!/usr/bin/env python
# -*- codnig: utf-8 -*-
"""
Изучаем множества, выясняем состав гласных в слове при
помощи множеств
"""
word = input('Введите слово латиницей >')
vowels = set('aouei')  # создаем множество
i = vowels.intersection(set(word))  # ищем общие гласные в двух множествах
for letter in i:
    print(letter)
