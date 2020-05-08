#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Для сравнения - однопоточная версия демо
'''
from datetime import datetime
import requests
from bs4 import BeautifulSoup
#список с урлами, в случае с парсером это должны быть урлы
#всех страниц с машинами, надо как-то их получить
URLS = ['https://auto.ria.com/newauto/marka-acura',
        'https://auto.ria.com/newauto/marka-opel',
        'https://auto.ria.com/newauto/marka-skoda/',
        'https://auto.ria.com/newauto/marka-renault/',
        'https://auto.ria.com/newauto/marka-bmw/',
        'https://auto.ria.com/newauto/marka-audi/',
        'https://auto.ria.com/newauto/marka-volvo/',
        'https://auto.ria.com/newauto/marka-suzuki/',
        'https://auto.ria.com/newauto/marka-honda/',
        'https://auto.ria.com/newauto/marka-hyundai/']


HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
           'accept': '*/*'}


def get_pages_count(html):
    """
    Получаем общее количество страниц по марке автомобиля
    """
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text()) # gets last element of pagination array
    return 1


def do_work(url, params=None):
    """
    Рабочая функция
    """
    html = requests.get(url, headers=HEADERS, params=params)
    if html.status_code == 200:
        pages_count = get_pages_count(html.text)
        print(f'Url {url} Страниц {pages_count}')
    else:
        print('Error')

START_TIME = datetime.now()
# Make the Pool of workers
for i in range(0, len(URLS)):
    do_work(URLS[i])
ELAPSED_TIME = datetime.now() - START_TIME
#elapsed_time = ELAPSED_TIME.total_seconds()
#HOURS = int(elapsed_time // 3600)
#MINUTES = int((elapsed_time % 3600) // 60)
#SECONDS = int(elapsed_time % 60)
print(f'Затрачено времени: {ELAPSED_TIME} с.')
