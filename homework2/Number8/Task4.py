# Напиши функцию find_first(arr, target), которая в отсортированном списке с повторами находит индекс ПЕРВОГО вхождения элемента.
# Для [1, 2, 2, 2, 3] и цели 2 ответ должен быть 1.

def binary_search(arr, target):
    if arr is None or len(arr) == 0:
        return "Список пустой"
    left = 0
    right = len(arr) - 1
    best_index = -1
    while left <= right:
        mid = (left + right) // 2

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            best_index = mid
            right = mid - 1
    return best_index if best_index != -1 else "Число не найдено"

print(binary_search([1, 2, 2, 2, 3], 2))
