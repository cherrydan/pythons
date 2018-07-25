'''
Created on 25 июл. 2018 г.

@author:Видоизменил шаблон под свои действительные нужды - Линукс сохраняет скриншоты криво danny
'''
#! python3
#renameDates - переименовывает файлы, в именах которых даты указаны в кривом формате ГГГГ ММ ДД,
#приводя даты в европейский формат ДД ММ ГГГГ

import shutil, os, re

#Создание регулярного выражения, которому соответствуют даты в американском формате


date_pattern = re.compile(r"""^(.*?)
                                ((19|20)\d\d)-
                                ((0|1)?\d)-
                                ((0|1|2|3)?\d)
                                (.*?)$
                          """,

                          re.VERBOSE)



print('Ищем файлы кривого формата ГГГГ ММ ДД в текущем каталоге (у меня так сохраняет скриншоты Линукс...')

#организация цикла по файлам в рабочем каталоге
for amerFilename in os.listdir('.'):
    mo = date_pattern.search(amerFilename)

#пропуск файлов с именами не содержащими дат
    if mo == None:
        continue

#получение отдельных частей имени файла (группы в регулярном выражении разделены круглыми скобками)
    beforePart = mo.group(1)
    monthPart = mo.group(6)
    dayPart = mo.group(4)
    yearPart = mo.group(2)
    afterPart = mo.group(8)

#формирование дат, соответствующее европейскому стилю
    euroFilename = beforePart + monthPart + '-' + dayPart + '-' + yearPart + afterPart

#получаем абсолютные пути к файлам
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir,amerFilename)
    euroFilename = os.path.join(absWorkingDir,euroFilename)

#переименование файлов
    print('Заменяем имя\n "%s"\n именем\n "%s"... ' %(amerFilename,euroFilename))

    shutil.move(amerFilename, euroFilename)
