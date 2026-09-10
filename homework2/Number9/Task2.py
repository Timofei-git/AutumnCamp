# Напиши функцию partition(arr, pivot), которая возвращает три списка: меньше опорного, равные ему и больше. Проверь её отдельно от сортировки.

def partition(arr, pivot):

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    return left, middle, right

lst = [3, 6, 8, 10, 1, 2, 1]
left, middle, right = partition(lst, lst[len(lst) // 2])
print(f'меньшая часть: {left}, средняя часть(равны опорному): {middle}, большая часть: {right}')