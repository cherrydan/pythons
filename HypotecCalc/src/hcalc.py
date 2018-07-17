'''
Created on 25 мая 2018 г.

"Рыба" ипотечного калькулятора

Вывод при помощи библиотеки PrettyTable

@author: danny
'''
#-*- coding:utf-8 -*-
#! python3

from prettytable import PrettyTable

def h_calc(ps, sk, m):

    piece_ps = float(ps) / (100 * 12)

    k = piece_ps * (1 + piece_ps) ** m /((1 + piece_ps) ** m - 1)

    res = k * sk

    return res

try:

    Ps = input("Введите процентную ставку: ")

    Sk = int(input("Введите сумму кредита: "))

    M = int(input("Введите кол-во месяцев: "))

    Res = h_calc(Ps, Sk, M)

    print("\n\tВы взяли КРЕДИТ на сумму " + str(Sk) + " руб. под " + str(Ps) + "%" + " на " + str(M) + " месяцев.\n\n")

    table = PrettyTable(['Месяц','Платёж'])

    for i in range(1, M+1):
        table.add_row([i, "%.2f" % Res])


    print(table)

    extra_pay = (Res * M) - Sk

    print('\n\n\t Переплата по Вашему кредиту составляет: ' + "%.2f" %extra_pay + ' рублей')

except ZeroDivisionError:
    print("\n\nК сожалению, процент по кредиту не может быть равен 0")

except ValueError:
    print('Ошибка в формате ввода данных!')