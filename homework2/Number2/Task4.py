# Добавь в свою linear_search счётчик сравнений и выведи, сколько сравнений понадобилось для поиска первого,
# среднего, последнего и отсутствующего элемента в списке из 100 чисел.


def linear_search(arr, x):
    counter = 0
    for i in range(len(arr)):
        counter += 1
        if arr[i] == x:
            break

    return counter

number_to_search = int(input("Enter the number: "))
lst = list(range(100))
print(f'Количество сравнений для поиска числа {number_to_search}: {linear_search(lst, number_to_search)}')