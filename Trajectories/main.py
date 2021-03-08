#!/usr/bin/env python
# -*- coding: utf-8 -*-
def num_of_traje(n):
    """
    num_of_traje(int)
    """
    K = [0] * (n + 1)
    K[0] = 0
    K[1] = 1
    for i in range(2, len(K)):
        K[i] = K[i - 1] + K[i - 2]
    return K[n]


def main():
    finish = int(input('->'))
    print('Кузнечик имеет {} траектории от 1 до {}'.format(num_of_traje(finish), finish))


if __name__ == '__main__':
    main()
