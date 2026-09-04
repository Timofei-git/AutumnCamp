#Задача 15: Проверка треугольника
#Считайте три стороны треугольника. Сначала проверьте, можно ли из них построить треугольник (сумма двух сторон > третьей).
# Если нет — выведите «Не треугольник». Иначе — «Равносторонний», «Равнобедренный» или «Разносторонний».

def define_the_type_of_triangle(first, second, third):
    if first + second <= third or first + third <= second or first + third <= second:
        return "Unsuitable type"
    elif first == second == third:
        return "equilateral"
    elif first == second or first == third or first == second:
        return "isosceles"
    else:
        return "versatile"

first = int(input("Enter a first side:"))
second = int(input("Enter a second side:"))
third = int(input("Enter a third side:"))
print(define_the_type_of_triangle(first, second, third))