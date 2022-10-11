# Ex. 3
# Импортировать из base.py класс Shape и унаследовать класс Circle.
# Реализовать конструктор (__init__) (подумать, какие параметры нужны при создании объекта) и
# метод get_area.
# Реализовать методы сложения и вычитания объектов,
# результатом которых будет новое значение площади (объекты при этом не меняются).
# Написать проверки.


import math

from base import Shape

class Circle(Shape):
    import math
    def __init__(self,radius):
        self.radius=radius

    def get_area(self):
        return math.pi*self.radius*self.radius

    def len_circle(self):
        return 2 * math.pi * self.radius
r=Circle(1)

assert round(r.get_area(),2)==3.14
assert round(r.len_circle(),2)==6.28