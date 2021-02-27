#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Многопоточный парсер с сайта auto.ria.com
'''
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import subprocess
#URL = 'https://auto.ria.com/newauto/marka-jeep'
DOMAIN = 'https://auto.ria.com'
# anti-blocking protection
HEADERS = {'user-agent': 
'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
'accept': '*/*'
}
def get_html(url):
    """
    получает html-данные по заданному url
    """
    resp = requests.get(url, headers=HEADERS, params=None)
    return resp.text

def get_pages_count(html):
    """
    Получаем все номера страниц
    """
    soup = BeautifulSoup(html,'html.parser')
    pagination = soup.find_all('span',class_='mhide')
    if pagination:
        return int(pagination[-1].get_text()) # gets last element of pagination array
    else:
        return 1


def get_all_links(url, max_page):
    """
    Функция получает общий url от машины, и
    максимальное количество страниц с инфо по машине
    returns словарь с правильными многостраничными url-ами
    """
    urls = []
    for page in range(max_page):
        urls.append(url + '?page='+str(page+1))
    return urls

def get_page_data(html):
    """
    Получаем всю инфу о монете по переданной ссылке
    """
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_='proposition_area')
    data = []
    for item in items:
        #print(item)
        uah_price = item.find('span',class_='grey size13')
        if uah_price:
            uah_price = uah_price.get_text(strip=True)
        else:
            uah_price = 'Цена в гривнах не определена'

        data.append({
            'title': item.find('strong').get_text(strip=True), #strip = обрезает лишние пробелы
            'usd_price': item.find('span',class_='green bold size18').get_text(strip=True),
            'uah_price': uah_price,
            'link': DOMAIN + item.find('a').get('href'),
            'fuel': item.find('span', class_='size13').get_text(),
            'city': item.find('svg', class_='svg svg-i16_pin').find_next('strong').get_text(strip=True)

        
            })    
    return data

def write_csv(items):
    """
    Записываем полученные данные в csv-файл
    """
    with open('cars.csv', 'a', newline='') as file:
        writer = csv.writer(file,delimiter=';')
        #writer.writerow(['Марка','Цена в USD','Цена в UAH','Ссылка','Двигатель','Город'])

        for item in items:
            writer.writerow([item['title'],item['usd_price'],item['uah_price'],item['link'],item['fuel'],item['city']])






def main():
    """
    Точка входа в программу
    """
    #сделать замеры времени
    all_links = []
    URL = input('Введите url (наподобие https://auto.ria.com/newauto/marka-acura/) > ')
    html = get_html(URL)
    pages_count = get_pages_count(html)
    start_time = datetime.now()
    all_links = get_all_links(URL, pages_count)
    print(f'Найдено {len(all_links)} страниц(ы).')
    for url in all_links:
        html = get_html(url)
        print('Парсим страницу...')
        data = get_page_data(html)
        write_csv(data)
    end_time = datetime.now()
    print('Затрачено времени ' + str(end_time - start_time))
    subprocess.call(['libreoffice', '--calc', 'cars.csv'])

if __name__ == '__main__':
    main()
