# -*- coding: utf-8 -*-
# lesson 2.2

class Guitar:
    body = "mahogany"
    strings = "6"
    pickups = "EMG"

    def changebody(self, newbody):
        self.body = newbody
        print "Guitar has upgraded to %s wood body" % self.body

    def changestrings(self, newstr):
        self.strings = newstr
        print "Guitar has changed to %s strings" % self.strings

    def changepickups(self, newpick):
        self.pickups = newpick
        print "Guitar has upgraded to %s pickups" % self.pickups

class Master:
    name = "John"
    age = 30
    material = "maple"

    def changename(self, newname):
        self.name = newname
        print "Master is %s" % self.name

    def changematerial(self, newmat):
        self.material = newmat
        print "Master %s bought %s wood" % (self.name, self.material)

    #
    def changewood(self):
        # ibz.body = self.material      # change material for class Guitar
        ibz.body = self.material        # change material for object ibz
        print "Master changed body guitar for %s" % self.material
