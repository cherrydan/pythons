'''
Created on 16 июл. 2018 г.

@author: danny
'''
from PyQt5 import uic
from PyQt5 import QtWidgets
import math


def printPi(pos):
    Pi = math.pi
    sPi = str(Pi)

    return sPi[:pos + 2]


class MyWin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)  # вызов конструктора базового класса
        uic.loadUi("mainForm.ui", self)  # ГРУЗИМ из ui файла в класс MyWin (self)
        self.hDigits.valueChanged.connect(self.valuechange)

    def valuechange(self):
        self.leRes.setText('')
        pos = self.hDigits.value()
        self.leRes.setText(printPi(pos))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.setWindowTitle('Печать Пи')
    window.move(window.width() * -2, 0)
    window.show()
    # располагаем окно точно по центру
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.frameSize().width()) // 2
    y = (desktop.height() - window.frameSize().height()) // 2
    window.move(x, y)

    sys.exit(app.exec())
