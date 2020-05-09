#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

Parser for site auto.ria.com, new auto
multiprocessing version
'''
import csv
from datetime import datetime
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from progress.bar import IncrementalBar
DOMAIN = 'https://auto.ria.com'
def get_html(url):
    """
    Функция получает html данные по заданному url
    returns html-данные
    """
    response = requests.get(url)
    return response.text

def get_all_page_urls(url, max_page):
    """
    Функция получает общий url от машины, и
    максимальное количество страниц с инфо по машине
    returns словарь с правильными многостраничными url-ами
    """
    urls = []
    for page in range(max_page):
    	urls.append(url + '?page='+str(page+1))
    return urls

def get_pages_count(html):
    """
    Use BEAUTIFUL SOUP
    get_pages_count(html) returns number of pages with car information
    needs html-text data
    """
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text()) # gets last element of pagination array
    return 1

def get_telephone_number(link):
    """
    Use SELENIUM automation
    get_telephone_number needs link to one page with detailed car information
    runs Chome with chromedriver (needs to be in system), then find button with telephone number
    clicks on it, and grab the telefone number as text
    returns text-object
    """
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

def get_page_data(html):
	"""
	Функция получает html-данные со страницы
	returns все нужные нам данные
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

		title = item.find('strong').get_text(strip=True) #strip = обрезает лишние пробелы
		usd_price = item.find('span', class_='green bold size18').get_text(strip=True)
		link = DOMAIN + item.find('a').get('href')
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

def write_csv(items):
	"""
	Функция принимает словарь с данными, пишет в дефолтный файл cars.csv
	"""
	with open('cars.csv', 'w', newline='') as file:
		writer = csv.writer(file, delimiter=';')
		writer.writerow(['Марка', 'Цена в USD', 'Цена в UAH', 'Ссылка',
                         'Двигатель', 'Город', 'Телефон'])
		for item in items:
			writer.writerow([item['title'], item['usd_price'], item['uah_price'],
                                         item['link'], item['fuel'], item['city'], item['telephone'],])

def main():
	"""
	Main-функция точка входа в программу
	"""
	url = input('Введите url (наподобие https://auto.ria.com/newauto/marka-jeep/) >')
	url = url.strip()
	start_time = datetime.now()
	all_urls = []
	data = []
	pages_count = get_pages_count(get_html(url))
	all_urls = get_all_page_urls(url, pages_count)
	#вывести что то типа "Парсинг страницы X из Y"
	#сделать замеры времени выполнения
	counter = 1
	for url in all_urls:
		html = get_html(url)
		print(f'Обработка страницы {counter} из {pages_count}')
		counter+=1
		data.extend(get_page_data(html))
	print(f'Получено данных о {len(data)} автомобилей')
	write_csv(data)
	elapsed_time = datetime.now() - start_time
	elapsed_time = elapsed_time.total_seconds()
	hours = int(elapsed_time // 3600)
	minutes = int((elapsed_time % 3600) // 60)
	seconds = int(elapsed_time % 60)
	print(f'Затрачено времени: {hours} ч {minutes} м {seconds} с ')	
#записать данные в csv


if __name__ == '__main__':
	main()
