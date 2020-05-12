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
                    format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',
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
    update.message.reply_text('Youtube Music Downloader')

def search_youtube(text):
    """
    Функция ищет данные по заданному ключу на Ютубе
    """
    url = 'https://youtube.com'
    #формируем запрос url
    response = requests.get(url + '/results', params={'search_query': text})
    soup = BeautifulSoup(response.content, 'html.parser')
    #забираем теги с Ютуба
    for tag in soup.find_all('a', {'rel': 'spf-prefetch'}):
        title, video_url = tag.text, url + tag['href']
        if 'gogleads' not in video_url:
            return normalize_special_char(title), video_url

def download(title, video_url):
    """
    Функция загружает данные с ютуба
    """
    ydl_opts = {
        'outtmpl': '{}.%(ext)s'.format(title),
        'format': 'bestaudio/best', 
        #указываем параметры сжатия аудио
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    return {
        'audio': open(title + '.mp3', 'rb'),
        'title': title,
        }        


def music(bot, update):
    """
    Функция которая грабит музыку
    """
    title, video_url = search_youtube(update.message.text)
    update.message.reply_text('Starting download ' + title)
    music_dict = download(title, video_url)
    update.message.reply_text('Converting to mp3 ' + title)
    update.message.reply_audio(**music_dict, timeout=9999)
    os.remove(title + '.mp3')

def main():
    """
    Точка входа в программу - функция main()
    """
    updater = Updater(TOKEN)
    dispatch = updater.dispatcher
    dispatch.add_handler(CommandHandler('start', start))
    dispatch.add_handler(MessageHandler(Filters.text, music))
    updater.start_polling()
    updater.idle()




if __name__ == '__main__':
    main()
