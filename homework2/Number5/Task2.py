# Напиши функцию reverse_list(arr), которая разворачивает список на месте двумя указателями, идущими навстречу.

def reverse_list(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

lst = list(range(11))
print(f'Список до реверса: {lst}')
print(f'Список после реверса: {reverse_list(lst)}')