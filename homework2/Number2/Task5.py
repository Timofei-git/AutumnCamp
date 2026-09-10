# Напиши функцию find_min_and_max(items), которая за один проход находит и минимум, и максимум списка.
# Сравни количество проходов со способом, где minimum и maximum ищутся отдельно.
import random


def find_min_and_max(items):
    min_item = items[0]
    max_item = items[0]
    min_index = 0
    max_index = 0
    for index, item in enumerate(items):
        if item < min_item:
            min_item = item
            min_index = index
        if item > max_item:
            max_item = item
            max_index = index

    return min_index, max_index

lst = [random.randint(1, 100) for i in range(100)]
min_index, max_index = find_min_and_max(lst)
print(f'Минимальный элемент это {lst[min_index]} под индексом {min_index}, макимальный {lst[max_index]} под индексом {max_index}')
