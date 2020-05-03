#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests

from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-land-rover/'
sURL = 'https://auto.ria.com'

HEADERS = {'user-agent': 
'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
'accept': '*/*'
}

def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r


def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_='proposition_area')
    cars = []

    for item in items:
        #print(item)
        uah_price = item.find('span',class_='grey size13')
        if uah_price:
            uah_price = uah_price.get_text(strip=True)
        else:
            uah_price = 'Цена в гривнах не определена'

        cars.append({
            'title': item.find('strong').get_text(strip=True), #strip = обрезает лишние пробелы
            'price': item.find('span',class_='green bold size18').get_text(strip=True),
            'uah_price': uah_price,
            'link': sURL + item.find('a').get('href'),
            'fuel': item.find('span', class_='size13').get_text(),
            'city': item.find('svg', class_='svg svg-i16_pin').find_next('strong').get_text(strip=True)

        
            })

    return cars

        




def parse():
    html = get_html(URL)
    
    if html.status_code == 200:
        print(get_content(html.text))
    else:
        print('Error')


parse()

