'''
Created on 9 июл. 2018 г.

@author: danny

Принимает на вход строку из символов A - F
и вычисляет процент высших баллов из всех оценок

'''
#!usr/bin/python3

counter = 0
totalGrades = 0

sGrades = input()

for word in sGrades:
    if word != ' ':
        totalGrades += 1
        if word != 'A':
            counter = counter
        else:
            counter += 1

cf = 0

try:
    cf = totalGrades / counter
    res = 1 / cf

    print('{0:.2f}'.format(res))

except ZeroDivisionError:
    res = 0.00
    print('{0:.2f}'.format(res))
