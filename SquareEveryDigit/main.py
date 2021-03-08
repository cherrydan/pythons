#! python3
# -*- coding: utf-8 -*-

def square_every_digit(n):
    """
    n - integer
    squares every digit of number
    """
    arr = []
    str_n = str(n)
    for num in str_n:
        arr.append(str(int(num) ** 2))
    return int(''.join(arr))


print(square_every_digit(9119))
