# Напиши функцию count_windows_above(arr, k, threshold), которая считает, сколько окон ширины k имеют сумму строго больше threshold.

def count_windows_above(arr, k, threshold):
    counter = 0
    for i in range(len(arr) - k + 1):
        curr_sum = sum(arr[i:i + k])
        if curr_sum > threshold:
            counter += 1

    return counter

print(count_windows_above([4, 1, 3, 2, 6], 2, 5))