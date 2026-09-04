# Задача 3: Количество делителей
# Найдите количество делителей числа n (не считая самого числа). Например, делители 12: 1, 2, 3, 4, 6.

def count_divisors(number):
    count = 1

    if number == 0 or number == 1:
        return 0
    if number == 2 or number == 3:
        return 1
    for i in range(2, int(number ** 0.5)):
        if number % i == 0:
            count += 1

            pair = number // i
            if pair != i:
                count += 1

    return count

number = int(input("Enter a number: "))
print(f'The amount of divisors of number {number} is {count_divisors(number)}')
