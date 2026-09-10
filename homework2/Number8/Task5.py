# Напиши функцию find_insert_position(arr, target), которая возвращает индекс, куда нужно вставить элемент в отсортированный список, чтобы он остался отсортированным.
# Для [1, 3, 5] и цели 4 ответ 2.



def find_insert_position(arr, target):
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
    return left


print(find_insert_position([1, 3, 5, 7], 5))