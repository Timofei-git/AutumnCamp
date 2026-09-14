# Задача 4
# средний уровень
# Напиши функцию count_inversions(arr), которая считает количество пар элементов,
# стоящих в неправильном порядке (когда более ранний элемент больше более позднего), используя модифицированное слияние.


def merge(left, right, counter = 0):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
            counter += len(left[i:])


    result.extend(left[i:])
    result.extend(right[j:])

    return counter, result


def merge_sort(arr):
    if len(arr) <= 1:
        return 0, arr

    mid = len(arr) // 2

    left_counter, left = merge_sort(arr[:mid])
    right_counter, right = merge_sort(arr[mid:])

    return merge(left, right, left_counter + right_counter)


print(merge_sort([5, 4, 3, 2, 1]))