<<<<<<< HEAD
# -*- coding: utf-8 -*-
# lesson 3_3

class Building:
    def __init__(self,w,c,n=0):
        self.what = w
        self.color = c
        self.numbers = n
        self.mwhere(n)

    def mwhere(self,n):
        if n<= 0:
            self.where = u"відсутні "
        elif 0 < n < 100:
            self.where = u"малий склад"
        else:
            self.where = u"основний склад"

    def plus(self,p):
        self.numbers += p
        self.mwhere(self.numbers)

    def minus(self,m):
        self.numbers -= m
        self.mwhere(self.numbers)


ob1 = Building(u'Цегла',u'червона',275)
ob2 = Building(u'Дошка',u'сосна',50)
ob3 = Building(u'Фарба',u'Біла')
=======
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# lesson 3_3


class Building:
    def __init__(self, w, c, n=0):
        self.what = w
        self.color = c
        self.numbers = n
        self.mwhere(n)

    def mwhere(self, n):
        if n <= 0:
            self.where = u"відсутні "
        elif 0 < n < 100:
            self.where = u"малий склад"
        else:
            self.where = u"основний склад"

    def plus(self, p):
        self.numbers += p
        self.mwhere(self.numbers)

    def minus(self, m):
        self.numbers -= m
        self.mwhere(self.numbers)


ob1 = Building(u'Цегла', u'червона', 275)
ob2 = Building(u'Дошка', u'сосна', 50)
ob3 = Building(u'Фарба', u'Біла')

print ob1.what, ob1.color, ob1.where
print ob2.what, ob2.color, ob2.where
print ob3.what, ob3.color, ob3.where
 
ob1.plus(500)
print ob1.numbers, ob1.where
>>>>>>> 58c3053a3dcbb951d0bcfaf1043902fc235ecc6d
