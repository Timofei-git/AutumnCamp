# Напиши функцию, которая печатает значения left, right и mid на каждой итерации бинарного поиска. Запусти её и посмотри, как сужается диапазон при поиске элемента в списке из 16 чисел.

def binary_search(arr, target):
    if arr is None or len(arr) == 0:
        return "Список пустой"
    left = 0
    right = len(arr) - 1
    while left <= right:
        print(f'left: {left}, right: {right}')
        mid = (left + right) // 2

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return mid
    return "Число не найдено"

lst = list(range(16))
print(binary_search(lst, 5))