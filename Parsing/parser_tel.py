#!/usr/bin/env python
# -*- coding: utf-8 -*-


#module for make csv file
import csv

#module for running LibreOffice Calc
import subprocess

#for time-checking importing module datetime
from datetime import datetime

#module for sleep function
import time

#importing Beautiful Soup library
from bs4 import BeautifulSoup

#importing requests library
import requests


#importing progress-bar drawing library
from progress.bar import IncrementalBar

#importing selenium for lauhching browser
from selenium import webdriver

# base url of cars
URL = 'https://auto.ria.com/newauto/marka-lexus/'

#short url of cars
S_URL = 'https://auto.ria.com'

# anti-blocking protection
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
           'accept': '*/*'}

#filename for csv-file
FILE = 'cars.csv'

# function gets html data via requests library
def get_html(url, params=None):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


# function gets number of pages in our query-url
def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text()) # gets last element of pagination array

    return 1

###SELENIUM
#opens Chrome via chromedriver  with link
#finds 'show phone number' button
#emulates button click
#finds element with phone number and GET its as text
#returns phone number
def get_telephone_number(link):
    #попробуем запустить хром в безголовом режиме
    chrome_options = webdriver.ChromeOptions()
    #запускаем браузер в безголовом режиме
    chrome_options.headless = True#
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)
    button = driver.find_element_by_xpath('//span[@class="show-phone-btn dotted"]')
    button.click()
    #time.sleep(1)
    phone_number = button.find_element_by_xpath('//a[@class="phone unlink bold proven"]').text
    return phone_number



### BEAUTIFUL SOUP
# function fills 'cars' dictionary with data, parsed by Beautiful Soup library
# and with get_telephone_number function
def get_content(html):
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

        title = item.find('strong').get_text(strip=True) #strip = обрезает лишние пробелы
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
        #time.sleep(0.3)
        prog_bar.next()
    prog_bar.finish()    
    return cars

# function saves 'items' to 'path' in csv file        
def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Цена в USD', 'Цена в UAH', 'Ссылка', 
                         'Двигатель', 'Город', 'Телефон'])

        for item in items:
            writer.writerow([item['title'], item['usd_price'], item['uah_price'], 
                             item['link'], item['fuel'], item['city'], item['telephone'],])

# function parse() makes test parsing
def parse():
    url = input('Введите URL (наподобие https://auto.ria.com/newauto/marka-acura)  > ')
    url = url.strip()
    start_time = datetime.now()
    html = get_html(url)
    cars = []
    if html.status_code == 200:
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count +1):
            print(f'Парсинг страницы {page} из {pages_count}')
            cars.extend(get_content(html.text))
        save_file(cars, 'cars.csv')
        print(f'Получено {len(cars)} автомобилей.')
        elapsed_time = datetime.now() - start_time
        elapsed_time = elapsed_time.total_seconds()
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        subprocess.call(['libreoffice','--calc',FILE])
        print(f'Затрачено времени: {hours} ч {minutes} м {seconds} с ')
    else:
        print('Error')


parse()
