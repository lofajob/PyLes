#! /usr/bin/env python
# -*- coding: utf-8 -*-

# isalpha string method

n = raw_input("Enter a word: ")

if len(n) > 0 and n.isalpha():
	print n
else:
	print "empty or non alphabetical characters!"