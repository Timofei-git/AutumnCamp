# Напиши оптимизированную функцию is_prime(n), которая перебирает делители только до корня из n. Проверь, что она даёт те же ответы, что и наивная, на числах от 1 до 50

# Замерь время работы обеих функций на числе 1000003 (оно простое) и выведи разницу.

import time


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнение функции {func.__name__}: {end_time - start_time}')
        return result
    return wrapper

@count_time
def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1

    return True

@count_time
def is_prime_naive(n):
    if n < 2:
        return False
    if n == 2:
        return True

    for i in range(3, n - 1):
        if n % i == 0:
            return False

    return True

print(f'Число {1000003} простое?: Нативная функция: {is_prime_naive(1000003)}, оптимизированная функция: {is_prime(1000003)}')