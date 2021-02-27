#-*- coding: utf-8 -*-

'''
Created on 28 апр. 2018 г.

@author: danny
'''



from PyQt5 import QtCore, QtWidgets

def show_modal_window():
    global modalWindow
    modalWindow = QtWidgets.QWidget(window1, QtCore.Qt.Window)
    modalWindow.setWindowTitle('Модальное окно')
    modalWindow.resize(200, 50)
    modalWindow.setWindowModality(QtCore.Qt.WindowModal)
    modalWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    modalWindow.move(window1.geometry().center() - modalWindow.rect().center() -
        QtCore.QPoint(4,30))
    modalWindow.show()




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window1 = QtWidgets.QWidget()
    window1.setWindowTitle('Обычное окно')
    window1.resize(300, 100)
    button = QtWidgets.QPushButton('Модальное окно')
    button.clicked.connect(show_modal_window)
    vbox = QtWidgets.QVBoxLayout()
    vbox.addWidget(button)
    window1.setLayout(vbox)
    window1.show()

    window2 = QtWidgets.QWidget()
    window2.setWindowTitle('Это окно не будет блокировано при WindowModal')
    window2.resize(300, 100)
    window2.show()

    sys.exit(app.exec())






