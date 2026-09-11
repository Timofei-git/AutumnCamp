# Напиши функцию min_sum_window(arr, k), находящую минимальную сумму окна ширины k.

def min_sum_window(arr, k):
    min_sum = sum(arr[:k])

    for i in range(1, len(arr) - k + 1):
        curr_sum = sum(arr[i:i + k ])
        min_sum = min(min_sum, curr_sum)

    return min_sum

print(min_sum_window([1, 2, 3, 4], 2))
print(min_sum_window([5, -3, 4, 2, -5, 1, -18], 4))

