#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Уроки асинхронности
@author: Олег Молчанов
"""
import socket


def run():
    """
    Устанавливаем соединение с сервером
    """
    server_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)  # AF_INET протокол IPv4
    server_socket.setsockopt(socket.SOL_SOCKET,
                             socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))  # связываем IP и порт
    # слушаем порт
    server_socket.listen()
    # создаём бесконечный цикл слушания пакетов
    while True:
        print('Before accept')
        # получаем данные пакетов
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)
        while True:
            print('Before .recv()')
            # смотрим данные
            request = client_socket.recv(1024)  # лимит в байтах

            if not request:
                break
            else:
                response = 'Hello, world!\n'.encode()
                client_socket.send(response)
        print('Outside inner while loop')
        client_socket.close()


if __name__ == '__main__':
    run()
