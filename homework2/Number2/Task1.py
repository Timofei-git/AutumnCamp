# Напиши функцию linear_search(items, target), которая возвращает индекс найденного элемента или -1. Не используй index и оператор in.
import random


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1

number_to_search = int(input("Enter the number: "))
lst = [random.randint(0, 20) for _ in range(100)]
print(f'The index of number is: {linear_search(lst, number_to_search)}')