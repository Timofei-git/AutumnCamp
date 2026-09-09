# Напиши рекурсивную функцию factorial(n), считающую факториал. Проверь на n = 5 и n = 0.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(0))