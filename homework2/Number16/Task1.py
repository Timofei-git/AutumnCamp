# Напиши функцию climb_stairs(n) для лестницы с шагами 1 и 2 ступени двумя способами: через массив dp и через две переменные. Проверь, что обе дают одинаковый ответ для n от 1 до 10.

def climb_stairs(n):
    if n <= 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

def climb_stairs2(n):
    if n == 0:
        return 1
    if n <= 3:
        return n

    prev_2, prev_1 = 1, 2
    for _ in range(3, n + 1):
        current = prev_1 + prev_2
        prev_2, prev_1 = prev_1, current

    return prev_1



for i in range(11):
    print(f'Количество поднятий на {i} ступеньку с помощью первого способа: {climb_stairs(i)}, второго способа: {climb_stairs2(i)}')