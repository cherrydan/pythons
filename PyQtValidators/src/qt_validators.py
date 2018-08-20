'''
Created on 7 авг. 2018 г.

@author: danny
'''

from PyQt5 import QtWidgets, uic

from PyQt5.QtWidgets import QMessageBox

def whose_card(CardStr):

    if(CardStr[0] == '4'):
        return 'VISA'
    elif (CardStr[0] == '5'):
        return 'MASTER CARD'

    elif (CardStr[0] == '2'):
        return 'МИР'

    elif (CardStr[0] == '3'):
        return 'AMERICAN EXPRESS'

    elif (CardStr[0] == '9'):
        return 'ПРОСТIP'
    else:
        return 'UNKNOWN'

def is_odd_card_number(CardStr):
    if (len(CardStr) % 2 == 0):
        return True
    else:
        return False

def validate_card(CardStr):
    list = []
    evenmultlist = []
    odddigits = []
    allsum = 0
    for lett in CardStr:
            list.append(int(lett))

    l_len = int((len(CardStr) / 2))
    if(is_odd_card_number(CardStr)):
        evencounter = 0

        for i in range(0, l_len):
            app = list[evencounter] * 2
            if (app > 9):
                app = app - 9
                evenmultlist.append(app)
            else:
                evenmultlist.append(app)

            evencounter+=2

        oddcounter = 1
        for x in range(0, l_len):
            odddigits.append(list[oddcounter])
            oddcounter+=2

        for y in range(0, l_len):
            allsum += evenmultlist[y] + odddigits[y]

        if(allsum % 10 == 0):
            return True
        else:
            return False

    else:
        show_error_message('Ошибка! В номере кредитной карты должно быть 16 цифр!')



def validate_EAN(Estr):
    list = []

    l_len = int((len(Estr) - 1) / 2)

    for lett in Estr:
        list.append(int(lett))


    oddsum = 0
    oddmult = 0
    oddcounter = 1
    for i in range(0, l_len):
        oddsum += list[oddcounter]
        oddcounter+=2
    oddmult = oddsum * 3

    evensum = 0
    evencounter = 0

    for i in range(0,l_len):
        evensum += list[evencounter]
        evencounter+=2

    bothsum = oddmult + evensum

    checksum = 10 - (bothsum % 10)

    if list[12] != checksum:
        return False
    else:
        return True


def show_error_message(text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle('ОШИБКА!!')
        msg.setInformativeText(text)
        msg.exec_()


def show_valid_message(text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('БИНГО!!')
        msg.setInformativeText(text)
        msg.exec_()

def show_success_message(text,caption):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(caption)
        msg.setInformativeText(text)
        msg.exec_()


class MyWin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent) #вызов конструктора базового класса
        uic.loadUi("mainForm.ui", self) #ГРУЗИМ из ui файла в класс MyWin (self)
        self.btnEANValid.setEnabled(True)
        self.btnCardValid.setEnabled(True)
        self.btnEANValid.clicked.connect(self.on_EAN_clicked)
        self.btnCardValid.clicked.connect(self.on_Card_clicked)



    def on_Card_clicked(self):
        card_system = " "
        card_str = self.leCard.text()

        if(card_str.isdigit() or len(card_str) == 16):
            card_system = whose_card(card_str)
            if(validate_card(card_str)):
                show_success_message('Карта № ' + card_str + " ВАЛИДНА!", card_system)
                self.leCard.clear()
            else:
                show_error_message('Карта № ' + card_str + " НЕ ВАЛИДНА!")
                self.leCard.clear()

        else:
            show_error_message('Что-то не так с вводом данных!')




    def on_EAN_clicked(self):
        EANStr = self.leEAN.text()

        if (len(EANStr) != 13 or (not(EANStr.isdigit()))):
            show_error_message('ВВОД: только 13 цифр!')
        else:
            if(validate_EAN(EANStr)):
                show_valid_message('Товар со штрих кодом ' + EANStr + ' легален!')
                self.leEAN.clear()
            else:
                show_error_message('Товар со штрих кодом ' + EANStr + ' нелегален!')
                self.leEAN.clear()





if __name__ == '__main__':
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
