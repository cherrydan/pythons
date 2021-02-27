#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Программа показывает длительность видеороликов в формате
mp4.
@author: Олег Молчанов
"""
import os
from subprocess import Popen, PIPE, STDOUT
from sys import exit
from datetime import timedelta

# доступные нам расширения видеофайлов
VIDEO_EXTENSIONS = ['avi', 'mp4', 'mkv']


def get_videos():
    """
    Получаем имена видеофайлов во всех папках рекурсивно
    """
    videos = []
    # проходка по каталогам, подкаталогам и файлам при помощи
    # модуля os
    for root, subfolders, files in os.walk(os.getcwd()):
        for FILE in files:
            # если в файле допустимое для нас расширение видеоформата
            if FILE.split('.')[-1] in VIDEO_EXTENSIONS:
                # добавляем путь в список
                videos.append(os.path.join(root, FILE))
            else:
                # или покидаем функцию с сообщением
                return print('В папке нет допустимых видеофайлов')
    return videos


def get_ffprobe_output(filename):
    """
    Запускаем программу ffprobe и получает её вывод
    """
    # заменяем пробелы на экранированные пробелы
    # чтобы не мешать команде ffprobe
    filename = filename.replace(' ', r'\ ')
    filename = filename.replace('(', ' ')
    filename = filename.replace(')', ' ')
    # команда для выполнения
    cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(filename)
    # создаем подпроцесс при помощи класса popen
    # shell=False предохраняет нашу программу от иньекций извне
    # также перенаправляем вывод
    popen = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT,
                  universal_newlines=True)
    # получаем данные
    stdout, stderr = popen.communicate()
    return int(float(stdout))


def seconds_to_str(s):
    """
    Конвертирует секунды в ч.м.с
    принимает время в секундах
    """
    return str(timedelta(seconds=s))


def main():
    """
    Точка входа в программу
    """
    videos = get_videos()
    total_duration = 0
    if videos is not None:
        for video in videos:
            duration = get_ffprobe_output(video)
            print('File: ', video.split('/')[-1], ' Duration: ',
                  seconds_to_str(duration))
            total_duration += duration
        print('\nTotal duration: ', seconds_to_str(total_duration))
    else:
        print('Что-то пошло не так...')
        exit(-1)


if __name__ == '__main__':
    main()
