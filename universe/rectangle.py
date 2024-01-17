from .shape import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def width(self):
        return self.__width

    def length(self):
        return self.__length

    def perimeter(self):
        return 2 * (self.__width + self.__length)

    def space(self):
        return self.__width * self.__length

    def __str__(self):
        return f"length: {self.length()}, width: {self.width()}"

    def __repr__(self):
        return f"rectangle with {self.__str__()}"