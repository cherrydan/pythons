#!/usr/bin/python3
# -*- coding: utf-8 -*-

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducatti']

print('Исходный список')

print(motorcycles)

print('Удаляем последний эл-т списка при помощи pop()')
deleted = motorcycles.pop()

print('Удалённый элемент можно использовать')
print(deleted)

print('Список, после удаления')
print(motorcycles)
