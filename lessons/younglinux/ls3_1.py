# -*- coding: utf-8 -*-
# lesson 3.1

class YesInit:
    def __init__(self, one, two):
        self.fname = one
        self.sname = two

class YInit:
    def __init__(self, one="noname", two="nonametoo"):
        self.fname = one
        self.sname = two


obj1 = YInit("Alex","Okey")
obj2 = YInit()
obj3 = YInit("Spartak")
obj4 = YInit(two="Harry")

print (obj1.fname, obj1.sname)
print (obj2.fname, obj2.sname)
print (obj3.fname, obj3.sname)
print (obj4.fname, obj4.sname)
