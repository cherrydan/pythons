'''
Created on 16 июл. 2018 г.

@author: danny
'''
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


def h_calc(ps, sk, m):

    piece_ps = float(ps) / (100 * 12)

    try:
        k = piece_ps * (1 + piece_ps) ** m /((1 + piece_ps) ** m - 1)
        res = k * sk
        return res

    except ZeroDivisionError:
        return -1


def show_error_message(text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle('Критическая ошибка!')
        msg.setInformativeText(text)
        msg.exec_()





class MyWin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent) #вызов конструктора базового класса
        uic.loadUi("mainForm.ui", self) #ГРУЗИМ из ui файла в класс MyWin (self)
        self.setWindowTitle("Ипотечный калькулятор")
        self.okButton.setEnabled(True)
        self.le_resPlatezh.setEnabled(False)
        self.le_extraPay.setEnabled(False)
        self.okButton.clicked.connect(self.on_clicked) #обращаемся к виджету


    def on_clicked(self):
        ps = self.le_Proc.text()
        m = self.le_Srok.text()
        sk = self.le_Sum.text()

        try:

            res = h_calc(float(ps), int(sk), int(m))

        except ValueError:
            show_error_message('Нужно заполнить все поля в форме!')


        if res != -1:
            res = float('{:.2f}'.format(res))
            extra_pay = (res * int(m)) - int(sk)
            extra_pay = float('{:.2f}'.format(extra_pay))
            self.le_resPlatezh.setEnabled(True)
            self.le_extraPay.setEnabled(True)
            self.le_resPlatezh.setText(str(res))
            self.le_extraPay.setText(str(extra_pay))

        else:
            show_error_message('Процент по кредиту не может быть равен 0!')







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.move(window.width() * -2, 0)
    window.show()
    #располагаем окно точно по центру
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.frameSize().width()) // 2
    y = (desktop.height() - window.frameSize().height()) // 2
    window.move(x,y)

    sys.exit(app.exec())

