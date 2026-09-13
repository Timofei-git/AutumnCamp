# Перепиши рюкзак так, чтобы использовать одномерный массив dp вместо двумерного.
# Убедись, что ответ совпал с предыдущей задачей, и объясни в комментарии, зачем нужен обратный порядок обхода вместимости.

def knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):   # справа налево!
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]


print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))
# вот этот код скопипастил с платформы, не могу понять почему идем справа налево,