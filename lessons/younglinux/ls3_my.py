#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Bank customer

class Customer:
    def __init__(self, name, bal = 0, cur = 'UAR'):
        cur = cur.upper()
        if  cur != 'UAR' and cur != 'EUR' and cur != 'USD':
            print u"Некоректно введена валюта."
        else:
            self.name = name
            self.currency = cur
            self.bal = bal
            self.show(cur)

    def show(self,cur):
        if cur == 'UAR':
            print u"Клієнт: %s має на рахунку %s грн" % (self.name, self.bal)
        elif cur == 'USD':
            print u"Клієнт: %s має на рахунку %s доларів" % (self.name, self.bal)
        elif cur == 'EUR':
            print u"Клієнт: %s має на рахунку %s євро" % (self.name, self.bal)
        else:
            print u"Невідома валюта!"

    
