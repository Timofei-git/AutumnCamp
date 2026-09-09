# Напиши функцию bubble_sort(arr), сортирующую список по возрастанию. Проверь на [5, 2, 8, 1].
# Добавь в свою сортировку флаг, который прерывает работу, если за проход не было ни одного обмена. Проверь на уже отсортированном списке.

def bubble_sort(arr):
    counter = 0 # для 2 задания
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                counter += 1
                swapped = True

        if swapped == False:
            break

    return arr, counter

sorted_lst, counter = bubble_sort([5, 2, 8, 1])
print(sorted_lst)
sorted_lst, counter = bubble_sort([1, 2, 3, 4, 5])
print(sorted_lst, counter)