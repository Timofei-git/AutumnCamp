# Реализуй quick_sort(arr) через генераторы списков и опорный элемент из середины. Проверь на списке [3, 6, 8, 10, 1, 2, 1].

def quick_sort(arr):
    if len(arr) < 2:
        return arr

    opp = len(arr)//2

    left = [x for x in arr if x < arr[opp]]
    right = [x for x in arr if x > arr[opp]]
    middle = [x for x in arr if x == arr[opp]]

    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([3, 6, 8, 10, 1, 2, 1]))