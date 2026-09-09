# Напиши функцию merge_sorted(a, b), которая сливает два отсортированных списка в один отсортированный, используя по указателю на каждый список.
import random


def merge_sorted(a, b):
    left = right = 0
    final_list = []
    while left < len(a) and right < len(b):
        if a[left] == b[right]:
            final_list.extend([a[left], b[right]])
            left += 1
            right += 1
        elif a[left] < b[right]:
            final_list.append(a[left])
            left += 1
        else:
            final_list.append(b[right])
            right += 1

    final_list.extend(a[left:]) # у меня всегда оставался один невнесенный элемент в каком-то из списков
    final_list.extend(b[right:])

    return final_list

lst_1 = sorted([random.randint(1, 10) for _ in range(20)])
print(lst_1)

lst_2 = sorted([random.randint(1, 10) for _ in range(10)])
print(lst_2)

print(merge_sorted(lst_1, lst_2))

