# Напиши рекурсивную функцию sum_to(n), считающую сумму чисел от 1 до n. Проверь на n = 5.

def sum_to(n):
    if n == 1:
        return 1
    return n + sum_to(n - 1)

print(sum_to(5))