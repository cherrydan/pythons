#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This program displays wowels in word
'''
VOWELS = ['a', 'o', 'u', 'i', 'e']
FOUND = []
WORD = input('Введите слово латиницей >')
for letter in WORD:
    if letter in VOWELS:
        if letter not in FOUND:
            FOUND.append(letter)
for vowel in FOUND:
    print(vowel)
