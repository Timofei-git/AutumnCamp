# Задача 3
# базовый уровень
# Напиши версию fib с мемоизацией через словарь. Сравни время вычисления fib(35) у наивной версии и у версии с мемоизацией.
import time

def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo )
    return memo[n]

def fib_recursive(n):
    if n <= 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

start = time.time()
print(fib(10))
print(time.time() - start)
start1 = time.time()
print(fib_recursive(35))
print(time.time() - start1)
