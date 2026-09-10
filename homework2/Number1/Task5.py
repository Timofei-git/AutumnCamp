# Напиши функцию, которая проверяет, есть ли в списке два одинаковых числа, двумя способами: перебором всех пар и через множество set.
# Замерь время обеих на списке из 5000 чисел и объясни, почему второй способ быстрее.
import random
import time


def count_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения функции {func.__name__}: {end-start}')
        return result
    return wrapper

@count_time
def first_checker(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True

    return False # O(n**2)

@count_time
def second_checker(lst):
    return len(lst) != len(set(lst)) # O(n)

lst = [random.randint(1,100000000) for i in range(50000)]

print(first_checker(lst))
print(second_checker(lst))
# Второй способ будет быстрее в случаях когда разброс значений огромен, при 50000 эелементах и разбросе в значений от 1 до 10000 скорее всего будет быстрее первый способ,
# так как при нахождении хотя бы одной пары он возвращает True
