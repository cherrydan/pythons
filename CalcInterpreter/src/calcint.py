'''
Created on 8 июл. 2018 г.

@author: danny
'''

str1 = input()

Split = str1.split(' ')

a1 = int(Split[0])
a2 = int(Split[2])
operator = Split[1]


if operator == 'plus':

    print(str(a1 + a2))

elif operator == 'minus':
    print(str(a1 - a2))

elif operator == 'multiply':
    print(str(a1 * a2))

elif operator == 'divide':
    try:
        print(str(int(a1 // a2)))

    except ZeroDivisionError:
        print("None")



