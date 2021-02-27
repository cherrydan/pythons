#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Демонстрация теоремы Эйлера
@author: danny
"""
def eiler(v, r, g):
    """
    eiler(int, int, int)
    returns: boolean
    v - вершины, r - ребра, g - грани
    Возвращает true, если многогранник соответствует
    эйлеровой характеристике, иначе false
    """
    if v - r + g == 2:
        return True
    else:
        return False

def main():
    A = [0,0,0]
    A[0] = int(input('Вершины -> '))
    A[1] = int(input('Ребра -> '))
    A[2] = int(input('Грани -> '))
    if(eiler(A[0], A[1], A[2])):
        print('Сответствует эйлеровой характеристике')
    else:
        print('Не соответствует эйлеровой характеристике')

if __name__ == "__main__":
    main()
