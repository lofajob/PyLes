# -*- coding: utf-8 -*-
# Game of Key

import random

#function of menu


def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry
    return 

# function check of choice


def check(choice, location):
    if choice < 1 or choice > 6:
        print u"Введіть, будь ласка, число в діапазоні 1-6!"
        print ""
    elif type(choice) <> int:
        print u"Введіть ціле число в діапазоні 1-6!"
        print ""
    else:
        if choice == location:          
            print ""
            print u"Ура! Ви знайшли ключ!"
            print ""
            return 1
        else:
            print ""
            print u"Тут нічого не було."
            print ""
            return 0

#initialize list of items in the room
# u - це юнікодові стрічки
items = [u"вазон", u"картина", u"ваза", u"абажур", u"туфля", u"двері"]

#initialize variables for loop
keylocation = random.randint(1, 6)

keyfound = 0

loop = 1

#Instructions of game
print u"Останньої ночі ви пішли спати у своєму комфортному ліжку у"
print u"власному домі. "
print ""

print u"Але прокинувшись, опинились в закритій кімнаті. Ти не знаєш "
print u"як ти попав туди, і навіть котра година. В кімнаті лежить ",len(items), u"речей: "

#show all items
menu(items, '')
print ""

#for x in items:
#    print x
#print ""

print u"Двері зачинені! Можливо ключ десь всередині кімнати?"

#main loop of program. it will be closed when player will find the key
while loop == 1:
    keyfound = check(input(u"Де будемо шукати ключа? "), keylocation) 
    if keyfound == 1:
            print u"Ти вставив ключ у замкову щілину, і провернув його!"
            print ""
            loop = 0
#The end
print u"Світло пробивається у відкриту крізь відчинені тобою двері. "\
      u"Двері до твоєї свободи!"
    
        



















