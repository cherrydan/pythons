#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverse_bits(n):
    """
    n - number
    reverse the bits of n
    returns new decimal value of n
    """
    xb = bin(n)
    a_new = []
    for i in reversed(xb):
        if i != 'b':
            a_new.append(i)
        else:
            break
    return int(''.join(a_new),2)

x = int(input('x = '))
print('new value bits reversed = ', reverse_bits(x))            
