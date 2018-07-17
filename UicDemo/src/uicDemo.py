'''
Created on 2 мая 2018 г.

@author: danny
'''

#-*-coding: utf-8 -*-
#
# Демонстрация загрузки ui-формы при программным способом
from PyQt5 import QtWidgets,QtCore, uic

class MyWin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent) #вызов конструктора базового класса
        uic.loadUi("MyForm.ui", self) #ГРУЗИМ из ui файла в класс MyWin (self)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit) #обращаемся к виджету
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText('Привет, мир!')
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.show()
    sys.exit(app.exec())
    

        