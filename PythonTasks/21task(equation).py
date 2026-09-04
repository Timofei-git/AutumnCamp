#Задача 21: Кубическое уравнение
#С клавиатуры вводятся числа a, b, c и d.
# Нужно вывести корни уравнения третьей степени ax³ + bx² + cx + d = 0.
# Учитывайте в решении, что a, b, c и d могут быть и нулем.

def division_on_d(d):
    divided_numbers = [1, -1]
    for i in range(2, d + 1):
        if d % i == 0:
            divided_numbers.extend([i, -i])

    return divided_numbers

def solve_the_squares(a, b, c):
    if a == 0:
        return f'One root {-c/b}'
    elif b**2 - 4*a*c < 0:
        return 'No roots'
    elif b**2 - 4*a*c == 0:
        return f'One root {-b/(2*a)}'
    else:
        return f'the first root is {(-b + (b**2 - 4*a*c)**0.5) / (2 * a)}, the second is {(-b - (b**2 - 4*a*c)**0.5) / (2 * a)}'

def solve_the_fourth_root(a, b, c, d):
    result = []
    divided_numbers = division_on_d(d)
    for i in divided_numbers:
        if a * pow(i, 3) + b * pow(i, 2) + c * pow(i, 1) + d == 0:
            result.append(str(i))

    return f"The solution is: {", ".join(result)}" if len(result) > 0 else "No solution"

def find_solution(a, b, c, d):
    if a != 0:
        return solve_the_fourth_root(a, b, c, d)
    else:
        return solve_the_squares(b, c, d)


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))
print(find_solution(a, b, c, d))