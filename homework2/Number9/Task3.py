# Модифицируй quick_sort так, чтобы она печатала опорный элемент и получившиеся части на каждом уровне рекурсии. Запусти на списке из 7 чисел и посмотри на дерево вызовов.

def quick_sort(arr):
    if len(arr) < 2:
        return arr

    opp = arr[len(arr)//2]

    left = [x for x in arr if x < opp]
    right = [x for x in arr if x > opp]
    middle = [x for x in arr if x == opp]

    print(f'Опорный элемент: {opp}, меньшая часть: {left}, средняя часть: {middle}, большая часть: {right}')
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([3, 6, 8, 10, 1, 2, 1]))