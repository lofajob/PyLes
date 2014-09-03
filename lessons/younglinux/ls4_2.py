# -*- coding: utf-8 -*-
# ls 4_2

class Figure(object):
    color = "white"
    def changecolor(self, newcolor):
        self.color = newcolor

class Oval(Figure):
    def __init__(self, r):
        self.radius = r

        
class Square(Figure):
    def __init__(self, x):
        self.x = x
        
abs = Figure()
ov = Oval(43)
kv = Square(5)
