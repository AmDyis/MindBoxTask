import math

class Shape:
    def get_area(self):
        raise NotImplementedError("Метод area должен быть реализован")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.val_triangle()

    def val_triangle(self):
        if not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            raise ValueError("Такого треугольника не существует")

    def get_area(self):
        self.val_triangle()
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def get_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
            return True
        else:
            return False

def calculate_area(shape: Shape):
    return shape.get_area()


