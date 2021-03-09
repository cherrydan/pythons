#! /usr/bin/python3
# -*- coding: utf-8 -*-

guests = ['Герман', 'Алёна', 'Саша', 'Катерина', 'Данил', 'Коля']

print('Список гостей: ')

no_entry = 'Катерина'

guests.remove(no_entry)
guests.insert(3, 'Маша')
guests.insert(0, 'Вова')
guests.insert(4, 'Яна')
guests.append('Андрей')
print(guests)

num_of_guests = len(guests)

print('Не получится разместить такое количество гостей: ' + 
        str(num_of_guests))

print('\nРасместить можно будет только двоих гостей!\n')

i = num_of_guests - 1
while i >= 2:
    print(guests[i] + ', к сожалению, придётся отозвать приглашение ')
    guests.pop(i)
    i-=1


print()
for guest in guests:
    print(guest + ', наше приглашение на обед остаётся в силе')

print('\nПридётся отменить весь обед - удаляем последних двух гостей из списка')

for i in range(0, len(guests)):
    del guests[i - 1]

print('Убеждаемся, что список пуст')
print(guests)
