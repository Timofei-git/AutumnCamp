# Задача 2: Площадь прямоугольника
# Считайте ширину и высоту прямоугольника (целые числа). Выведите его площадь.

def countSquare(width, height):
    return width*height

width = int(input('Enter width: '))
height = int(input('Enter height: '))
print(countSquare(width, height))