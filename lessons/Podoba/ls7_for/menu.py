<<<<<<< HEAD
#menu

def menu(list, question):
    #пробагіэмся по усых опціях у списку і роздруковуємл їх користувачу
    #на екран для побальшого вибору
    for entry in list:
        #додаэмо одиничку для того, щоб користувачу список почиався з 1ці
        print 1 + list.index(entry),
        print ") " + entry
    return input(question) -1
=======
#menu

def menu(list, question):
    #пробагіэмся по усых опціях у списку і роздруковуємл їх користувачу
    #на екран для побальшого вибору
    for entry in list:
        #додаэмо одиничку для того, щоб користувачу список почиався з 1ці
        print 1 + list.index(entry),
        print ") " + entry
    return input(question) -1
>>>>>>> 58c3053a3dcbb951d0bcfaf1043902fc235ecc6d
