#Задача 16: Квадратное уравнение
#Считайте коэффициенты a, b, c квадратного уравнения ax² + bx + c = 0.
# Если a == 0, уравнение линейное — обработайте отдельно.
# Иначе найдите дискриминант.
# Выведите корни (2 корня / 1 корень / нет корней).

def solve_the_squares(a, b, c):
    if a == 0:
        return f'One root {-c/b}'
    elif b**2 - 4*a*c < 0:
        return 'No roots'
    elif b**2 - 4*a*c == 0:
        return f'One root {-b/(2*a)}'
    else:
        return f'the first root is {(-b + (b**2 - 4*a*c)**0.5) / (2 * a)}, the second is {(-b - (b**2 - 4*a*c)**0.5) / (2 * a)}'

first = int(input("Enter first number:"))
second = int(input("Enter second number:"))
third = int(input("Enter third number:"))
print(solve_the_squares(first, second, third))