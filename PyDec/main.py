#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
def decrypt(file):
    import pyAesCrypt
    print('----------------')
    password = input('Enter password to decrypt: ')
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(str(file), 
                           str(os.path.splitext(file)[0]) + '.dec',
                           password, buffer_size)

    print('File ' + file + ' decrypted to ' +
           str(os.path.splitext(file)[0]) + '.dec')

if __name__ == '__main__':
    file = input('Enter file name: ')
    decrypt(file)



