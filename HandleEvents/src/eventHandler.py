'''
Created on 30 апр. 2018 г.

@author: danny
'''
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets

import sys


"""
def on_clicked()
- функция-заглушка, которая вызывается при щелчке на кнопке
"""

def on_clicked():
    print('Метод on_clicked()')
    app.quit()


#класс для обработки события
class MyClass():
    def __init__(self, x=0):
        self.x = x

    def __call__(self):
        print('Кнопка нажата - метод MyClass.__call__() ')
        print('x = ' + str(self.x))

    def on_clicked(self):
        print('Кнопка нажата - метод MyClass.on_clicked()')


obj = MyClass()

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('Нажми меня')

#назначаем обработчиком функцию
button.clicked.connect(on_clicked)

#назначаем обработчиком метод класса
button.clicked.connect(obj.on_clicked)

#назначем обработчиком экземпляр класса
button.clicked.connect(MyClass(10))

#назначаем обработчиком ламбда-функцию анонимную
button.clicked.connect(lambda: MyClass(5)())

button.show()

sys.exit(app.exec())


