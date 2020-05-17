#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Программа показывает длительность видеороликов в формате
mp4.
@author: Олег Молчанов
"""
import os
from subprocess import *
#доступные нам расширения видеофайлов
VIDEO_EXTENSIONS = ['avi','mp4','mkv']

def get_videos():
    """
    Получаем имена видеофайлов во всех папках рекурсивно
    """
    videos = []
    #проходка по каталогам, подкаталогам и файлам при помощи
    #модуля os
    for root, subfolders, files in os.walk(os.getcwd()):
        for FILE in files:
            #если в файле допустимое для нас расширение видеоформата
            if FILE.split('.')[-1] in VIDEO_EXTENSIONS:
                #добавляем путь в список
                videos.append(os.path.join(root, FILE))
            else:
                #или покидаем функцию с сообщением
                return print('В папке нет допустимых видеофайлов')
    return videos

def get_ffprobe_output(filename):
    """
    Запускаем программу ffprobe и получает её вывод
    """
    #заменяем пробелы на экранированные пробелы, чтобы не мешать команде ffprobe
    filename = filename.replace(' ','\ ')
    #команда для выполнения
    cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(filename)
    #создаем подпроцесс при помощи класса popen
    #shell=False предохраняет нашу программу от иньекций извне, но я пока хз как это сделать
    #также перенаправляем вывод
    popen = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
    #получаем вывод в переменную
    output = popen.stdout.read()
    print(output)

def main():
    """
    Точка входа в программу
    """
    videos = get_videos()
    for video in videos:
        get_ffprobe_output(video)

if __name__ == '__main__':
    main()
