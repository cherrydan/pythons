#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt5 import QtWidgets, uic 

from PyQt5.QtWidgets import QMessageBox

from block import *


def show_error_message(text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle('Критическая ошибка!')
        msg.setInformativeText(text)
        msg.exec_()



class MyWin(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self,parent)
		uic.loadUi('mainForm.ui',self)
		self.setWindowTitle('Демо блокчейна')
		self.write_button.clicked.connect(self.on_clicked)
		self.integrity_button.clicked.connect(self.on_integrity_clicked)

	def on_clicked(self):
		lender = self.le_lender.text()
		amount = self.le_amount.text()
		borrower = self.le_borrower.text()

		try:
			write_block(name=lender,amount=amount,to_whom=borrower)
			self.le_lender.setText('')
			self.le_amount.setText('')
			self.le_borrower.setText('')

		except OSError:
			show_error_message('Произошла системная ошибка!')
			
	def on_integrity_clicked(self):
		result = []
		str_text = ''

		result = check_integrity()

		for res in result:
			str_text += 'Блок ' + res['block'] + ': ' + res['result'] + '\n'

		self.te_integrity.setText(str_text)	

		











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