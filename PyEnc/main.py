#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os

def crypt(dir):
    import pyAesCrypt
    print('-----------------')
    password = input('Enter password: ')
    buffer_size = 512 * 1024
    pyAesCrypt.encryptFile(str(dir), str(dir) + '.aes', 
            password, buffer_size)
    print('File ' + str(dir) + ' crypted to ' + str(dir) + '.aes')

if __name__ == '__main__':
    dir = input('Enter filename to encrypt: ')
    crypt(dir)

