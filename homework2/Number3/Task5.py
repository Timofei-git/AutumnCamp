# Напиши функцию, которая печатает состояние списка после каждого прохода сортировки, и запусти её на списке из восьми случайных чисел.
# Убедись, что после каждого прохода в конце оказывается ещё одно число на своём месте.
import random


def bubble_sort(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        print(f'{i + 1} итерация: {arr}')
        if swapped == False:
            break

    return arr

lst = [random.randint(1, 100) for i in range(8)]
sorted_lst = bubble_sort(lst)
print(sorted_lst)