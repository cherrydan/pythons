'''
Created on 22 авг. 2018 г.
Демонастрашка библиотеки Python Game
@author: В.А.Перлин
'''
# !/usr/bin/python3
# !-*- coding:utf-8 -*-

import sys, pygame

import numpy as np

pygame.init()

print('Для управлением скоростью используйте клавиши-стрелки "вверх-вниз"')
# размер окна
size = width, height = 640, 480

# скорость шарика = количеству fps которые выдаёт комньютер
# внимание! при помощи библиотеки numpy пытаемся их задать в формале float32
speed = np.array([0.2, 0.3], dtype=np.float32) * 400  # ускоряем всё это дело в 400 раз
pos = np.array([width / 2, height / 2], dtype=np.float32)

# цвет

black = (0, 0, 0)

# привяжем движение шарика к таймеру, чтобы его скорость не зависела от мощности компьютера
T = pygame.time.get_ticks()

# создаем окно
screen = pygame.display.set_mode(size)

# создаем мячик из графического файла
ball = pygame.image.load("smiling.png")

# область экрана, прямоугольник, который занимает мяч
ballrect = ball.get_rect()

# event-loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            speed *= 1.1
        # попробую сделать замедление шарика
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            speed /= 1.1

    t = pygame.time.get_ticks()
    T, t = t, (t - T) / 1000

    pos += speed * t

    ballrect.center = tuple(np.array(pos, dtype=int))

    # отслеживаем ударения шарика от краев экрана
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # ставим черный фон для экрана
    screen.fill(black)
    # двигаем изображение вместе с прямоугольной областью
    screen.blit(ball, ballrect)

    # замещаем буфферы (двойной буффер) для исключения эффекта "старого телевизора"    (моргание)
    pygame.display.flip()
