# Сравни время работы решета и функции is_prime из предыдущей главы при поиске всех простых чисел до 100000. Выведи оба времени и объясни разницу в комментарии.
import time

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

def primes_up_to(n):
    if n >= 2:
        yield 2
    for i in range(3, n):
        if is_prime(i):
            yield i

def sieve(n):
    dp = [True] * (n + 1)
    dp[0] = False
    dp[1] = False

    i = 2
    while i * i <= n:
        if dp[i]:
            for j in range(i * i, n + 1, i):
                dp[j] = False

        i += 1
    return [i for i in range(1, n + 1) if dp[i]]

start = time.time()
sieve(100000)
print(f'Время выполненич фнукции sieve: {time.time() - start}')

start = time.time()

primes_up_to(100000)

print(f'Время выполненич фнукции is_prime: {time.time() - start}')

assert sieve(100000) == list(primes_up_to(100000))
print("Результат одинаковый")