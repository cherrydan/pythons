#!/usr/bin/env python
# -*- coding: utf-8 -*-


def namelist(names):
    """
    returns string formatted from namelist
    """
    x = len(names)
    if x == 0:
        return ''
    if x == 1:
        return names[0]['name']
    if x == 2:
        for i in range(len(names)):
            return names[i]['name'] + ' & ' + names[i + 1]['name']
    if x == 3:
        return names[0]['name'] + ', ' + names[1]['name'] + ' & ' + names[2]['name']
    if x >= 4:
        text = ''
        i = 0
        while(i != (x - 2)):
            text += names[i]['name'] + ', '
            i += 1
        text += names[-2]['name'] + ' & ' + names[-1]['name']
        return text


def main():
    names = []
    S = ' '
    while(S != ''):
        S = input('Имя? ').strip()
        if(S == ''):
            break
        names.append({'name': S})

    print(namelist(names))


if __name__ == '__main__':
    main()
