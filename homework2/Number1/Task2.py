# Напиши функцию, которая считает сумму всех чисел в списке через цикл (без встроенного sum). Укажи в комментарии её сложность.

def count_sum(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum

lst = [x for x in range(1,21) if x % 3 == 0]
print(count_sum(lst))