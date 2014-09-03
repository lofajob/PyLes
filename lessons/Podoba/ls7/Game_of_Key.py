# -*- coding: utf-8 -*-
# Game of Key

#function of menu
def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry

    return input(question) - 1

#initialize list of items in the room
# u - �� ������� ������
items = ["�����", "�������", "����", "������", "�����", "����"]

#initialize variables for loops
keylocation =2

keyfound = 0

loop = 1

#Instructions of game
print "�������� ���� �� ���� ����� � ����� ����������� ���� �"
print "�������� ���. "
print ""

print "��� ������������, ��������� � ������� �����. �� �� ���� "
print "�� �� ����� ����, � ����� ����� ������. � ����� ������ "
print len(items), "�����: "

#show all items
for x in items:
    print x
print ""
print "���� �������! ������� ���� ���� �������� ������?"

# main loop of program. it will be closed when player will find the key
while loop == 1:
    choice = menu(items, "�� ������ ������ ����? ")

    if choice == 0:
        if choice == keylocation:
            print " ���� �������� � �����!"
            print ""

            keyfound = 1
        else:
            print "� ����� ����� �� ����."
            print ""
    #repeat the same for other items
    elif choice == 1:
        if choice == keylocation:
            print "�� ������� ���� �� ��������!"
            print ""
            keyfound =1
        else:
            print "�� �������� ����� �� ����."
            print ""

    elif choice == 2:
        if choice == keylocation:
            print "���� ��� � ���!"
            print ""
            keyfound = 1
        else:
            print "���� ���� ������."
            print ""
    elif choice == 3:
        if choice == keylocation:
            print "���� ��� ��� ��������"
            print ""
            keyfound = 1
        else:
            print "�� ����� �� ������� ��� ��������."
            print ""
    elif choice == 4:
        if choice == keylocation:
            print "���. � ���� ��� ����!"
            print ""
            keyfound = 1
        else:
            print "� ���� ����� ����."
            print ""
    #special choice - door
    elif choice ==5:
        #if key has been found - door will be open
        if keyfound ==1:
            loop = 0
            print "    �� ������� ���� � ������� �����, � ��������� ����!"
            print ""
        else:
            print " ���� �������, �������� ����� ������ ����."
            print ""

#The end
print "����� ����������� � ������� ���� ������� ����� ����. "\
      "���� �� �� �������!"
    
        



















