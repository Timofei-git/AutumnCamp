# Расширь задачу: разреши прыжки на 1, 2 или 3 ступени. Напиши функцию и посчитай ответ для n = 5.

def climb_stairs(n):
    if n <= 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]

print(climb_stairs(5))