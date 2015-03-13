# -*- coding: utf-8 -*-

class Animal(object):

    def __init__(self, name):
        self.name = name
        self.legs = 4

    def getName(self):
        return self.name

    def repr(self):
        print "Animal has %s name, and has %s legs" % self.name, self.legs


class Dog(Animal):

    def gav(self):
        print "Dog %s is saying gav" % self.name
        
