# -*- coding: utf-8 -*-

class Win_Door(object):
    def __init__(self, x, y):
        self.square = x * y

class Room(object):
    def __init__(self, x, y, z):
        self.square = 2 *z * (x + y)
    def win_door(self, d, e, f, g, m=1, n=1):
        self.window = Win_Door(d, e)
        self.door = Win_Door(f, g)
        self.numb_w = m
        self.numb_d = n
        self.wallpapers()
    def wallpapers(self):
        self.wallpapers = self.square - \
            self.window.square * self.numb_w \
            - self.door.square * self.numb_d
    def printer(self):
        print u"Площа стін кімнати: "\
              ,str(self.square), u" кв.м"
        if hasattr(Room, 'self.wallpapers') == False:
            print u"Обклеювана площа кімнати: ",\
                  str(self.wallpapers), u"кв.м"
        else:
            pass 
