#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

print("Игра в кости")
name = input("Введите свое имя ")
n = input("Введите количество раундов, которое вы хотите сыграть ")
n = int(n)
result = [[], []]
for i in range(0, n):
    print("Ваша очередь,", name, ".Для броска нажмите ввод ")
    input()
    a = random.randint(1, 6)
    result[0].append(a)
    print("Вам выпало ", a)
    a = random.randint(1, 6)
    result[1].append(a)
    print("Бросок компьютера. Ему выпало ", a)
    print("Раунд", i+1, "закончен.")
    input()
print("Для вывода итоговой таблицы нажмите ввод")
input()
resultUser = 0
resultCpu = 0
print(name, "       Компьютер")
for i in range(0, n):
    print(result[0][i], "        ", result[1][i])
    resultUser = resultUser+result[0][i]
    resultCpu = resultCpu+result[1][i]
print()
print(resultUser, "        ", resultCpu)
if resultUser > resultCpu:
    print("Поздравляем,", name, "! Вы победили!")
elif resultCpu == resultUser:
    print("Поздравляем,", name, "! У вас ничья!")
else:
    print("Поздравляем,", name, "! Вы проиграли!")
