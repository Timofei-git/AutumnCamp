# Напиши функцию min_coins(coins, amount), которая через ДП находит минимальное количество монет для набора суммы, и верни -1, если сумма недостижима.
# Проверь на номиналах [1, 3, 4] и сумме 6 — должно получиться 2.

def min_coins(n, coins):

    dp = [n + 1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for c in coins:
            dp[i] = min(dp[i], dp[i - c] + 1)

    if dp[n] > n:
        return -1
    else:
        return dp[n]


print(min_coins(6, [1, 3, 4]))

