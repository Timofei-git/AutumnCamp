# Добавь в сортировку счётчик сравнений и счётчик обменов. Выведи оба числа для списка [5, 2, 8, 1], для уже отсортированного и для отсортированного в обратном порядке.

def bubble_sort(arr):
    counter_comparison = 0 # сравнения
    counter_exchange = 0 # обмены
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-i-1):
            counter_comparison += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                counter_exchange += 1
                swapped = True

        if swapped == False:
            break

    return arr, counter_comparison, counter_exchange

sorted_lst, counter_comparison, counter_exchange = bubble_sort([5, 2, 8, 1])
print(f'Отсортированный массив {sorted_lst}, счетчик сравнений: {counter_comparison}, счетчик обменов: {counter_exchange}')
sorted_lst, counter_comparison, counter_exchange = bubble_sort([1, 2, 5, 8])
print(f'Проверка на уже отсортированном массиве, счетчик сравнений: {counter_comparison}, счетчик обменов: {counter_exchange}')
sorted_lst, counter_comparison, counter_exchange = bubble_sort([8, 6, 2, 1])
print(f'Проверка на отсортированноv в обратном порядке массиве, счетчик сравнений: {counter_comparison}, счетчик обменов: {counter_exchange}')
