# Напиши функцию is_sorted(arr), которая за один проход проверяет, отсортирован ли список по возрастанию. Укажи её сложность в комментарии.

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True

lst = range(10)
print(f'Список lst отсортирован по возрастанию?: {is_sorted(lst)}')
lst = [x for x in range(10, 1, -1)]
print(f'Список lst отсортирован по возрастанию?: {is_sorted(lst)}')
