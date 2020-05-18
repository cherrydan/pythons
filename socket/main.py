#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Этот скрипт показывает как работают фреймворки типа
    Django и Flask на низком уровне
    @author: Олег Молчанов

    Как всё устроено. Есть три протокола http, tcp и ip

    Самый нижний по уровню абстракции это IP-протокол, дающий нам IP-адрес
    Следующим идет TCP-протокол, дающий нам Port
    Пара IP-адрес и порт называется сокет
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
        # получаем данные пакетов
        client_socket, addr = server_socket.accept()
        # смотрим данные
        request = client_socket.recv(1024)  # лимит в байтах
        print(request.decode('utf-8'))
        print()
        print(addr)
        # отправляем в ответ Hello, world
        client_socket.sendall('Hello, world!'.encode())
        # обязательно надо закрывать соединение
        client_socket.close()


if __name__ == '__main__':
    run()
