'''
Created on 29 апр. 2018 г.

@author: danny
'''

if __name__ == '__main__':
    while True:
        age = input('Enter your age: ')
        if age.isdecimal():
            print('Good! Next...')
            break
        print('Please, enter a NUMBER for your age! ')

    while True:
        passw = input('Select your password (LETTERS AND NUMBERS only! ')
        if passw.isalnum():
            print('Very good!')
            break

        print('Passwords can only have letters and numbers! ')

