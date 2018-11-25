'''
Created on 22 июл. 2018 г.

@author: danny

Программа берет на вход строку, содержащую 13-значный EAN-овский штрих код, и проверяет его на валидность по спец алгоритму

'''

def validate_EAN(Estr):
    list = []

    l_len = int((len(Estr) - 1) / 2)

    for lett in Estr:
        list.append(int(lett))


    oddsum = 0
    oddmult = 0
    oddcounter = 1
    for i in range(0, l_len):
        oddsum += list[oddcounter]
        oddcounter+=2
    oddmult = oddsum * 3

    evensum = 0
    evencounter = 0

    for i in range(0,l_len):
        evensum += list[evencounter]
        evencounter+=2

    bothsum = oddmult + evensum

    print(oddsum)
    print(oddmult)
    print(bothsum)

    checksum = 10 - (bothsum % 10)

    if list[12] != checksum:
        return False
    else:
        return True




EANStr = input('Введите EAN-штрих код (13 цифр) ->')

if (len(EANStr) != 13 or (not(EANStr.isdigit()))):
    print('Ввод неверный! Введите ТОЛЬКО ЦИФРЫ в количестве 13!')
else:
    print('Ввод принят...')
    if(validate_EAN(EANStr)):
        print('Товар со Штрих-код ' + EANStr + ' легален!')
    else:
        print('Товар со Штрих-код ' + EANStr + ' НЕЛЕГАЛЕН!')
