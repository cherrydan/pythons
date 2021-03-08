'''
Обходим каталог home/danny при помощи модуля питона os

Также удаляем файл в корзину при помощи библиотеки send2send2trash

'''
import os
import send2trash

baconFile = open('bacon.txt', 'a')

baconFile.write('Bacon is not a vegitable')

baconFile.close()

send2trash.send2trash('bacon.txt')

counter = 0

uPath = ""

uPath = input('Введите путь к файлам, которые нужно пройти: ')

for folderName, subFolders, fileNames in os.walk(uPath):
    print('Текущая папка - ' + folderName)

    for subfolder in subFolders:
        print('ПОДПАПКА ПАПКИ ' + folderName + ': ' + subfolder)

    for filename in fileNames:
        print('ФАЙЛ В ПАПКЕ ' + folderName + ': ' + filename)
        counter += 1

print('')
print('Всего файлов пройдено: ' + str(counter))
