# Напиши функцию find_max(arr), которая находит максимум в списке методом «разделяй и властвуй», деля список пополам рекурсивно.
import random


def find_max(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2
    left_max = find_max(arr, left, mid)
    right_max = find_max(arr, mid + 1, right)

    return max(left_max, right_max)


lst = [random.randint(1, 99) for _ in range(20)]
print(lst)
print(find_max(lst, 0, len(lst)-1))