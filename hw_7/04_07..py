# Ex. 4
# Реализовать класс Box, который принимает в себя экземпляры класса Shape.
# Реализовать методы
# - add_shape - добавляет фигуру в текущую коллекцию
# - remove_shape - удаляет последн добавленную фигуру
# - get_common_area - возвращает общую площадь всех фигур



from base import Shape
from hw_02_07 import Retangle
from hw_03_07 import Circle
import math

class Box:
    def __init__(self):
        self.acc = []

    def add_shape(self, inst):
        if isinstance(inst, Shape):
            self.acc.append(inst)

    def remove_shape(self):
        self.acc.pop()

    def get_common_area(self):
        return sum(list(map(lambda shape: shape.get_area(), self.acc)))


box = Box()
my_shape = Retangle(5,10)
my_shape2 = Circle(5)
box.add_shape(my_shape)
box.add_shape(my_shape2)
assert box.get_common_area() == 5 * 10 + math.pi * 5 ** 2
box.remove_shape()
assert box.get_common_area() == 5 * 10





