# Задача 5: НОД (алгоритм Евклида)
# Найдите НОД двух чисел без встроенной функции. Используйте рекурсию или алгоритм Евклида.

def define_nod(first, second):
    if first < 0 or second < 0:
        return "Unsuitable  numbers"

    if first == 0:
        return second
    if second == 0:
        return first

    if first == 1 or second == 1:
        return 1

    # while first != second:
    #     if first > second:
    #         first -= second
    #     else:
    #         second -= first

    while second != 0:
        first, second = second, first % second

    return first

first =  int(input("Enter first number: "))
second = int(input("Enter second number: "))
print(f'The result of NODof numbers {first} and {second} is : {define_nod(first, second)}')
