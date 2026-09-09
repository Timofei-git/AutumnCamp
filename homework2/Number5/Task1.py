# Напиши функцию two_sum_sorted(arr, target), которая ищет в отсортированном списке пару чисел с заданной суммой. Проверь на [1, 3, 4, 6, 8, 9] и цели 11.

def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return left, right
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1

    return None, None

lst = list(range(10))
target = int(input("Введите искомое число: "))
left, right = two_sum_sorted(lst, target)
if left is not None and right is not None:
    print(f"Числа {lst[left]} и {lst[right]} в сумме дают искомое число {target}")
else:
    print(f"Невозможно найти сумму {target} из списка {lst}")