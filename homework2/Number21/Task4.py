# Напиши функцию sieve(n), возвращающую список всех простых чисел до n включительно методом решета Эратосфена. Проверь на n = 30.

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

print(sieve(30))