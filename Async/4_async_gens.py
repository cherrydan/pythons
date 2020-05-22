#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Уроки асинхронности,
делаем асинхронность на генераторах
@author: Олег Молчанов

Разбор алгоритма Дэвида Бизли
Concurency from the Ground up live
Довольно тяжелый для понимания способ
"""
import socket
from select import select

tasks = []

to_read = {}
to_write = {}


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
        yield ('read', server_socket,)  # отдаём серверный сокет
        # получаем данные пакетов
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        yield ('read', client_socket,)  # отдаём клиентский сокет
        # смотрим данные
        request = client_socket.recv(1024)  # лимит в байтах

        if not request:
            break
        else:
            response = 'Hello, world!\n'.encode()
            yield ('write', client_socket,)
            client_socket.send(response)
    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])
            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))
            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            reason, sock = next(task)

            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
        except StopIteration:
            print('Done!')  # когда мы отключилисьы


if __name__ == '__main__':
    tasks.append(server())
    event_loop()
