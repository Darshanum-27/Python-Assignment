class Shape:
    def __init__(self):
        pass
    def area(self):
        print("Area of Shape Class: 0")


class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print("Area of Square:"+str(self.length ** 2))

Shape().area()
Square(10).area()