# Задача 3
# базовый уровень
# Напиши две функции, которые проверяют наличие дубликатов в списке: первую через два вложенных цикла, вторую через множество set. Укажи сложность каждой в комментарии.

def first_checker(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True

    return False # O(n**2)

def second_checker(lst):
    return len(lst) != len(set(lst)) # O(n)


print(f'У списка есть дубликаты: {first_checker([1, 2, 3, 4, 5, 5])}')