# Напиши функцию max_sum_window(arr, k), которая находит максимальную сумму k подряд идущих элементов за один проход. Проверь на [2, 1, 5, 1, 3, 2] при k = 3.

def max_sum_window(arr, k):
    if len(arr) < k:
        return None

    max_sum = sum(arr[:k])

    for i in range(k, len(arr) + 1):
        curr_sum = sum(arr[i-k + 1:i + 1])
        max_sum = max(max_sum, curr_sum)
        print(arr[i-k:i])
    return max_sum

print(max_sum_window([2, 100, 5, 6, 3, 2], 3))
