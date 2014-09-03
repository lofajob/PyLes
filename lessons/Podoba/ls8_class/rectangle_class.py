#coding: utf-8
#class of rectangle
class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    despription = "none"
    author = "none"

    def area(self):
        """Обчислюємо площу прямокутника"""
        return self.x * self.y

    def perimeter(self):
        """Обчислюємо периметр прямокутника"""
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        """Встановлюємо означення прямокутника"""
        self.description = text

    def authorName(self, text):
        """Встановлюємо автора прямокутника"""
        self.author = text

    def scaleSize(self, scale):
        """Змінюємо розміри прямокутника згідно отриманого співвідношення"""
        self.x = self.x * scale
        self.y = self.y * scale
