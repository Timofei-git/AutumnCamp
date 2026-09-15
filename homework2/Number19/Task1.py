# Напиши функцию is_even(n), проверяющую чётность числа через побитовое И с единицей. Проверь на числах от 1 до 10.

def is_even(n):
    return n & 1

lst = range(10)
print('0 - четное, 1 - нечетное')
for num in lst:
    print(f'Число {num} четное: {is_even(num)}')