"# -*- coding: utf-8 -*-"
# �������� �����������

# ����� ��� ������� �����
loop = 1
# ����� ��� ������ 䳿
choise = 0

print "���� ��"
print "1) ���������"
print "2) ³�������"
print "3) ��������"
print "4) ĳ�����"
print "5) ������� �����������"
    
while loop==1:


    choise = input("������ ���� ��: ")
    if choise ==1:
        num1 = input("������ �� �����: ")
        num2 = input("�� �����: ")

        print num1, "+", num2, "=", num1+num2
        
    if choise ==2:
        num1 = input("³� �����: ")
        num2 = input("������ �����: ")

        print num1, "-", num2, "=", num1-num2
    
    if choise ==3:
        num1 = input("������� ����� :")
        num2 = input("��: ")

        print num1, "*", num2, "=", num1*num2
        
    if choise ==4:
        num1 = input("ĳ���� �����: ")
        num2 = input("��: ")

        print num1, "/", num2, "=", float(num1)/float(num2)

    if choise ==5:
        loop = 0

#ʳ���� ��������
print "������ �� ������������ �������������. ��������� ��!"
