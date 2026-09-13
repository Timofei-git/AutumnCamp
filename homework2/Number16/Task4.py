# Реализуй задачу о рюкзаке 0/1 через двумерную таблицу dp. Проверь на весах [1, 3, 4, 5], ценностях [1, 4, 5, 7] и вместимости 7 — ответ 9.

def knapsack(weights, values, capacity):
    if capacity == 0:
        return 0

    dp = [[0] * (capacity + 1) for _ in range(len(values) + 1)]
    for i in range(1, len(values) + 1):
        for j in range(1, capacity + 1):
            dp[i][j] = dp[i - 1][j]
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i][j],dp[i - 1][j - weights[i-1]] + values[i - 1])


    return dp[len(values)][capacity]


print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))