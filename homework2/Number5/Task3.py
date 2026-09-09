# Напиши функцию remove_duplicates(arr), убирающую повторы из отсортированного списка. Проверь на [1, 1, 2, 3, 3, 3, 4].

def remove_duplicates(arr):
    left = 0
    right = len(arr) - 1
    while left < right + 1:
        if arr[right - 1] == arr[right]:
            arr.remove(arr[right])
        right -= 1
    return arr

print(remove_duplicates([1, 1, 2, 3, 3, 3, 4]))
