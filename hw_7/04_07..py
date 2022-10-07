# Ex. 4
# Реализовать класс Box, который принимает в себя экземпляры класса Shape.
# Реализовать методы
# - add_shape - добавляет фигуру в текущую коллекцию
# - remove_shape - удаляет последн добавленную фигуру
# - get_common_area - возвращает общую площадь всех фигур



from base import Shape
from hw_02_07 import Retangle
from hw_03_07 import Circle

class Box:
    def __init__(self):
        self.acc = []

    def add_shape(self, inst):
        if isinstance(inst, Shape):
            self.acc.append(inst.get_area())

    def remove_shape(self):
        self.acc.pop()


    def get_common_area(self):
        sum(self.acc)





