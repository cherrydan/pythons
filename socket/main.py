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

URLS = {
    '/': 'hello index',
    '/blog': 'hello blog'
}


def parse_request(request):
    """
    Распарсиваем запрос
    """
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return (method, url)


def generate_headers(method, url):
    """
    Генерирует заголовки, без которых не может хром
    """
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)

    if url not in URLS:
        return ('HTTP/1.1 404 Page not found\n\n', 404)

    return ('HTTP/1.1 200 OK\n\n', 200)


def generate_response(request):
    """
    Получаем ответ по нашему запросу
    """
    method, url = parse_request(request)  # вызываем фцию распарсивающую запрос
    headers, code = generate_headers(method, url)
    return (headers + 'hello, world').encode()


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
        print(request)
        print()
        print(addr)

        response = generate_response(request.decode('utf-8'))

        # отправляем в ответ Hello, world
        client_socket.sendall(response)
        # обязательно надо закрывать соединение
        client_socket.close()


if __name__ == '__main__':
    run()
