# Напиши функцию power(base, n) для быстрого возведения в степень за O(log n). Обязательно сохрани результат половины в переменную.

def power(base, n):
    if n == 0:
        return 1
    elif n == 1:
        return base

    half = power(base, n//2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * base

print(power(2, 5))