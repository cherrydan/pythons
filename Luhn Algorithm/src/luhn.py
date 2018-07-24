'''
Created on 23 июл. 2018 г.

@author: danny

Программа валидирует номер кредитной карты согласно общепринятому алгоритму Луна
'''

def whose_card(CardStr):

    if(CardStr[0] == '4'):
        return "Карта системы VISA "
    elif (CardStr[0] == '5'):
        return "Карта системы MASTER CARD "

    elif (CardStr[0] == '2'):
        return "Карта системы МИР "

    elif (CardStr[0] == '3'):
        return "Карта системы AMERICAN EXPRESS "

    elif (CardStr[0] == '9'):
        return "Карта системы ПРОСТIР "
    else:
        return "Карта неизвестной платежной системы, или ошибка в вводе номера карты"



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
    print(whose_card(card_str))
    if(validate_card(card_str)):
        print("Карта № " + card_str  + " валидна!")
    else:
        print("Карта № " + card_str  + " НЕ валидна!")
        
