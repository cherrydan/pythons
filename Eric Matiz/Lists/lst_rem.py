#! /usr/bin/python3
# -*- coding: utf-8 -*-

print('Удаление эл-та списка при помощи метода remove()')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducatti']

print('Исходный список: ')
print(motorcycles)

print('Удаляем элемент списка по значению "ducatti"')

too_exp = 'ducatti'
motorcycles.remove(too_exp)

print('Список после удаления:')
print(motorcycles)

print(too_exp.title() + ' - мотоцикл этой марки оказался очень дорогим для меня')
