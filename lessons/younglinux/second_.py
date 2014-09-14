<<<<<<< HEAD
# -*- coding: utf-8 -*-
# lesson 2

class Second:
    color = "Red"
    form = "sqare"
    author = "author"

    def changecolor(self, newcolor):
        self.color = newcolor


    def changeform(self, newform):
        self.form = newform

    def changeauthor (self, newauthor):
        self.author = newauthor
        
a = Second()
b = Second()
c = Second()

print "object a color = %s, object b color = %s , object c = %s"% (a.color, b.color, c.color)
print "object a form = %s, object b form = %s, object c form = %s" % (a.form, b.form, c.form)

print "something will change"
a.changecolor('white')
b.changeform('point')
c.changecolor('green')
c.changeform('circle')
print "object a color = %s, object b color = %s , object c = %s"% (a.color, b.color, c.color)
print "object a form = %s, object b form = %s, object c form = %s" % (a.form, b.form, c.form)

print a.author, b.author, c.author
a.changeauthor('Lofa')
c.changeauthor('Oleksiy')
print a.author, b.author, c.author
=======
# -*- coding: utf-8 -*-
# lesson 2

class Second:
    color = "Red"
    form = "sqare"


    def changecolor(self, newcolor):
        self.color = newcolor


    def changeform(self, newform):
        self.form = newform
        
>>>>>>> 58c3053a3dcbb951d0bcfaf1043902fc235ecc6d
