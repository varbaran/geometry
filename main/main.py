from universe.circle import Circle
from universe.square import Square
from universe.rectangle import Rectangle

def main():
    shapes = []
    while True:
        selection = input("""choose an option:
    1: for creating a shape
    2: for showing shapes
    3: for selecting shapes
        """)
        if selection == "1":
            selection = input("""choose an option:
    1: for creating a circle
    2: for creating a rectangle
    3: for creating a square
                    """)
            if selection == "1":
                radius = float(input("please enter radius: "))
                if radius <= 0:
                    print("invalid radius")
                    continue
                shapes.append(Circle(radius))
            elif selection == "2":
                width = float(input("please enter width: "))
                length = float(input("please enter length: "))
                if width <= 0 or length <= 0:
                    print("invalid input")
                    continue
                shapes.append(Rectangle(length, width))
            elif selection == "3":
                side = float(input("please enter side: "))
                if side <= 0:
                    print("invalid side")
                    continue
                shapes.append(Square(side))
            else:
                print("invalid option")
                continue
        elif selection == "2":
            # calls each object's __repr__
            print(shapes)
        elif selection == "3":
            selection = int(input("enter shape number: "))
            if selection <= 0 or selection > len(shapes):
                print("invalid option")
                continue
            # calls object's __str__
            print(shapes[selection - 1])
        else:
            print("invalid option")
            continue


if __name__ == '__main__':
    main()