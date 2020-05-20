#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Уроки асинхронности
Кооперативная многозадачность в Python,
при помощи событийного цикла
Асинхронность в один поток
@author: Олег Молчанов
"""
import socket
from select import select

# список с объектами для мониторинга
to_monitor = []

server_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)  # AF_INET протокол IPv4
server_socket.setsockopt(socket.SOL_SOCKET,
                         socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))  # связываем IP и порт
# слушаем порт
server_socket.listen()


def accept_connection(server_socket):
    """
    Подключаемся к клиенту
    """
    # получаем данные пакетов
    client_socket, addr = server_socket.accept()
    print('Connection from: ', addr)
    to_monitor.append(client_socket)


def send_message(client_socket):
    """
    Посылаем ответ от клиента
    """

    # смотрим данные
    request = client_socket.recv(1024)  # лимит в байтах

    if request:
        response = 'Hello, world!\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    """
    Функция событийный цикл
    """
    while True:
        # select - read, write, errors
        ready_to_read, _, _ = select(to_monitor, [], [])
        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
