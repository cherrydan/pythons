#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
	Этот бот берёт аудио с ютуба и конвертирует его в mp3
	@autor Alex Borsch

'''
from __future__ import unicode_literals
import os
import re
import logging
from unicodedata import normalize

import requests
import youtube_dl
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TOKEN

logging.basicConfig(filename='bot.log',
                    format='%(ascitime)s - %(name)% - %(levelname)s -%(message)s',
                    level=logging.INFO)

def normalize_special_char(txt):
    """
    Функция для преобразования имени файла
    """
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def start(bot, update):
    """
    Реакция на нажатие кнопки старт
    """
def music():
    """
    Функция которая грабит музыку
    """

def main():
    """
    Точка входа в программу - функция main()
    """
    updater = Updater(TOKEN, use_context=True)
    dispatch = updater.dispatcher
    dispatch.add_handler(CommandHandler('start', start))
    dispatch.add_handler(MessageHandler(Filters.text, music))
    updater.start_polling()
    updater.idle()




if __name__ == '__main__':
    main()
