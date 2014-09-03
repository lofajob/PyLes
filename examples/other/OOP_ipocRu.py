# coding: utf-8
class girl:
    methods = {u'и':'у',u'й':'ю','ти':'щу','ей':'ью','ри':'рю',
               'ери':'еру','ети':'ечу','ись':'усь','йся':'юсь',
               'оди':'ожу','рай':'раю','вись':'вюсь','тись':'чусь'}
    def __init__(self, name = u'Наташа'):
        print u'Привет, меня зовут', name
        self.name = name
    def __del__(self):
        print u'Прощай'
    def __getattr__(self, m):
        for l in xrange( len(m) ):
            try:
                print m[:l] + girl.methods[ m[l:] ]
                return
            except KeyError: pass
        if m[0] != '_': print u'Я не умею это делать'
