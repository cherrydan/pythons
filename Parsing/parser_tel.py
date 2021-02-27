#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Parser for site auto.ria.com, new auto
title, usd_price, uah_price, link, fuel, telephone
"""

# module for make csv file
import csv

# module for running LibreOffice Calc
import subprocess

# for time-checking importing module datetime
from datetime import datetime

# importing Beautiful Soup library
from bs4 import BeautifulSoup

# importing requests library
import requests

# importing progress-bar drawing library
from progress.bar import IncrementalBar

# importing selenium for lauhching browser
from selenium import webdriver

# base url of cars
URL = 'https://auto.ria.com/newauto/marka-lexus/'

# short url of cars
S_URL = 'https://auto.ria.com'

# anti-blocking protection
HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'accept': '*/*'}

# filename for csv-file
FILE = 'cars.csv'


def get_html(url, params=None):
    """
    get_html(url, params=None) returns a request-obj giving url and params
    """
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_pages_count(html):
    """
    Use BEAUTIFUL SOUP
    get_pages_count(html) returns number of pages with car information
    needs html-text data
    """
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text())  # gets last element of pagination array
    return 1


def get_telephone_number(link):
    """
    Use SELENIUM automation
    get_telephone_number needs link to one page with detailed car information
    runs Chome with chromedriver (needs to be in system), then find button with telephone number
    clicks on it, and grab the telefone number as text
    returns text-object
    """
    # попробуем запустить хром в безголовом режиме
    chrome_options = webdriver.ChromeOptions()
    # запускаем браузер в безголовом режиме
    chrome_options.headless = True  #
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)
    button = driver.find_element_by_xpath('//span[@class="show-phone-btn dotted"]')
    button.click()
    # time.sleep(1)
    phone_number = button.find_element_by_xpath('//a[@class="phone unlink bold proven"]').text
    return phone_number


def get_content(html):
    """
    Use Beautiful soup again
    get_content(html) gets all content inc. telephone number
    return dictionary with all data
    """
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='proposition_area')
    cars = []
    prog_bar = IncrementalBar('', max=len(items))
    for item in items:
        uah_price = item.find('span', class_='grey size13')
        if uah_price:
            uah_price = uah_price.get_text(strip=True)
        else:
            uah_price = 'Цена в гривнах не определена'

        title = item.find('strong').get_text(strip=True)  # strip = обрезает лишние пробелы
        usd_price = item.find('span', class_='green bold size18').get_text(strip=True)
        link = S_URL + item.find('a').get('href')
        fuel = item.find('span', class_='size13').get_text()
        city = item.find('svg', class_='svg svg-i16_pin').find_next('strong').get_text(strip=True)
        tel_number = get_telephone_number(link)
        if tel_number:
            cars.append({
                'title': title,
                'usd_price': usd_price,
                'uah_price': uah_price,
                'link': link,
                'fuel': fuel,
                'city': city,
                'telephone': tel_number})

        else:
            cars.append({
                'title': title,
                'usd_price': usd_price,
                'uah_price': uah_price,
                'link': link,
                'fuel': fuel,
                'city': city,
                'telephone': 'Телефон доступен в рабочие часы'})
        prog_bar.next()
    prog_bar.finish()
    return cars


def save_file(items, path):
    """
    save_file save all data from dictionary to csv-file format
    """
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Цена в USD', 'Цена в UAH', 'Ссылка',
                         'Двигатель', 'Город', 'Телефон'])

        for item in items:
            writer.writerow([item['title'], item['usd_price'], item['uah_price'],
                             item['link'], item['fuel'], item['city'], item['telephone'], ])


def parse():
    """
    parse() is main function analog, doing all
    """
    url = input('Введите URL (наподобие https://auto.ria.com/newauto/marka-acura)  > ')
    url = url.strip()
    start_time = datetime.now()
    html = get_html(url)
    cars = []
    if html.status_code == 200:
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы {page} из {pages_count}')
            cars.extend(get_content(html.text))
        save_file(cars, 'cars.csv')
        print(f'Получено {len(cars)} автомобилей.')
        elapsed_time = datetime.now() - start_time
        elapsed_time = elapsed_time.total_seconds()
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        print(f'Затрачено времени: {hours} ч {minutes} м {seconds} с ')
        subprocess.call(['libreoffice', '--calc', FILE])
    else:
        print('Error')


parse()
