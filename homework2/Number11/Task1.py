# Задача 1
# базовый уровень
# Напиши наивную рекурсивную функцию fib(n) и посчитай ей fib(10) и fib(25). Замерь время выполнения для обоих через модуль time.
import time


def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

start = time.time()
print(fib(10))
end = time.time()
print(f"Время выполнения функции fib(10): {end - start}")
start = time.time()
print(fib(25))
end = time.time()
print(f"Время выполнения функции fib(25): {end - start}")