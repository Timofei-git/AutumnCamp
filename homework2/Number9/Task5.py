# Напиши функцию find_kth_smallest(arr, k), которая находит k-й по величине элемент,
# используя идею разделения из quicksort, но рекурсивно спускаясь только в ОДНУ нужную часть.

def find_kth_smallest(arr, k):
    if len(arr) < 2:
        return arr

    arr = sorted(set(arr))
    medium = arr[len(arr)//2]

    left = [x for x in arr if x < medium]
    right = [x for x in arr if x > medium]
    middle = [x for x in arr if x == medium]

    if len(left) >= k:
        return find_kth_smallest(left, k)

    elif k <= len(arr) - len(right):
        return middle[0]
    else:
        return find_kth_smallest(right, k - len(left) - len(middle))

print(find_kth_smallest(list(range(10)), 8))