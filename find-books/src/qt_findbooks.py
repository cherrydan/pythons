# -*- coding: utf-8 -*-
#!/usr/bin/python3

# импортируйте необходимые пакеты
import cv2,sys

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication

def find_books(path):
# загрузите изображение, смените цвет на оттенки серого и уменьшите резкость
	image = cv2.imread(path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (3, 3), 0)
	cv2.imwrite("gray.jpg", gray)

	# распознавание контуров
	edged = cv2.Canny(gray, 10, 250)
	cv2.imwrite("edged.jpg", edged)


	# создайте и примените закрытие
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
	closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
	cv2.imwrite("closed.jpg", closed)

	# найдите контуры в изображении и подсчитайте количество книг
	cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
	total = 0

	# цикл по контурам
	for c in cnts:
		# аппроксимируем (сглаживаем) контур
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)

		# если у контура 4 вершины, предполагаем, что это книга
		if len(approx) == 4:
			cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
			total += 1

	#

	cv2.imwrite("output.jpg", image)

	return total

class MyWin(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        exitAction = QAction('&Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выход из программы')
        exitAction.triggered.connect(qApp.quit)

        openAction = QAction('&Открыть...',self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Открывает графический файл')
        openAction.triggered.connect(self.on_openFile)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Ищем книгу на картинке')
        self.show()
        
    def on_openFile(self):
    	return 
	

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyWin()
    sys.exit(app.exec_())


