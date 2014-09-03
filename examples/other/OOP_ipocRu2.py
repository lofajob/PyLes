#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class girl:
    dic = {'и':'у','й':'ю','ти':'щу','ей':'ью','ри':'рю',
           'ери':'еру','ети':'ечу','ись':'усь','йся':'юсь',
           'оди':'ожу','рай':'раю','вись':'вюсь','тись':'чусь'}
    udic = dict([(k.decode('utf-8'), v.decode('utf-8')) for k, v in dic.items()])
    
    def __init__(self, name = 'Наташа'):
        print u'Привет, меня зовут', name.decode('utf-8')
        self.name = name.decode('utf-8')
    def __del__(self):
        print u'Прощай'
    def do(self, m):
        m = m.decode('utf-8')
        for key in self.udic.keys():
            if m[-len(key):] == key:
                print ''.join([m[:-len(key)],self.udic[key]]).encode(sys.stdout.encoding)
                return
        print u'Я не умею это делать'


