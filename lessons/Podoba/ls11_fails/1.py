#! /usr/bin/env python
# -*- coding: utf-8 -*-


def menu(list_, question):
    for entry in list_:
        print 1 + list_.index(entry),
        print ") " + entry

    try:
        return input(question) - 1
    except NameError:
        print u"Будь ласка, введіть число від 1-8"

<<<<<<< HEAD
# store list of options for menu
=======
# assign list of options for menu
>>>>>>> 58c3053a3dcbb951d0bcfaf1043902fc235ecc6d
options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
loop = 1

while loop == 1:
    answer = menu(options, u'Яка ваша улюблена літера? ')
    try:
        print u'Ваша відповідь ' + (options[answer])
        loop = 0
    except:
        pass