# Напиши функцию avg_window(arr, k), которая возвращает список средних значений всех окон ширины k. Для [1, 3, 2, 6] и k = 2 результат [2.0, 2.5, 4.0].

def avg_window(arr, k):
    average_list = []

    for i in range(len(arr) - k + 1):
        current_sum = sum(arr[i:i+k])
        average_list.append(current_sum / k)

    return average_list

print(avg_window([1, 3, 2, 6], 2))