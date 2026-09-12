# Напиши наивную функцию is_prime_naive(n), перебирающую все делители от 2 до n-1. Проверь её на числах 2, 17, 20 и 1.
import math


def is_prime_naive(n):
    if n < 2:
        return False
    if n == 2:
        return True

    for i in range(2, n - 1):
        if n % i == 0:
            return False

    return True

print(f'Число 4 простое: {is_prime_naive(4)}')
print(f'Число 17 простое: {is_prime_naive(17)}')
print(f'Число 1 простое: {is_prime_naive(1)}')
print(f'Число 20 простое: {is_prime_naive(20)}')
