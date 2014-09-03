# -*- coding: utf-8 -*-
# Game of Key

#function of menu
def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry

    return input(question) - 1

#initialize list of items in the room
# u - це юнікодові стрічки
items = [u"вазон", u"картина", u"ваза", u"абажур", u"туфля", u"двері"]

#initialize variables for loops
keylocation =2

keyfound = 0

loop = 1

#Instructions of game
print u"Останньої ночі ви пішли спати у своєму комфортному ліжку у"
print u"власному домі. "
print ""

print u"Але прокинувшись, опинились в закритій кімнаті. Ти не знаєш "
print u"як ти попав туди, і навіть котра година. В кімнаті лежить "
print len(items), "речей: "

#show all items
for x in items:
    print x
print ""
print u"Двері зачинені! Можливо ключ десь всередині кімнати?"

# main loop of program. it will be closed when player will find the key
while loop == 1:
    choice = menu(items, u"Де будемо шукати ключ? ")

    if choice == 0:
        if choice == keylocation:
            print u" ключ знайдено у вазоні!"
            print ""

            keyfound = 1
        else:
            print u"У вазоні нічого не було."
            print ""
    #repeat the same for other items
    elif choice == 1:
        if choice == keylocation:
            print u"Ти знайшов ключ за картиною!"
            print ""
            keyfound =1
        else:
            print u"За картиною нічого не було."
            print ""

    elif choice == 2:
        if choice == keylocation:
            print u"Ключ був у вазі!"
            print ""
            keyfound = 1
        else:
            print u"Ваза була пустою."
            print ""
    elif choice == 3:
        if choice == keylocation:
            print u"Ключ був над абажуром"
            print ""
            keyfound = 1
        else:
            print u"Ти нічого не знайшов над абажуром."
            print ""
    elif choice == 4:
        if choice == keylocation:
            print u"Ура. В туфлі був ключ!"
            print ""
            keyfound = 1
        else:
            print u"В туфлі нічого немає."
            print ""
    #special choice - door
    elif choice ==5:
        #if key has been found - door will be open
        if keyfound ==1:
            loop = 0
            print u"    Ти вставив ключ у замкову щілину, і провернув його!"
            print ""
        else:
            print u" Двері зачинені, спочатку варто знайти ключ."
            print ""

#The end
print u"Світло пробивається у відкриту крізь відчинені тобою двері. "\
      u"Двері до твоєї свободи!"
    
        



















