#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Уроки асинхронности
Кооперативная многозадачность в Python,
реализованная на колбеках. Этот способ значительно изящнее,
чем предыдущий.
Асинхронность в один поток
@author: Олег Молчанов
"""
import socket
import selectors

selector = selectors.DefaultSelector()


def server():
    """
    Функция, которая создаёт серверную часть
    """
    server_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)  # AF_INET протокол IPv4
    server_socket.setsockopt(socket.SOL_SOCKET,
                             socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))  # связываем IP и порт
    # слушаем порт
    server_socket.listen()
    # регистрируем серверный сокет в селекторе
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ,
                      data=accept_connection)


def accept_connection(server_socket):
    """
    Подключаемся к клиенту
    """
    # получаем данные пакетов
    client_socket, addr = server_socket.accept()
    print('Connection from: ', addr)
    # регистрируем клиенский сокет
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ,
                      data=send_message)


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
        # снимаем клиенский сокет с регистрации
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    """
    Функция событийный цикл
    """
    while True:
        # получаем данные о событии - источник события и само событие
        events = selector.select()

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
