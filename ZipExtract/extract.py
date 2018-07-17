import zipfile

exampleZip = zipfile.ZipFile('example.zip')

exampleZip.extractall()

exampleZip.close()
