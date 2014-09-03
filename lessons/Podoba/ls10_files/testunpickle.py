#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pickle

# режим відкривання файла є 'rb': r - читати (read), b - бінарний режим,
# тобто даємо знати пітону, що файл містить не текстові дані
myfile = open('my_file.db', 'rb')

mylist = pickle.load(myfile)
myfile.close()

for item in mylist:
	print item