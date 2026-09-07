# Задача 2
# базовый уровень
# Создай класс Rectangle с атрибутами width и height и методом area(), который возвращает площадь. Создай объект и выведи площадь через print.

# Задача 3
# базовый уровень
# Добавь классу Rectangle из прошлой задачи метод __str__, чтобы print(объект) выводил что-то осмысленное вроде «Прямоугольник 5x10».

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f'Rectangle({self.width}*{self.height})'

first_rectangle = Rectangle(2, 3)
print(first_rectangle.area())
print(first_rectangle)