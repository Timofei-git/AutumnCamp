# Напиши две функции — merge_sort и наивный fib — и добавь в обе кеш через словарь.
# Замерь время до и после кеширования для обеих. Объясни в комментарии, почему кеш помог только одной.
import random, time


def merge(left, right):
    arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i = i + 1
        elif left[i] > right[j]:
            arr.append(right[j])
            j = j + 1
        else:
            arr.extend([right[j], left[i]])
            j = j + 1
            i = i + 1

    arr.extend(right[j:])
    arr.extend(left[i:])

    return arr


def merge_sort(arr, cache={}):
    key = tuple(arr)
    if key in cache:
        return cache[key]

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], cache)
    right = merge_sort(arr[mid:], cache)
    result = merge(left, right)

    cache[key] = result
    return result


def fib(n, cache={}):
    if n in cache:
        return cache[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    result = fib(n - 1, cache) + fib(n - 2, cache)
    cache[n] = result
    return result

lst = [random.randint(1, 99) for _ in range(1000)]

start = time.time()
merge_sort(lst)
print("merge_sort с кешем:", time.time() - start)

start = time.time()
fib(30)
print("fib с кешем:", time.time() - start)
# кэш поможет только наивной фибоначчи потому что значения которые вычисляются часть втсречаются больше одного раза а в мердж сорт шанс одинаковые значения  почти не встречаются и смысла в кешировании нет
