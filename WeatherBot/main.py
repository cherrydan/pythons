#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Вспоминаем библиотеку PyTelegramBotAPI
Бот-погодник, в зависимости от наших координат,
которые передаютя боту.

@author danny
"""
import logging
from telebot import TeleBot
from telebot import types
from config import TOKEN

logging.basicConfig(filename='bot.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',
                    level=logging.INFO)

BOT = TeleBot(TOKEN)

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
