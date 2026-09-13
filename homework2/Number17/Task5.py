# Напиши функцию, которая ищет пару ближайших по значению элементов в отсортированном списке методом деления пополам,
# и в комментарии объясни, ДП это или D&C и почему.


def find_closest(arr):
    if len(arr) == 1:
        return None  # сигнал "пары здесь нет"

    if len(arr) == 2:
        return (arr[0], arr[1], abs(arr[0] - arr[1]))  # пара + разница

    mid = len(arr) // 2
    left_result = find_closest(arr[:mid])
    right_result = find_closest(arr[mid:])

    return combine(left_result, right_result, arr[mid - 1], arr[mid])

def combine(left_result, right_result, left, right):
    min_diff = float('inf')
    best_pair = None

    if left_result is not None:
        best_pair = left_result
        min_diff = abs(left_result[0] - left_result[1])

    if right_result is not None:
        diff = abs(right_result[0] - right_result[1])
        if diff < min_diff:
            best_pair = right_result
            min_diff = diff

    if abs(left - right) < min_diff:
        best_pair = (left, right, abs(left - right))
        min_diff = abs(left - right)

    return best_pair

arr = [1, 4, 7, 9, 11, 20]
print(find_closest(arr))
# это D&C потому что результат прошлых вычислений не используется
# сам полностью задачу не осилил





