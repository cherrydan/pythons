#-*- coding:utf-8 -*-
#! usr/bin/ python3.5
'''
Created on 1 мая 2018 г.

@author: danny
'''
import sys, pyperclip
PASSWORDS = {'email': 'meksik85',
             'blog':'22Genis$1953',
             'luggage':'125'}

if len(sys.argv) < 2:
    print('Ussage: python3 %.py [account name] copied account name')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' has been copied to clipboard!')
    print(pyperclip.paste())
else:
    print('Account name ' + account + ' is not in a PASSWORDS list!')

