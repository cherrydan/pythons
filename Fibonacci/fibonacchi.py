#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Программа выводить ряд чисел Фибоначчи до x-числа
"""
import sys
fib1 = fib2 = 1
N = int(input())
if N < 2:
    sys.exit(0)
print(fib1, end=' ')
print(fib2, end=' ')
for i in range(2, N):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
print()
