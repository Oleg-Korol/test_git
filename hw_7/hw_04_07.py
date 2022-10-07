# Ex. 4
# Реализовать класс Box, который принимает в себя экземпляры класса Shape.
# Реализовать методы
# - add_shape - добавляет фигуру в текущую коллекцию
# - remove_shape - удаляет последн добавленную фигуру
# - get_common_area - возвращает общую площадь всех фигур
#

from base import Shape
from hw_02_07 import Retangle
from hw_03_07 import Circle

class Box(Retangle,Circle,Shape):
    def __init__(self,*args):
        pass

    def add_shape(self):
        col = []
        return col.append(self.figure)

    def remove_shape(self):
        col = []
        return col.pop(-1)
    def get_common_area(self):
        col = []
        return sum(col)

a=Box(2,4)
print(a.get_area())
b=Box(4)
