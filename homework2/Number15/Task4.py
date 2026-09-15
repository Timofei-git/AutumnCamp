# Замерь время сортировки списка из 100 000
# случайных чисел тремя способами: своей пузырьковой (возьми список поменьше, иначе ждать вечно), своей быстрой и встроенной sorted. Выведи все три времени.
import random
import time


def count_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения функции {func.__name__}: {end - start}')
        return result
    return wrapper


def quick_sort(lst):
    if len(lst) < 2:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    right = [x for x in lst if x > pivot]
    middle = [x for x in lst if x == pivot]
    return quick_sort(left) + middle + quick_sort(right)

@count_time
def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return "Массив отсортирован"

lst = [random.randint(1, 10000) for _ in range(2000)]
start = time.time()
new_lst = sorted(lst)
print(f'Время сортировки с помощью втсроенной функции sorted = {time.time() - start} s')

print(f'Bubble sort: {bubble_sort(lst)}')
random.shuffle(lst)


start = time.time()
new_lst = quick_sort(lst)
print(f'Время сортировки с помощью quick sort = {time.time() - start} s')