"# -*- coding: utf-8 -*-"
# Програма калькулятор

# Змінна для зупинки циклу
loop = 1
# Змінна для вибору дії
choise = 0

print "Набір дій"
print "1) Додавання"
print "2) Віднімання"
print "3) Множення"
print "4) Ділення"
print "5) Закрити калькулятор"
    
while loop==1:


    choise = input("Оберіть Вашу дію: ")
    if choise ==1:
        num1 = input("Додати це число: ")
        num2 = input("до цього: ")

        print num1, "+", num2, "=", num1+num2
        
    if choise ==2:
        num1 = input("Від числа: ")
        num2 = input("відняти число: ")

        print num1, "-", num2, "=", num1-num2
    
    if choise ==3:
        num1 = input("Множимо число :")
        num2 = input("на: ")

        print num1, "*", num2, "=", num1*num2
        
    if choise ==4:
        num1 = input("Ділимо число: ")
        num2 = input("на: ")

        print num1, "/", num2, "=", float(num1)/float(num2)

    if choise ==5:
        loop = 0

#Кінець програми
print "Дякуємо за користування калькулятором. Приходьте ще!"
