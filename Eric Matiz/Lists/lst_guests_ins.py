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
print('\nМы решили позвать БОЛЬШЕ гостей!')
guests.insert(0, 'Вова')
guests.insert(4, 'Яна')
guests.append('Андрей')
print('\n\nСписок гостей расчитанных на новый большой стол:')
print(guests, '\n')
print(guests[0] + ' приглашается на обед 02.06.2021 в 19.00')
print(guests[1] + ' приглашается на обед 02.06.2021 в 19.00')
print(guests[2] + ' приглашается на обед 02.06.2021 в 19.00')
print(guests[3] + ' приглашается на обед 02.06.2021 в 19.00')
print(guests[4] + ' приглашается на обед 02.06.2021 в 19.00')
print(guests[5] + ' приглашается на обед 02.06.2021 в 19.00')
print(guests[6] + ' приглашается на обед 02.06.2021 в 19.00')
print(guests[7] + ' приглашается на обед 02.06.2021 в 19.00')
print(guests[8] + ' приглашается на обед 02.06.2021 в 19.00')
