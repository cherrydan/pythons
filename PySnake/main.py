#! /usr/bin/python3
# -*- coding: utf-8 -*-

#############################################
#
#           PYGAME DEMO
#
#           игра-змейка (с) Хауди Хо
#
#############################################

import pygame

# initialize pygame
pygame.init()

# initialize display
display = pygame.display.set_mode((640, 480))

pygame.display.update()
pygame.display.set_caption('Snake Demo by Howdy Ho')

game_end = False

while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True

    pygame.draw.rect(display, (0, 255, 0), [640 / 2 - 5, 480 / 2 - 5, 10, 10])
    pygame.display.update()

pygame.quit()
quit(0)
