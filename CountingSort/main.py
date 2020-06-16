#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Сортировка подсчётом
@author: Тимофей Хирьянов
Переписано на Питон мной
"""
def print_list(arr, n):
    """
    print_list(list, int)
    печатает массив заданного размера
    """
    for i in range(n):
        print(arr[i],' ',end='')
    print()

def main():
    counters = [0]*10
    A = list()
    while(True):
        x = int(input('Введите числа (терминатор 10) -> '))
        if x == 10: break;
        if x < 0 or x > 9: continue;
        counters[x] += 1

    for x in range(len(counters)):
        for i in range(counters[x]):
            A.append(x)
    print_list(A, len(A))

if __name__ == "__main__":
    main()
