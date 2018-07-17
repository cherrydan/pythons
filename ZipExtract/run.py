import zipfile, os

os.chdir('./')


exampleZip = zipfile.ZipFile('example.zip')

print(exampleZip.namelist())

spamInfo = exampleZip.getinfo('spam.txt')

print(str(spamInfo.file_size))

print(str(spamInfo.compress_size))

message = 'Сжатый файл в %s раз меньше ' % (round(spamInfo.file_size /
spamInfo.compress_size,2))

print(message)

exampleZip.close()
