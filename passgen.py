# Простой генератор паролей

import random

symbols =  '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def generate(len):
	len = int(len)
	if len > 50:
		print("Длина пароля не может быть более 50 символов")
		main()
	else:
		password = ''
		for i in range(len):
			password += random.choice(symbols)
		return password
			
def main():
	print("[1] Генератор пароля")
	menu = input(">>> ")
	menu = int(menu)
	if menu == 1:
		len = input("Длина пароля >>> ")
		print("Результат: " + str(generate(len)))
		main()
	else:
		print("Выберите пункт из меню")
		main()
		
main()