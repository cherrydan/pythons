#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests

from bs4 import BeautifulSoup

import csv

import subprocess

#for time-checking importing module datetime
from datetime import datetime

import time

#importing progress-bar drawing library
from progress.bar import IncrementalBar

# base url of cars
URL = 'https://auto.ria.com/newauto/marka-lexus/'

#short url of cars
sURL = 'https://auto.ria.com'

# anti-blocking protection
HEADERS = {'user-agent': 
'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
'accept': '*/*'
}

#filename for csv-file
FILE = 'cars.csv'

# function gets html data via requests library
def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r


# function gets number of pages in our query-url
def get_pages_count(html):
    soup = BeautifulSoup(html,'html.parser')
    pagination = soup.find_all('span',class_='mhide')
    if pagination:
        return int(pagination[-1].get_text()) # gets last element of pagination array
    else:
        return 1




# function fills 'cars' dictionary with data, parsed by Beautiful Soup library
def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_='proposition_area')
    cars = []
    
    bar = IncrementalBar('',max=len(items))

    for item in items:
        #print(item)
        uah_price = item.find('span',class_='grey size13')
        if uah_price:
            uah_price = uah_price.get_text(strip=True)
        else:
            uah_price = 'Цена в гривнах не определена'

        cars.append({
            'title': item.find('strong').get_text(strip=True), #strip = обрезает лишние пробелы
            'usd_price': item.find('span',class_='green bold size18').get_text(strip=True),
            'uah_price': uah_price,
            'link': sURL + item.find('a').get('href'),
            'fuel': item.find('span', class_='size13').get_text(),
            'city': item.find('svg', class_='svg svg-i16_pin').find_next('strong').get_text(strip=True)

        
            })
        time.sleep(0.3)
        bar.next()

    bar.finish()    
    return cars

# function saves 'items' to 'path' in csv file        
def save_file(items, path):
    with open(path,'w',newline='') as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerow(['Марка','Цена в USD','Цена в UAH','Ссылка','Двигатель','Город'])

        for item in items:
            writer.writerow([item['title'],item['usd_price'],item['uah_price'],item['link'],item['fuel'],item['city']])





# function parse() makes test parsing
def parse():
    URL = input('Введите URL (наподобие https://auto.ria.com/newauto/marka-acura)  > ')
    URL = URL.strip()
    start_time = datetime.now()
    html = get_html(URL)
    cars = []
    if html.status_code == 200:
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы {page} из {pages_count} ')
            html = get_html(URL,params={'page':page})
            cars.extend(get_content(html.text))
        
        save_file(cars, FILE)
        print(f'Получено {len(cars)} автомобилей')
        elapsed_time = datetime.now() - start_time
        elapsed_time = elapsed_time.total_seconds()
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time  % 60)
        print(f'Затрачено времени: {hours} час {minutes} мин {seconds} сек')
        subprocess.call(['libreoffice','--calc', FILE])

    else:
        print('Error')


parse()

