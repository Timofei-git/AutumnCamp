# Напиши функцию find_all_positions(items, target), которая возвращает список всех индексов, где встретилось значение.
import random


def find_all_positions(items, target):
    positions = []
    for index, item in enumerate(items):
        if target == item:
            positions.append(index)
    return positions

number_to_search = int(input("Enter the number: "))
lst = [random.randint(0, 20) for _ in range(100)]


print(f'Number {number_to_search} occurs on positions: {find_all_positions(lst, number_to_search)}')