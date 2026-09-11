# Задача 1
# базовый уровень
# Напиши функцию merge(left, right), которая сливает два уже отсортированных списка в один отсортированный. Проверь на [1, 4, 7] и [2, 3, 9].

# Задача 2
# базовый уровень
# Используя свою merge, реализуй merge_sort(arr) и отсортируй ей [38, 27, 43, 3, 9, 82, 10].

# Задача 3
# базовый уровень
# Добавь в merge_sort печать текущего куска массива в начале каждого вызова. Запусти на списке из 8 элементов и по выводу проследи, как массив дробится.

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.extend([left[i], right[j]])
            i += 1
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    print(f'Отсортированный Кусок массива: {result}')  # для 3 таски

    return result

print(merge([1, 4, 7], [2, 3, 9]))

def merge_sort(arr):
    print(f'Кусок массива: {arr}')# для 3 таски
    if len(arr) <= 1:
        return arr


    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))