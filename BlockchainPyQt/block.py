#-*- coding: utf-8 -*-

import json,os, hashlib

BLOCKCHAIN_DIR = os.curdir + '/blockchain/'

#пишем функцию переопределяющую хэш каждого блока
def get_hash(filename):
	
	file = open(BLOCKCHAIN_DIR + filename, 'rb').read()
	return hashlib.md5(file).hexdigest()

#получает отсортированный список файлов
def get_files():
	files = os.listdir(BLOCKCHAIN_DIR)
	files =sorted([int(i) for i in files])
	return files


#проверка целостности блоков
def check_integrity():
	
	# составляем имя следующего файла в цепочке
	files = get_files()
	#список для хранения имени блока и результата
	results = []
	#получаем хэши всех имеющихся файлов
	for file in files[1:]:
		h = json.load(open(BLOCKCHAIN_DIR + str(file)))['hash']
		prev_file = str(file-1)
		actual_hash = get_hash(prev_file)
		
		if h == actual_hash:
			res = 'OK'
		else:
			res = 'Нарушен'

		results.append({'block': prev_file, 'result': res})

	return 	results



# функция, которая занимается записью в блок
def write_block(name, amount, to_whom, prev_hash=''):

	
	# составляем имя следующего файла в цепочке
	files = get_files()
	prev_file = files[-1]
	filename = str(prev_file + 1)
	# print(filename)
	prev_hash = get_hash(str(prev_file))


	# приблизительная модель данных
	data = {'name': name,
			 'amount': amount,
			 'to_whom': to_whom,
			 'hash':prev_hash}

	with open(BLOCKCHAIN_DIR + filename,'w') as file:
		json.dump(data, file, indent=4, ensure_ascii=False)
			 




 

def main():
	# write_block('VITYA', 3000, 'DAN')
	print(check_integrity())





if __name__ == "__main__":
	main()
