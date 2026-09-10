# Реализуй binary_search(arr, target), возвращающую индекс элемента или -1.
# Проверь её на отсортированном списке из 10 чисел: найди первый элемент, последний, средний и отсутствующий

# Проверь свою реализацию на граничных случаях: пустой список, список из одного элемента (искомый есть) и список из одного элемента (искомого нет).
# Убедись, что нигде нет ошибки и зацикливания.

def binary_search(arr, target):
    if arr is None or len(arr) == 0:
        return "Список пустой"
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return mid
    return "Число не найдено"

lst = [x for x in range(1, 20) if x % 2 == 0]
print(lst)
print(binary_search(lst, lst[0]))
print(binary_search(lst, lst[-1]))
print(binary_search(lst, lst[len(lst)//2]))
print(binary_search(lst, 10000))

print(binary_search([], lst[0]))
print(binary_search([1], 1))
print(binary_search([1], 2))