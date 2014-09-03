#! /usr/bin/env python
# -*- coding: utf-8 -*-

# відкриваємо файл my_file.txt, що знаходиться всередині папки
# Documents; відкриваємо його для читання - другий аргумент є 'r' (read)
myfile = open('/home/oleksiy/Документы/my_file.txt', 'r')

# а тепер вичитуємо весь вміст файлу my_file.txt з допомогою метода
# read вказівника файлу (так званого дескриптора - у нашому випадку myfile);
print myfile.read()

second_file = open('/media/oleksiy/Data/Тунчик.txt', 'r')
print second_file.read()

#Програємось з переміщенням курсору
myfile.seek(0) 			#переміщення на початок файлу
print myfile.read()

print myfile.read()		#пустий рядок, бо курсор перейшов до кінця

myfile.seek(-23,1)		#переміщення на 23 символи з поточного вказівника
print myfile.read()

myfile.seek(-100,2)		#переміщення на 100 символів з кінця файлу
print myfile.read()
