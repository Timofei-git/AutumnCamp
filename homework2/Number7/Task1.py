# Напиши функцию, которая считает, сколько раз число n можно поделить пополам (целочисленно), пока оно не станет равно 1.
# Запусти её для 8, 1024 и 1000000 и укажи в комментарии, какой сложности соответствует такое поведение.
import time


def count_divisors_recursive(n):
    if n == 1:
        return 0
    return 1 + count_divisors_recursive(n//2)

def count_divisors_iterative(n):
    count = 0
    while n != 1:
        count += 1
        n //= 2
    return count

print(count_divisors_recursive(8))
print(count_divisors_iterative(8))
print(count_divisors_recursive(1024))
print(count_divisors_iterative(1024))
print(count_divisors_recursive(1000000))
print(count_divisors_iterative(1000000))

