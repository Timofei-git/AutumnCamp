# Напиши функцию, которая для списка чисел печатает все возможные пары. Укажи в комментарии её сложность.
import random


def find_pairs(lst):
    new_lst = []
    for i in range (len(lst) - 1):
        for j in range (i + 1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in new_lst:
                new_lst.append(lst[i])

    return new_lst

lst = [random.randint(1,100) for i in range(50)]
print(lst)
print(find_pairs(lst))
