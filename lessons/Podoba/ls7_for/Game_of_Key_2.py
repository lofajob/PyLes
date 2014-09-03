# -*- coding: utf-8 -*-
# Game of Key

import random

#function of menu
def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry

    return input(question) - 1

# function check of choice
def check(choice, location):
    if choice == location:
        print ""
        print u"Ви знайшли ключ!"
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

#initialize variables for loops
keylocation = random.randint(0,5)

keyfound = 0

loop = 1

#Instructions of game
print u"Останньої ночі ви пішли спати у своєму комфортному ліжку у"
print u"власному домі. "
print ""

print u"Але прокинувшись, опинились в закритій кімнаті. Ти не знаєш "
print u"як ти попав туди, і навіть котра година. В кімнаті лежить ",len(items), u"речей: "

#show all items
for x in items:
    print x
print ""
print u"Двері зачинені! Можливо ключ десь всередині кімнати?"

# main loop of program. it will be closed when player will find the key
while loop == 1:
    keyfound = check(menu(items, u"Де будемо шукати ключа? "), keylocation) 
    if keyfound == 1:
            print u"Ти вставив ключ у замкову щілину, і провернув його!"
            print ""
            loop = 0
#The end
print u"Світло пробивається у відкриту крізь відчинені тобою двері. "\
      u"Двері до твоєї свободи!"
    
        



















