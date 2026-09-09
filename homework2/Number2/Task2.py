# Напиши функцию count_occurrences(items, target), которая считает, сколько раз значение встречается в списке.
import random


def count_occurrences(items, target):
    counter = 0
    for item in items:
        if item == target:
            counter += 1

    return counter

number_to_search = int(input("Enter the number: "))
lst = [random.randint(0, 20) for _ in range(100)]


print(f'Number {number_to_search} occurs {count_occurrences(lst, number_to_search)} times')