#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Программа печатает:
фразу Marvin Android Paradoid
используя срезы
"""
PARANOID_ANDROID = 'Marvin, The Paradoid Android'
LETTERS = list(PARANOID_ANDROID)

for char in LETTERS[:6]:  # с начала строки
    print('\t', char)
print()

for char in LETTERS[8:11]:  # срез
    print('\t' * 2, char)
print()

for char in LETTERS[-7:]:  # с конца строки
    print('\t' * 3, char)
print()

for char in LETTERS[12:20]:  # срез
    print('\t' * 4, char)
