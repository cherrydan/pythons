#! /usr/bin/python3
# -*- coding: utf-8 -*-

print('Удаление элемента из списка pop(index)')

motorcycles = ['honda', 'yamaha', 'suzuki']
print('Исходный список ')
print(motorcycles)
print('Удаляем элемент с индексом 0')
first_owned = motorcycles.pop(0) # удаляем первый элемент
# используем его
print('Первый мотоцикл, которым я владел был марки ' + first_owned)
print('\nСписок после удаления:')
print(motorcycles)
