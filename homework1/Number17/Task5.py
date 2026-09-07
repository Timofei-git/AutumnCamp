# Задача 5
# средний уровень
# Создай базовый класс Shape с методом area(), который просто возвращает 0.
# Создай классы-наследники Circle и Square, каждый со своей формулой площади в area(). Собери список из нескольких фигур и в цикле выведи площадь каждой.
import math


class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def __str__(self):
        return f'The area of circle is {self.area()}'

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width**2

    def __str__(self):
        return f'The area of Square is {self.area()}'

figures = [
    Square(5),
    Square(4),
    Circle(3),
    Circle(2)
]

for figure in figures:
    print(figure)


