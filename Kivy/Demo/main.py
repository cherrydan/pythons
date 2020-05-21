#!/usr/bin/env python
# -*- coding: utf-8 -**-
from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    """
    Класс приложения,
    метод build выстраивает приложение
    """
    def build(self):
        return Button(text='Hello, world!')


MyApp().run()
