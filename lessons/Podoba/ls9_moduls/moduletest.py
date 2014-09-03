#-*- coding: utf-8 -*-

#some variables
years = 8
apples = 23

#some functions
def hello_world():
    print "hi there"

def multiply(value):
    print value * 4

#create class of table
class Table:

    def __init__(self):
        self.color = raw_input(u"Який колір стола? ")
        self.height = raw_input(u"Яка висота стола? ")
        self.price = raw_input(u"Яка ціна стола? ")

    def details(self):
        """Print details of table """
        print u"Цей стіл має висоту " + self.height + u" метрів "
        print u"Цей стіл коштує " + self.price + u" гривень " 
    
