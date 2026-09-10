# Напиши две функции, которые проверяют наличие дубликатов в списке: первую через два вложенных цикла, вторую через множество set. Укажи сложность каждой в комментарии.
import random, time


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

lst = [random.randint(1, 100) for _ in range(10000)]
print(f'У списка есть дубликаты: {first_checker(lst) }')
print(f'У списка есть дубликаты: {second_checker(lst)}')

# при небольшом разбросе и количестве данных время выполнения первой функции иногда может быть меньше чем время выполнения второй, но при увеличении количества данных и их разброса,
# время выполнения второй функции будет меньше