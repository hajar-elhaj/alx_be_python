import math
class Shape:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__(width, length)
    def area(self):
        return self.width * self.length

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)