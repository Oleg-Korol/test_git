# Ex. 2
# Импортировать из base.py класс Shape и унаследовать класс Rectangle.
# Реализовать конструктор (__init__) (подумать, какие параметры нужны при создании объекта) и
# метод get_area.
# Реализовать методы сложения и вычитания объектов,
# результатом которых будет новое значение площади (объекты при этом не меняются).
# Написать проверки.


from base import Shape

class Retangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

b=Retangle(2,3)
assert b.get_area()==6
assert b.perimeter()==10





