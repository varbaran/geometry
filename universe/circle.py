import math

from .shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def radius(self):
        return self.__radius

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def space(self):
        return math.pi * self.__radius ** 2

    def __str__(self):
        return f"radius: {self.radius()}"

    def __repr__(self):
        return f"circle with {self.__str__()}"