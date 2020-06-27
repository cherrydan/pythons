#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def capitalize(s, ind):
    for i in range(len(s)):
        if i != ind - 1:
            print(s[i], sep='', end='')
        else:
            print(s[i].upper(), sep='', end='')
    print()


def capitalize2(s, ind):
    for i in range(len(s)):
        if i + 1 not in ind:
            print(s[i], sep='', end='')
        else:
            print(s[i].upper(), sep='', end='')
    print()


def main():
    s = input('Строка: ')
    pos = input('Позиция: ')
    if int(pos) > len(s):
        print('Такого индекса не существует!')
        sys.exit()
    capitalize(s, int(pos))
    capitalize2(s, [1, 2, 4])


if __name__ == '__main__':
    main()
