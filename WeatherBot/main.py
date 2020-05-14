#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Вспоминаем библиотеку PyTelegramBotAPI
Бот-погодник, в зависимости от наших координат,
которые передаютя боту.

На vps поменять #/usr/bin/python3

@author danny
"""
import logging
from telebot import TeleBot
from telebot import types
from config import TOKEN, API_KEY

logging.basicConfig(filename='bot.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',
                    level=logging.INFO)

BOT = TeleBot(TOKEN)

def get_weather(lat, lon):
    """
    Функция которая по переданной локации получает погоду с сайта
    openweather.com
    1. Формируем url запроса и тестируем его пока в браузере
    2. Если всё пучком, то, делаем get-запрос по этому url
    3. Смотрим, что он нам там отдал в текстовом формате (по идее должен быть json)
    """
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    url = weather_url + '?lat=' + '{' + str(lat) + '}'
    url += '&lon=' + '{' + str(lon) + '}'
    url += '&appid=' + '{' + API_KEY + '}'
    return url



@BOT.message_handler(content_types=['location'])
def location(message):
    """
    Обрабатываем полученую локацию
    """
    if message.location is not None:
        text = get_weather(message.location.latitude, message.location.longitude)
        BOT.send_message(message.chat.id, text)



@BOT.message_handler(commands=["geo"])
def geophone(message):
    """
    Пробуем передать боту местоположение
    """
    text = 'Поделись местоположением, жалкий человечишка!'
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    BOT.send_message(message.chat.id, text, reply_markup=keyboard)


@BOT.message_handler(commands=['start'])
def start(message):
    """
    Приветствуем пользователя при старте
    """
    text = 'Я - бот-погодник!\n'
    text += 'Я подскажу, нужен ли тебе сегодня зонтик.'
    BOT.send_message(message.chat.id, text)


if __name__ == '__main__':
    BOT.polling(True)
