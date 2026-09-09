# Задача 3
# базовый уровень
# Сделай версию bubble_sort_desc(arr), которая сортирует список по убыванию.

def bubble_sort_asc(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if swapped == False:
            break

    return arr

sorted_lst = bubble_sort_asc([5, 2, 8, 1])
print(sorted_lst)