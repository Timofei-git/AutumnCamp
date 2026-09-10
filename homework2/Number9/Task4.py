# Сделай версию quick_sort, которая берёт опорным ПЕРВЫЙ элемент, и запусти её на уже отсортированном списке из 10 чисел, печатая глубину рекурсии.
# Объясни в комментарии, почему получилось столько уровней.

def quick_sort(arr, depth = 0):
    if len(arr) < 2:
        return arr

    opp = arr[0]

    left = [x for x in arr if x < opp]
    right = [x for x in arr if x > opp]
    middle = [x for x in arr if x == opp]

    print(f'Глубина рекурсии: {depth}, меньшая часть: {left}, средняя часть: {middle}, большая часть: {right}')
    return quick_sort(left, depth + 1) + middle + quick_sort(right, depth + 1)

print(quick_sort(list(range(10)), 0))
# уровней получилось столько потому что каждый раз мы брали первый элемент, а в отсортировнном массиве он далеко от среднего по величине элемента