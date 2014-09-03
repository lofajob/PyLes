#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

# assign test dictionary
mylist = ['hello', 3, 'seven', 'else', 432, 'more text for dictionatry']

#create new file 
myfile = open('my_file.db', 'w')

# а тепер збережемо наш словник використовуючи функцію dump
# функція dump отримує два аргумента: дані, які треба зберігати;
# а другим параметром - відкритий для читання файл - куди писати
pickle.dump(mylist, myfile)

myfile.close()
		