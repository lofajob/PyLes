#menu

def menu(list, question):
    #���������� �� ���� ������ � ������ � ������������ �� �����������
    #�� ����� ��� ���������� ������
    for entry in list:
        #������� �������� ��� ����, ��� ����������� ������ �������� � 1��
        print 1 + list.index(entry),
        print ") " + entry
    return input(question) -1
