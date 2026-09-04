# Задача 6: Факториал
# Напишите функцию для вычисления факториала n. Обработайте граничные случаи (0! = 1). Используйте рекурсию.

def factorial(number):
    if number <= 1:
        return 1

    return number * factorial(number - 1)

factor = int(input("Enter a number: "))
print("The factorial of ", factor, "is ", factorial(factor))