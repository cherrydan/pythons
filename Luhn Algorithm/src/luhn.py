'''
Created on 23 июл. 2018 г.

@author: danny

Программа валидирует номер кредитной карты согласно общепринятому алгоритму Луна

'''

import sys
def whose_card(CardStr):

    if(CardStr[0] == '4'):
        print ("Карта системы VISA ")
    elif (CardStr[0] == '5'):
        print ("Карта системы MASTER CARD ")

    elif (CardStr[0] == '2'):
        print ("Карта системы МИР ")

    elif (CardStr[0] == '3'):
        print("Карта системы AMERICAN EXPRESS ")

    elif (CardStr[0] == '9'):
        print("Карта системы ПРОСТIР ")
    else:
        print("Карта неизвестной платёжной системы!!! Выход...")
        sys.exit(0)




def is_odd_card_number(CardStr):
    if (len(CardStr) % 2 == 0):
        return True
    else:
        return False


def validate_card(CardStr):
    list = []
    evenmultlist = []
    odddigits = []
    allsum = 0
    for lett in CardStr:
            list.append(int(lett))

    l_len = int((len(CardStr) / 2))
    if(is_odd_card_number(CardStr)):
        evencounter = 0

        for i in range(0, l_len):
            app = list[evencounter] * 2
            if (app > 9):
                app = app - 9
                evenmultlist.append(app)
            else:
                evenmultlist.append(app)

            evencounter+=2

        oddcounter = 1
        for x in range(0, l_len):
            odddigits.append(list[oddcounter])
            oddcounter+=2

        for y in range(0, l_len):
            allsum += evenmultlist[y] + odddigits[y]

        if(allsum % 10 == 0):
            return True
        else:
            return False

    else:
        print("Ошибка! В номере кредитной карты должно быть 16 цифр!")




card_str = input('Введите номер банковской карты: ')

if(card_str.isdigit() or len(card_str) == 16):
    whose_card(card_str)
    
    if(validate_card(card_str)):
        print('\t * * * Карта № ' + card_str + ' ВАЛИДНА! * * *\t')
    else:
        print('\t - - - Карта № ' + card_str + ' НЕ ВАЛИДНА! - - -\t')
else:
    print('Что-то не так с вводом данных! Допустимый ввод: ЦИФРЫ, количество цифр - 16!')
    sys.exit(0)