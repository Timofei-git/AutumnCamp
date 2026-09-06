# Задача 4
# средний уровень
# Дан список чисел. С помощью filter и lambda оставь только отрицательные числа.

def find_negative(lst):
    return list(filter(lambda x: x < 0, lst))

numbers = [-5, 3, -1, 0, 2, -10, 7, -3, 8]
print(find_negative(numbers))