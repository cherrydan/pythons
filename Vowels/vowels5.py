#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This program counts wowels in word
'''

vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Введите слово латиницей >')

found = {}

# переносим инициализацию в цикл

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, ' was found ', v, 'time(s).')
