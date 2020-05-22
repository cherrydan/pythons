#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Уроки асинхронности,
делаем асинхронность на генераторах
@author: Олег Молчанов
"""
import socket


def server():
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
    while True:
        # получаем данные пакетов
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)
        client(client_socket)


def client(client_socket):
    while True:
        # смотрим данные
        request = client_socket.recv(1024)  # лимит в байтах

        if not request:
            break
        else:
            response = 'Hello, world!\n'.encode()
            client_socket.send(response)
    client_socket.close()


if __name___ == '__main__':
    server()
