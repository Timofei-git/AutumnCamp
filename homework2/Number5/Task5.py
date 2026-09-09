# Напиши функцию closest_sum(arr, target), которая находит пару чисел с суммой, максимально близкой к заданной.
# Сравни её время работы с решением через перебор всех пар на списке из 2000 чисел.
import random
import time


def count_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start} seconds')
        return result
    return wrapper

@count_time
def closest_sum(arr, target):
    max_closest, max_closest2 = 0, 0
    left, right = 0, len(arr) - 1
    closest_sum = -1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return arr[left], arr[right]
        if abs(curr_sum - target) < abs(closest_sum - target) or closest_sum == -1:
            closest_sum = curr_sum
            max_closest = left
            max_closest2 = right

        if arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1

    return arr[max_closest], arr[max_closest2]

@count_time
def closest_sum2(arr, target):
    max_closest, max_closest2 = 0, 0
    closest_sum = -1
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            curr_sum = arr[i] + arr[j]
            if curr_sum == target:
                return arr[i], arr[j]
            if abs(curr_sum - target) < abs(closest_sum - target) or closest_sum == -1:
                closest_sum = curr_sum
                max_closest = j
                max_closest2 = i

    return arr[max_closest], arr[max_closest2]

lst = sorted([random.randint(1, 20000) for _ in range(2000)])
print(closest_sum(lst, 4567))
print(closest_sum2(lst, 4567))
# время выполнения второй функции занимает в разы больше чем время первой из-за сложности O(n**2)

