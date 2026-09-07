# Задача 1
# базовый уровень
# Создай класс Cat с атрибутами name и age и методом meow(), который печатает «{имя} говорит: Мяу!». Создай два объекта класса и вызови метод у каждого.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f'{self.name} is {self.age} years old and says meow')

first_cat = Cat('James', 20)
first_cat.meow()
second_cat = Cat('Money', 30)
second_cat.meow()