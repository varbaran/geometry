from .shape import Shape

class Square(Shape):
    def __init__(self, side):
        self.__side = side
    # private field (self.__side) getter
    def side(self):
        return self.__side

    def perimeter(self):
        return 4 * self.__side

    def space(self):
        return self.__side ** 2

    def __str__(self):
        result =""
        for i in range(int(self.side())):
            for j in range(int(self.side())):
                if i == 0 or i == int(self.side()) - 1:
                    if j == 0:
                        result += " "
                    elif j == int(self.side()) - 1:
                        result += "-"
                    else:
                        result += "-\t"
                else:
                    if j == 0 or j == int(self.side()) - 1:
                        result += "|"
                    if j != int(self.side()) - 1:
                        if j != int(self.side()) - 2:
                            result += "\t"
                        else:
                            result += " "
            result += "\n"
        return result

    def __repr__(self):
        return f"square with side: {self.side()}"