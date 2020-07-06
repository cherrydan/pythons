#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import random
from config import *

"""
    Учебник по Pygame
    c сайта https://pythonru.com/uroki/biblioteka-pygame-chast-1-vvedenie
    В данном файле создаётся и запускается шаблон игры

"""

def main():
    pygame.init()
    pygame.mixer.init() # инициализация звука
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('PyGame Tutorial')
    clock = pygame.time.Clock()

    # цикл игры
    running = True
    while running:
        # держим цикл на правильной скорости
        clock.tick(FPS)

        # цикл обработки событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK) # отрисовка экрана
        pygame.display.flip() # переворот экрана

    pygame.quit()


if __name__ == '__main__':
    main()
