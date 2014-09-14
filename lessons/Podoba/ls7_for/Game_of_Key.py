<<<<<<< HEAD
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
print "Останньої ночі ви пішли спати у своєму комфортному ліжку у"
print "власному домі. "
print ""

print "Але прокинувшись, опинились в закритій кімнаті. Ти не знаєш "
print "як ти попав туди, і навіть котра година. В кімнаті лежить "
print len(items), "":

#show all items
for x in items:
    print x
print ""
print "Двері зачинені! Можливо ключ десь всередині кімнати?"

=======
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
print "Останньої ночі ви пішли спати у своєму комфортному ліжку у"
print "власному домі. "
print ""

print "Але прокинувшись, опинились в закритій кімнаті. Ти не знаєш "
print "як ти попав туди, і навіть котра година. В кімнаті лежить "
print len(items), "":

#show all items
for x in items:
    print x
print ""
print "Двері зачинені! Можливо ключ десь всередині кімнати?"

>>>>>>> 58c3053a3dcbb951d0bcfaf1043902fc235ecc6d
