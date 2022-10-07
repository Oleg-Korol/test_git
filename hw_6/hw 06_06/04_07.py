
from base import Shape

class Box:
    def __init__(self):
        self.acc=[]

    def add_shape(self,inst):
        if isinstance(inst,Shape):
            self.acc+=inst.get_area()
