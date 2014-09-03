# -*- coding: utf-8 -*-
# lesson 4_1

class Table(object):
    def __init__(self, l, h, w):
        self.long = l
        self.height = h
        self.weight = w
    def outing(self):
        print self.long, self.height, self.weight

class Kitchen(Table):
    def howplaces(self, n):
        if n < 2:
            print "It isn't kitchen table"
        else:
            self.places = n
    def outplaces(self):
        print self.places

class Medical(Table):
    def equipment(self, dev):
        self.device = dev
        print self.device," was installed to the table"


tab1 = Table(25, 5, 10)

tab2 = Kitchen(11, 2, 4)
tab2.howplaces(6)
