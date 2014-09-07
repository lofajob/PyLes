#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Bank customer


class Customer:
    def __init__(self, name, bal = 0, cur = 'UAR'):
        # checking the correct currency value
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

    def show_balance(self):
        print self.bal, self.currency

    def deposit(self, amount):
        if amount > 0:
            self.bal += amount
        else:
            print "Enter money!"

    def withdraw(self, wdrw):
        if wdrw <= self.bal:
            self.bal -= wdrw
        else:
            print "You can't withdraw %s %s. Your current balance: %s." % (wdrw,
            self.currency, self.bal)
