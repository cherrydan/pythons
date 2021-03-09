#! /usr/bin/python3
# -*- coding: utf-8 -*-

guests = ['Герман', 'Алёна', 'Саша', 'Катерина', 'Данил', 'Коля']

print('Список гостей: ')
print(guests)

no_entry = 'Катерина'

guests.remove(no_entry)
print(no_entry + ' прийти не сможет')
guests.insert(3, 'Маша')
print('Новый список гостей:')
print(guests)


