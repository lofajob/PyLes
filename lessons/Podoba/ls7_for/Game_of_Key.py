<<<<<<< HEAD
# Game of Key

#function of menu
def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry

    return input(question) - 1

#initialize list of items in the room
# u - �� ������� ������
items = [u"�����", u"�������", u"����", u"������", u"�����", u"����"]

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
print len(items), "":

#show all items
for x in items:
    print x
print ""
print "���� �������! ������� ���� ���� �������� ������?"

=======
# Game of Key

#function of menu
def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry

    return input(question) - 1

#initialize list of items in the room
# u - �� ������� ������
items = [u"�����", u"�������", u"����", u"������", u"�����", u"����"]

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
print len(items), "":

#show all items
for x in items:
    print x
print ""
print "���� �������! ������� ���� ���� �������� ������?"

>>>>>>> 58c3053a3dcbb951d0bcfaf1043902fc235ecc6d
