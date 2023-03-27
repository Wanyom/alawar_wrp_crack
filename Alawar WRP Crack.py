# -*- coding: utf-8 -*-

print("[Alawar WRP Crack] Чтобы программа работала корректно\nпереустановите игру с путём который не содержит кириллицу и пробелов\n")

import os, sys, shutil

os.system("title Alawar WRP Crack")

# Alawar WRP Crack by Wanyom

path_to_program = os.getcwd()
path1 = f"{path_to_program}"
username = os.getlogin()

print("Alawar WRP Crack, версии 1.1")
print("(c) Wanyom | Все права защищены")

path_to_game = input('\n[Alawar WRP Crack] Введи полный путь до игры (Например: D:\\Games\\SuperCow): ')
if not path_to_game:
	print("[Alawar WRP Crack] Ты не указал путь до игры!")
	input("[Alawar WRP Crack] Нажми Enter, чтобы выйти!")
	sys.exit()

question = input("[Alawar WRP Crack] Вы действительно хотите модифицировать файлы игры? (да / нет): ")
if question.lower() == 'да':
	pass
else:
	sys.exit()

try:
	os.remove(f'{path_to_game}\\wrapper.dll')
except:
	print("[Alawar WRP Crack] Не удалось удалить 'wrapper.dll', возможно ты указал неверный путь до игры!")
	input("[Alawar WRP Crack] Нажми Enter, чтобы выйти!")
	sys.exit()
else:
	print("[Alawar WRP Crack] 'wrapper.dll' удалён, копирую модифицированный файл...")
	try:
		shutil.copy(f"{path1}\\wrapper.dll", f"{path_to_game}\\")
	except:
		print("[Alawar WRP Crack] Не удалось завершить патч игры из-за ошибки...")
		input("[Alawar WRP Crack] Нажми Enter, чтобы выйти!")
		sys.exit()
	else:
		print("[Alawar WRP Crack] Патч игры завершён успешно!")
		input("[Alawar WRP Crack] Нажми Enter, чтобы выйти!")
		sys.exit()