#Задача 2: Палиндром
#Проверьте, является ли число палиндромом
# (читается одинаково в обе стороны). Используйте цикл, а не преобразование в строку.

def palindrom(n):
    sum = 0
    copy_num = n
    while copy_num > 0:
        sum = sum * 10 + copy_num % 10
        copy_num //= 10

    return True if sum == n else False

n = int(input("Enter a number for checking: "))
print(f'Number {n} is palindrome: {palindrom(n)}')